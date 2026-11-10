# Advance provider v0.1.2 — bounded release evaluation

Image: `ghcr.io/sapogov1978/aelev-advance-screening-provider@sha256:ebaa9668b2534c12790e337749ff2ae756f2f858b9d2e4b387ef1cf999871cd9`.
Source: `64933d1587837baf7905c2c1613ab2fb353ad660`.

The exact native arm64 image passed the same four mTLS cases used for v0.1.1,
with the frozen corpus SHA-256 recorded in the [machine report](provider-release-v0.1.2-20261110.json).
The collected four-page site returned ACCEPT, the church-service and domain-sale
items returned REJECT, and withholding documents returned REVIEW. Codex reviewed
all four rationales against the supplied real material and retained policy.
This component replay does not execute the functional owner's queue.

The capacity correction rejects an overlapping request with HTTP 503
`PROVIDER_BUSY`, without another upstream call or provider-side waiting queue.
Source audit `42906378878` passed unit tests, strict typing, lint, image builds
and the networkless placeholder-health regression. Release `42907481776`
published amd64 and arm64 with SBOM and provenance. Cosign verified the exact
v0.1.2 tag workflow identity; both platform attestations match the source above.

Anonymous TLS and the wrong release digest were rejected. Test containers were
removed and no RESUME was issued. Raw requests and responses remain outside Git
at the path in the machine report; their hashes cover complete opaque envelopes.
The earlier incomplete-homepage discrepancy remains in the
[initial evaluation](provider-quality-20261110.md).

Production admission is blocked: Trivy 0.76.1 with its November 10 database
reported 2 CRITICAL and 49 HIGH findings. The subsequent runtime correction
removes build-only tools and requires new exact-image verification. A GitHub
release page has not been published for v0.1.2. Functional-owner policy-scope
admission, permanent identities and deployed owner-worker E2E remain open.
The neutral descriptor continues to declare NOT_ADMITTED.
