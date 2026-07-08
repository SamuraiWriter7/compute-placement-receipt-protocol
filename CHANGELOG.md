# Changelog

All notable changes to the Compute Placement Receipt Protocol will be documented in this file.

The project follows an incremental protocol-development model.

## [0.2.0-candidate] - 2026-07-08

### Added

- Candidate Node Evaluation record.
- Candidate compute node set structure.
- Evaluation dimension registry.
- Eligibility status model.
- Failed constraint references.
- Conditional eligibility records.
- Per-dimension evaluation results.
- Observed value and unit fields.
- Policy and evidence bindings.
- Candidate decision status.
- Rejection reason codes.
- Selected candidate summary.
- Evaluation actor identification.
- Evaluation evidence references.


### Protocol Expansion

v0.2 extends the protocol from:

```text
Selected Node
    ↓
Placement Reason

to:

Candidate A ─┐
Candidate B ─┼→ Evaluation → Selection
Candidate C ─┘

The protocol can now record both:

why a node was selected,
and why alternative candidates were not selected.
Key Distinction

v0.2 separates:

Eligibility

from:

Selection

A compute node may satisfy mandatory workload constraints while still being rejected because another eligible candidate is preferred.

Algorithm Neutrality

The protocol does not prescribe a scheduling or optimization algorithm.

Candidate evaluations may originate from:

schedulers,
policy engines,
autonomous agents,
human operators,
or hybrid systems.

The protocol records evaluation outcomes and evidence without replacing the decision system.

Deferred

The following capabilities remain deferred:

explicit task-to-model binding,
model-to-accelerator compatibility routing,
compute-type selection trace,
route binding,
active workload migration,
rebalancing triggers,
unified lifecycle auditing.

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
