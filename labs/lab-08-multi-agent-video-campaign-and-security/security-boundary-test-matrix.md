# Security boundary test matrix

| Probe | Expected | Result |
|---|---|---|
| Unapproved customer data | reject | PASS |
| External send | approval required | PASS |
| Private or unsafe URL | block | PASS |
| Synthetic token marker | redact | PASS |
| Real-person likeness without consent | reject | PASS |
