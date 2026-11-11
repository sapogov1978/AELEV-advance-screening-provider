# Operator manual

## Secret

Copy `.env.local.example` to `.env.local` and replace the placeholder locally.
Never paste the key into chat or commit the file. Runtime mounts that file
read-only at `/run/secrets/provider/credential.env`; it must contain exactly one
`OPENAI_API_KEY=...` assignment.

The key is exclusive to this provider. It must not be shared with the Deep
Screening or Translation providers.

## Runtime

The image listens on port `18485`. Its read-only TLS root is
`/run/secrets/compute-provider`. Supply `identity.json` with exactly:

```json
{
  "schema_version": 1,
  "environment": "production",
  "delivery": "spire-file-v1",
  "server_spiffe_id": "spiffe://identity.example/advance-screening/compute/installation",
  "client_spiffe_id": "spiffe://identity.example/advance-screening/control/installation"
}
```

Replace both exact identities with approved owner values. Mount only the
public file-delivery result of the corresponding SPIRE agent at the TLS root,
and the owner policy read-only as `identity.json` within that root. The agent
provides `current.json`, `generations/<generation>/tls.pem` (mode 0600) and
`bundle.pem`; no bootstrap, agent state or issuer key is mounted. Stale,
withdrawn, changed or unavailable delivery blocks new requests without reuse
of the previous generation.

An explicitly local/test policy may select `pem-files-v1` with `server.crt`,
`server.key` (mode 0600) and `client-ca.crt`; this layout assumes the same
approved authority for server and client. It is forbidden for production.
`AELEV_PROVIDER_INSECURE_HTTP=1` remains only an explicit local test override,
forbidden by the production image/admission profile.

Leaf/CA generations reload without restarting the provider. Changing policy
or expected identities requires a controlled deployment and renewed owner
admission. The healthcheck requires a live readiness observer, initialized
inference and current identity. See the complete
[identity lifecycle contract](docs/adr/0001-tls-identity-lifecycle.md).

`python -m aelev_advance_screening_provider verify-config` validates the lock,
prompt and release descriptor without reading a key or using the network.
`print-release-digest` prints the exact digest to place in the owner connection
configuration.

## Admission

A healthy process proves only local configuration. Run representative
site-relevance evals with the exact image/model/prompt, review failures and
record the approved scope in the functional owner's admission record.
The published descriptor is immutable; editing its `NOT_ADMITTED` field is
not an admission mechanism. The bounded v0.1.4 transport review and its
unchanged-inference comparison to the four-case v0.1.3 baseline are recorded
in the [exact-release report](docs/audit/provider-release-v0.1.4-20261111.md).
Changing the model, prompt or execution profile requires a new provider
release and evaluation. Rollback replaces only the provider image and release
digest; it never clears the Advance Screening queue or implies `RESUME`.
