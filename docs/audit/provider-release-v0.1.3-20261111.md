# Advance provider v0.1.3 — exact-release component verification

Image: `ghcr.io/sapogov1978/aelev-advance-screening-provider@sha256:292529de6c9f8346e84a2dabeff81df9cff75920f40191bb51267043ae27cb93`.
Source: `1eda5a7431e0c3fa38fd2506852460e2fc32f24f`.

The exact native arm64 image passed 4 bounded live API cases. Codex
separately reviewed every actual output against the supplied material and
expected meaning. Frozen retained real queue material and policy, replayed through isolated mTLS; four site-relevance cases. Not deployed owner collection, queue processing, or cascade E2E.

The [machine report](provider-release-v0.1.3-20261111.json) binds the frozen corpus, complete opaque
request/response hashes, native image, security scans and supply-chain receipts.
Raw exchanges remain outside Git at `/var/tmp/aelev-production-admission.wDuzQd/advance-v013/advance-screening-quality.json`.

Cosign verified the exact tag workflow identity and GitHub OIDC issuer. Both
amd64 and arm64 have SPDX SBOMs and SLSA provenance matching the source above.
Source audit [42924968681](https://github.com/sapogov1978/AELEV-advance-screening-provider/actions/runs/42924968681)
and release [42925398607](https://github.com/sapogov1978/AELEV-advance-screening-provider/actions/runs/42925398607) passed.

Both native architectures passed the [scoped security review](runtime-security-20261111.md).
Each raw scan retains **1 CRITICAL and 35 HIGH** package findings. Individual
applicability decisions admit only the reviewed default opaque entrypoint with
UID 10001, read-only root, no effective capabilities, no-new-privileges and an
empty fstab. This is not a claim that those OS packages are patched. The owner
must verify the same profile at deployment; an unknown HIGH/CRITICAL blocks.

The real four-page queue site returned ACCEPT, the retained church-service and
domain-sale pages returned REJECT, and withholding all documents returned
REVIEW. Their policy is the retained real policy captured with the corpus;
this run does not assert that it is still the platform's active policy.
Anonymous TLS and a wrong release digest were rejected before inference.
Temporary containers were removed and no queue command or RESUME was issued.

Functional-owner policy-scope admission, permanent identities and deployed
owner-worker E2E remain open. The immutable descriptor still says NOT_ADMITTED;
provider evaluation does not grant the owner permission to apply results.
