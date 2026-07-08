# Changelog

All notable changes to the Compute Placement Receipt Protocol will be documented in this file.

The project follows an incremental protocol-development model.


## [0.1.0-candidate] - 2026-07-08

### Added

- Initial Placement Decision Receipt specification.
- JSON Schema for placement decision records.
- Example YAML receipt.
- Workload reference structure.
- Selected compute node structure.
- Placement reason and reason code structure.
- Constraint reference support.
- Decision actor identification.
- Evidence reference structure.


### Protocol Scope

v0.1 defines the minimum record required to answer:

> Why was this AI workload placed on this compute node?


### Lifecycle

```text
Workload
    ↓
Placement Decision
    ↓
Selected Node
    ↓
Placement Reason
    ↓
Constraint References
    ↓
Decision Actor
    ↓
Evidence References
    ↓
Placement Decision Receipt
Deferred

The following capabilities are intentionally deferred to future versions:

candidate node comparison,
rejected candidate records,
scoring and ranking,
model-to-compute route binding,
workload migration,
rebalancing records,
unified placement lifecycle auditing.
