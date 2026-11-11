# Advance provider v0.1.4: exact-image component verification

The signed release adds exact client SPIFFE authorization and renewable leaf/CA
contexts. Wrong clients cannot dispatch buffered HTTP bytes. Identity withdrawal
blocks new requests; the readiness marker expires after five seconds.

- Image: `ghcr.io/sapogov1978/aelev-advance-screening-provider@sha256:256632c1fdb32fb762a7b64718d37ab1f0520f378141894968f8ce7af0f09b1c`.
- Source: `fd8d04ed05f38ada07a4b2a0bf67fcbf18ff7e09`; successful main audit `42966519149`, release `42968871969`.
- Native manifests, signatures, source provenance and SBOM: AMD64 and ARM64.
- Linux suite: 49 passed; the one image-health skip was exercised separately and passed.
- Exact-image live requests: 1; each returned HTTP 200.

| Retained real-material case | Result |
| --- | --- |
| real-queued-site-current-policy | ACCEPT |

The semantic review checks supplied source content and per-document URL/digest
binding. Complete prior component coverage is recorded for [v0.1.3](provider-release-v0.1.3-20261111.md).
The inference/application, prompt, descriptor and dependency bytes are unchanged;
the [machine-readable report](provider-release-v0.1.4-20261111.json) retains the exact comparison hashes.
The raw request and response JSON content remains at `/private/var/tmp/aelev-production-admission.wDuzQd/advance-v014/advance-screening-quality.json`. These are frozen
component replays, not fresh working-queue or current-policy processing.

Both native security reports pass the reviewed restricted runtime profile. Each
raw scan still contains one CRITICAL and 35 HIGH package findings; the specific
conditions are assessed as not affected in this execution profile. This is not a
claim that the distribution packages are patched or suitable for arbitrary CLI
use. Any unreviewed HIGH/CRITICAL or changed reviewed source blocks admission.

Anonymous clients and a wrong exact identity from the same CA were rejected by
the released image. Rotation, CA replacement, stale delivery and withdrawal
were exercised with real TLS in Linux source tests. Native issuer operation and
permanent deployment identities remain separate gates. Established TLS sessions
are not reverified against a changed CA; see [ADR-0001](../adr/0001-tls-identity-lifecycle.md).

The first staging attempt failed before serving startup and made no inference.
The successful attempt's cleanup hit Docker's asynchronous auto-removal race;
its original receipt is retained, cleanup was independently reconciled, and no
paid POST was repeated. All 138 pre-existing containers retained their image,
start, restart count and mounts. No working runtime switch or RESUME occurred.

Functional-owner scope admission, permanent identities and grants, deployed
collection/workers and clean-checkout platform E2E remain required.
