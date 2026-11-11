# Changelog

## Unreleased

- Require exact client/server SPIFFE identities and fresh SPIRE delivery for
  production mTLS. Reload leaf and CA generations for new connections, block
  stale or withdrawn material and retain the existing model/dependency locks.
  Certificate inspection uses bounded in-memory OpenSSL handshakes, without
  network access, a new dependency or a private Python certificate parser.
- Verified signed v0.1.3 on both native architectures against the reviewed
  runtime profile, and reviewed four actual mTLS inference responses from the
  frozen real-queue corpus. Raw CVEs remain recorded; functional-owner scope,
  permanent identities and deployed worker admission remain separate.
- Added source/lock/gate-bound CVE applicability evidence for the restricted
  provider entrypoint. Raw findings remain visible; unknown HIGH/CRITICAL,
  changed reviewed code/dependencies and missing controls block admission.
- Release signing now requires the exact main source audit and a native amd64
  scan of the published digest followed by the scoped security gate. Runtime
  profile evidence is retained as a release-workflow artifact.
- Added an immutable-image runtime probe and CI receipt for both Python
  environments, absent build tools/SQLite, MiniZip and systemd-homed. It runs
  without network or credentials and does not claim complete CVE admission.
- Removed the unused distribution SQLite library from runtime after a dry-run
  proved it has no dependent package removals. The provider exposes no SQL;
  functional-owner storage, queues and application locks are unaffected.
- Release builds refresh the OS-update stage instead of reusing its cache;
  image builds assert build tools are absent from both Python environments.
- Isolated the runtime from the Poetry builder after exact-image scanning
  found vulnerable build-only tools in the published image. The Python/OS and
  application dependency locks are unchanged; global and virtualenv installers
  are removed from the runtime. Distribution vulnerability admission remains open.
- Recorded the exact v0.1.2 image's native mTLS replay of the frozen four-case
  real-queue corpus after the bounded-capacity correction. Source, signature,
  platform attestations and raw request/response hashes are bound in the report;
  image security scanning and functional-owner admission remain separate gates.
- Return bounded HTTP 503 `PROVIDER_BUSY` for overlapping inference rather than
  queueing behind the active upstream call. HTTP and timeout tests prove a busy
  request makes no second API call and failures release provider capacity.
- Recorded exact v0.1.1 signature, SBOM/provenance and native arm64 mTLS replay
  of four real-queue cases: ACCEPT, two REJECT and withheld-evidence REVIEW.
- Fixed false-positive Docker health: a placeholder credential could previously
  return HTTP 503 while its listening TCP port made the image healthy. The
  non-billable health CLI now checks serving-process inference readiness.
- CI runs the runtime image without a network or real key and requires Docker
  unhealthy together with HTTP 503 for the repository placeholder.
- Recorded exact v0.1.0 signature, native arm64 mTLS and real-queue evaluation
  evidence, including a preserved conservative REVIEW fixture discrepancy.
  Owner production admission remains a separate deployment gate.
- Recomputed prompt, execution and neutral release digests after canonical
  single-newline file normalization.
- Created an independent OpenAI Responses API provider for the opaque Advance
  Screening `SITE_RELEVANCE` contract.
- Added an immutable provider lock, digest-pinned prompt, neutral release
  descriptor, strict structured output and bounded failures.
- Added a separate ignored API-key placeholder, mutual-TLS server defaults,
  offline tests and a non-root multi-stage image.
