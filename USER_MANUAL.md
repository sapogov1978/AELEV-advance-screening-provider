# Operator manual

## Secret

Copy `.env.local.example` to `.env.local` and replace the placeholder locally.
Never paste the key into chat or commit the file. Runtime mounts that file
read-only at `/run/secrets/provider/credential.env`; it must contain exactly one
`OPENAI_API_KEY=...` assignment.

The key is exclusive to this provider. It must not be shared with the Deep
Screening or Translation providers.

## Runtime

The image listens on port `18485`. By default it requires server files
`server.crt`, `server.key` and `client-ca.crt` under
`/run/secrets/compute-provider`. `AELEV_PROVIDER_INSECURE_HTTP=1` is accepted
only for an explicit local test outside production.

`python -m aelev_advance_screening_provider verify-config` validates the lock,
prompt and release descriptor without reading a key or using the network.
`print-release-digest` prints the exact digest to place in the owner connection
configuration.

## Admission

A healthy process proves only local configuration. Run representative
site-relevance evals with the exact image/model/prompt, review failures and
record the approved scope in the functional owner's admission record.
The published descriptor is immutable; editing its `NOT_ADMITTED` field is
not an admission mechanism. The bounded v0.1.3 review is recorded in the
[exact-release report](docs/audit/provider-release-v0.1.3-20261111.md).
Changing the model, prompt or execution profile requires a new provider
release and evaluation. Rollback replaces only the provider image and release
digest; it never clears the Advance Screening queue or implies `RESUME`.
