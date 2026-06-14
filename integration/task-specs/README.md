# TaskSpecs

Date: 2026-06-15

This directory records active and completed sub-agent assignments for
`devframe-system`.

Every TaskSpec must preserve these boundaries:

- No runtime execution unless a fresh RuntimeAuthorization explicitly allows it.
- No final acceptance claims from executor, runtime, or test summaries.
- No mutation of historical evidence archives.
- Every sub-agent report must include a Reviewer Index.
