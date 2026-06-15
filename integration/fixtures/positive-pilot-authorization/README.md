# Positive Pilot Authorization Fixtures

Date: 2026-06-15

These fixtures exercise the parent positive-pilot authorization packet
validator:

```text
scripts/validate_positive_pilot_authorization_packet.py
```

They are synthetic. They are not RuntimeAuthorization records and do not permit
MiniApp, Zotero, WriteLab, browser/CDP, cloud, PDF, attachment, full-text, or
private paper runtime execution.

Hard boundaries:

- `packet_mode=synthetic_fixture`
- no secrets
- no real resource payload
- no final acceptance claim
- missing-env behavior remains `blocked_not_pass`

The fixture suite includes one valid synthetic packet plus negative canaries for
multi-track selection, wildcard commands, authorization mismatch, output outside
the approved evidence root, and final acceptance overclaim.
