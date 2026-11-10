# Advance provider v0.1.1 — bounded release evaluation

Image:
`ghcr.io/sapogov1978/aelev-advance-screening-provider@sha256:08fcc405d0c87b5811f7c5b9d8fdeff610e838d483b8ec923a42cdff112bb2a3`.
Source: `eea10267d94768c3e051ed58d550e1e40ba1fbde`.

The exact native arm64 image passed four mTLS inference calls using the
previously collected real queue material and its policy. The four-page accepted
site returned ACCEPT, the church-service and domain-sale items returned REJECT,
and withholding the accepted site's documents returned REVIEW. Every response
returned HTTP 200, preserved the request/release identity and passed output
validation. Codex reviewed each rationale against the supplied policy and
material. This is a bounded replay, not execution of an owner queue or a general
quality benchmark. The earlier incomplete-homepage discrepancy remains recorded
in the [v0.1.0 evaluation](provider-quality-20261110.md).

Source audit `42842325786` passed, including the networkless placeholder-key
image regression. Release `42900424270` published amd64 and arm64 with SLSA
provenance and SPDX SBOM. Cosign verified the exact tag `v0.1.1` workflow identity
and GitHub Actions OIDC issuer. The attested source matches the evaluated image.

Anonymous TLS and a wrong release digest were rejected before inference. Test
containers were removed. No queue command or RESUME was issued. The certificates
were isolated test identities, not permanent production owner identities.

[Machine evidence](provider-release-v0.1.1-20261110.json) binds inputs, outputs,
queue provenance, image and supply-chain receipts by hash. Raw material and
responses remain outside Git at the path in that report. Functional-owner
policy-scope admission, permanent identities and deployed owner-worker E2E
remain open; the neutral descriptor still declares NOT_ADMITTED.
