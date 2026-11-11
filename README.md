# AELEV Advance Screening Provider

Independent black-box implementation of the Advance Screening
`SITE_RELEVANCE` compute contract. The image receives owner-collected site
material over mutually authenticated HTTPS and calls the OpenAI Responses API.
Model ID, prompt and credential remain provider-owned and never cross the
opaque port.

Release [v0.1.4](docs/audit/provider-release-v0.1.4-20261111.md) adds exact client SPIFFE authorization and renewable TLS
generations under [ADR-0001](docs/adr/0001-tls-identity-lifecycle.md). Local
real-TLS tests cover wrong identities, buffered unauthorized requests,
renewal, replacement CA and withdrawal; they do not call OpenAI or grant
deployment admission. Model, prompt and dependency locks are unchanged.

The exact signed image also passed one selected live regression request
with retained real material, and rejected anonymous and same-CA foreign peers.
This bounded transport evidence is separate from current-policy owner admission.

Release [v0.1.3](docs/audit/provider-release-v0.1.3-20261111.md) has verified
signatures, source provenance, both native architecture security profiles and
four reviewed real-material inference cases. Its bounded component evaluation
does not grant functional-owner policy-scope or deployment admission.

The initial lock selects `gpt-6.1-sol`, medium reasoning, `store=false` and a
strict JSON schema. The neutral [release.json](release.json) intentionally
contains no provider identity. It is not quality-admitted until a representative
bounded evaluation is reviewed.

Offline verification requires no API key:

```sh
poetry install
poetry run ruff check .
poetry run ruff format --check .
poetry run pyright
poetry run pytest -q
PYTHONPATH=src poetry run python -m aelev_advance_screening_provider verify-config
docker build --target test .
docker build --target runtime .
```

Copy `.env.local.example` to the ignored `.env.local` only when an operator is
ready to supply this provider's own key. A placeholder starts no billable API
request and is reported as a blocked local readiness condition.
