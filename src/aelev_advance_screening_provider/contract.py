"""Exact owner-visible compute contract and provider-owned output validation."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, cast

OWNER = "advance-screening"
TASK = "SITE_RELEVANCE"
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
MAX_BODY_BYTES = 1024 * 1024


class RequestInvalid(ValueError):
    """Opaque request did not match the exact owner contract."""


@dataclass(frozen=True, slots=True)
class InferenceRequest:
    request_id: str
    input: dict[str, Any]


def parse_request(value: object, release_digest: str) -> InferenceRequest:
    if not isinstance(value, dict):
        raise RequestInvalid("ASC_PROVIDER_REQUEST_INVALID")
    payload = cast(dict[str, object], value)
    request_id = payload.get("request_id")
    model_input = payload.get("input")
    if (
        set(payload)
        != {"schema_version", "owner", "task", "request_id", "release_digest", "input"}
        or payload.get("schema_version") != 1
        or payload.get("owner") != OWNER
        or payload.get("task") != TASK
        or payload.get("release_digest") != release_digest
        or not isinstance(request_id, str)
        or not 0 < len(request_id) <= 240
        or not isinstance(model_input, dict)
        or len(json.dumps(model_input, ensure_ascii=False).encode()) > MAX_BODY_BYTES
    ):
        raise RequestInvalid("ASC_PROVIDER_REQUEST_INVALID")
    return InferenceRequest(request_id, cast(dict[str, Any], model_input))


def validate_output(value: object) -> dict[str, object]:
    if not isinstance(value, dict):
        raise RuntimeError("PROVIDER_RUNTIME_RESPONSE_INVALID")
    output = cast(dict[str, object], value)
    raw_response = output.get("model_response")
    response = (
        cast(dict[str, object], raw_response)
        if isinstance(raw_response, dict)
        else None
    )
    raw_reasons = output.get("reason_codes")
    reasons = cast(list[object], raw_reasons) if isinstance(raw_reasons, list) else None
    confidence = output.get("confidence")
    if (
        set(output) != {"outcome", "model_response", "reason_codes", "confidence"}
        or output.get("outcome") not in {"ACCEPT", "REJECT", "REVIEW"}
        or response is None
        or set(response) != {"matches_policy", "relevance_score", "rationale"}
        or response.get("matches_policy") not in {True, False, None}
        or not (
            response.get("relevance_score") is None
            or type(response.get("relevance_score")) is int
            and 0 <= cast(int, response["relevance_score"]) <= 100
        )
        or not isinstance(response.get("rationale"), str)
        or not 0 < len(cast(str, response["rationale"])) <= 2000
        or reasons is None
        or not 0 < len(reasons) <= 16
        or any(
            not isinstance(item, str)
            or re.fullmatch(r"[A-Z][A-Z0-9_]{1,63}", item) is None
            for item in reasons
        )
        or not (
            confidence is None or type(confidence) is int and 0 <= confidence <= 100
        )
    ):
        raise RuntimeError("PROVIDER_RUNTIME_RESPONSE_INVALID")
    return output


def response(
    request: InferenceRequest, release_digest: str, output: dict[str, object]
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "owner": OWNER,
        "task": TASK,
        "request_id": request.request_id,
        "release_digest": release_digest,
        "output": output,
    }
