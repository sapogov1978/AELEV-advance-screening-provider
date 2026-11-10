# AELEV Advance Screening Provider specification

## Responsibility

The provider owns the remote API choice, model lock, prompt, credential,
structured-output schema, response validation and image healthcheck. Advance
Screening owns collection, policy, queueing, retries, decisions, evidence,
admission, UI, storage and Kafka publication.

## Opaque port

`GET /v1/status` and `POST /v1/infer` implement schema version 1 for owner
`advance-screening`, task `SITE_RELEVANCE`, capability `INFERENCE` and the exact
SHA-256 digest of [release.json](release.json). Requests and responses use the
envelope in [contracts/opaque-compute-v1.json](contracts/opaque-compute-v1.json).
No provider, model, prompt, upstream body or credential is disclosed.

Inference output contains `outcome` (`ACCEPT`, `REJECT` or `REVIEW`), a bounded
`model_response`, at least one `reason_code`, and nullable uncalibrated
`confidence`. Advance Screening remains the only component allowed to apply
that result.

## OpenAI execution

[provider.lock.json](provider.lock.json) pins the Responses endpoint, model,
reasoning effort, output budget, `store=false`, exact prompt digest and direct
HTTPS transport. Each call is a stateless, buffered request with no tools,
streaming, background mode or stored-response chaining. Input material is data,
not instructions. Only one strict structured-output object is accepted.

`store=false` requests stateless API behavior; it is not a claim that the
OpenAI project has Zero Data Retention or a particular data residency setting.
Those account-level properties remain admission gates.

## Readiness and release

Security admission uses the [reviewed runtime profile](security/runtime-profile.json)
and [CVE-specific evidence](docs/audit/runtime-security-20261111.md). It is scoped
to the default opaque entrypoint under non-root, read-only, no-capabilities and
no-new-privileges conditions. The owner verifies those conditions at deployment.
Any changed reviewed source/dependency or unreviewed HIGH/CRITICAL blocks the
gate. Release signing requires the exact successful main audit and a scan of
the actual published native digest; raw findings and decisions are retained.

The runtime uses the same Python 3.13.7 Debian Bookworm base as the builder,
but copies only the locked application environment. Poetry, its build-only
dependencies, pip and setuptools are excluded from runtime. Build and test
stages continue to use pinned Poetry 2.2.1.
The unused distribution SQLite library is excluded from runtime. The opaque
provider has no SQL interface or durable database; owner storage is independent.

One upstream inference is active at a time. An overlapping inference returns
HTTP 503 `PROVIDER_BUSY` immediately without a second API call or an internal
waiting queue. The functional owner retains retry responsibility. Timeouts and
transport failures release the capacity for subsequent requests.

Local readiness validates immutable configuration and a non-placeholder secret
without performing a billable upstream probe. Docker healthcheck requires the
serving process's initialized inference state, a live process and the bound
local port; a listening port with blocked configuration is unhealthy. Its
readiness marker is cleared at startup and shutdown, and the health CLI never
initializes inference or reads a key. Provider quota, model access and
semantic quality require a bounded live evaluation. Production use additionally
requires an immutable signed image digest, SBOM, provenance, mTLS identities and
an explicit Advance Screening quality-admission decision.
