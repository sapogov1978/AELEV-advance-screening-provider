# Bounded provider evaluation — 2026-11-10

Exact image:
`ghcr.io/sapogov1978/aelev-advance-screening-provider@sha256:defd441f47c59631312678aafb27451bb5df3fd424f56ba69afdfd677409fc00`.
Artifact source: `e2845eed43ddee2eeabbaaf5a264f02ed912f7e4`.

The existing `v0.1.0` image passed native arm64 mTLS replay against real
Advance-owned queue material and its actual policy digest. The already
collected four-page site was accepted; two explicitly excluded/out-of-scope
queue items were rejected; withheld evidence returned REVIEW. A single
incompletely observed homepage returned conservative REVIEW instead of the
test author's initial REJECT. This discrepancy is preserved in the machine
report; it is not a provider acceptance or a silently corrected baseline.

All five observed responses returned HTTP 200. Codex reviewed the rationales
against the supplied material and policy. Every opaque response preserved the
request ID and exact release identity. Anonymous TLS failed and a mismatched
release was rejected with 422 before inference. Test containers were stopped
and removed without issuing any queue command.

Cosign 3.1.4 verified the image's keyless signature, certificate chain and
transparency-log claims for issuer `https://token.actions.githubusercontent.com`
and exact workflow identity
`https://github.com/sapogov1978/AELEV-advance-screening-provider/.github/workflows/release.yml@refs/tags/v0.1.0`.
SLSA provenance and SPDX SBOM are published for amd64 and arm64. Source audit
`42710904670` and image publication `42711199946` passed; the current source
also passed six tests, Ruff and Pyright locally.

[Hash-only evidence](provider-quality-20261110.json) binds the exact image,
corpus exchanges, real queue job IDs and preserved discrepancy. Raw requests
and responses remain outside Git at the paths in that report. No credentials,
model-specific upstream headers or runtime databases are included.

## Admission boundary

This closes the bounded provider evaluation gate. The image still declares
`NOT_ADMITTED`: only the functional owner may select and admit its exact digest
and policy scope. Permanent owner identities, representative workload quality,
recovery and the deployed owner-worker E2E are separate gates. Test-generated
mTLS identities are not production identities. No claim of full platform
production readiness is made by this report.
