# Changelog

All notable changes to the **Compute Placement Receipt Protocol** are documented in this file.

The project follows an incremental protocol-development model.

---

## [0.5.0-candidate] - 2026-07-08

### Added

* Unified Compute Placement Lifecycle schema.
* Lifecycle identifier.
* Parent lifecycle reference support.
* Workload reference envelope.
* Origin trace reference support.
* Agent handoff reference support.
* Execution reference support.
* Artifact reference support.
* Lifecycle status registry.
* Phase record envelope.
* Route binding phase reference.
* Candidate evaluation phase reference.
* Initial placement phase reference.
* Execution phase reference.
* Runtime observation phase reference.
* Multiple migration receipt references.
* Completion phase reference.
* Placement audit phase reference.
* Lifecycle transition chain.
* Transition identifiers.
* Transition type classification.
* Trigger references.
* Decision references.
* Receipt references.
* Transition timestamps.
* Chain integrity status.
* Reference resolution status.
* Evidence sufficiency status.
* Missing reference tracking.
* Integrity warnings.
* Verification references.
* Lifecycle outcome classification.
* Final placement record.
* Completion reason classification.
* Artifact outcome reference.
* Placement explainability status.
* Migration explainability status.
* Policy traceability status.
* Audit readiness summary.
* Lifecycle creation timestamp.
* Lifecycle update timestamp.
* Lifecycle closure timestamp.
* Unified lifecycle evidence references.

### Protocol Expansion

v0.5 closes the first development arc.

The protocol now supports:

```text
Task
  ↓
Model Selection
  ↓
Compute Requirement
  ↓
Candidate Evaluation
  ↓
Placement Decision
  ↓
Execution
  ↓
Runtime Observation
  ↓
Rebalancing and Migration
  ↓
Completion
  ↓
Placement Audit
```

### Integration Model

v0.5 introduces reference-based lifecycle integration.

The unified lifecycle does not duplicate all lower-level records.

Instead, it connects:

* Model-to-Compute Route Binding records,
* Candidate Node Evaluation records,
* Placement Decision Receipts,
* execution records,
* runtime observation records,
* Rebalancing and Migration Receipts,
* completion records,
* placement audit records.

This preserves modularity while enabling end-to-end lifecycle traceability.

### Phase and Transition Model

v0.5 separates lifecycle states from lifecycle movement.

```text
Phase Record
=
What existed during a lifecycle stage

Transition Record
=
How and why the lifecycle moved to another stage
```

This enables explicit recording of adaptive, policy-triggered, failure-triggered, manual, emergency, completion, and closure transitions.

### Integrity Layer

The lifecycle can now report:

* chain completeness,
* reference resolution,
* evidence sufficiency,
* missing references,
* integrity warnings,
* verification references.

Operational success and audit readiness are treated as separate states.

### Outcome Layer

The protocol can distinguish:

* successful completion,
* successful completion with migration,
* successful completion with warning,
* partial success,
* failure,
* cancellation.

Migration is not treated as failure by default.

An adaptive migration may be part of a successful compute lifecycle.

### Audit Readiness

The lifecycle audit summary can independently evaluate:

* placement explainability,
* migration explainability,
* policy traceability,
* overall audit readiness.

### First Arc Completion

The completed first arc is:

```text
v0.1 — Placement Decision Receipt
       ↓
v0.2 — Candidate Node Evaluation
       ↓
v0.3 — Model-to-Compute Route Binding
       ↓
v0.4 — Rebalancing and Migration Receipt
       ↓
v0.5 — Unified Compute Placement Lifecycle
```

### Development Status

The first candidate arc of the Compute Placement Receipt Protocol is structurally complete.

Potential future extensions include:

* distributed compute discovery,
* cross-provider placement evidence,
* compute identity and resource attestations,
* energy and carbon attestations,
* reservation and placement permit records,
* placement dispute and appeal records,
* allocation and settlement bridges,
* cryptographic receipt chaining.

---

## [0.4.0-candidate] - 2026-07-08

### Added

* Rebalancing and Migration Receipt schema.
* Previous placement reference.
* Previous migration chain reference.
* Route binding reference.
* Previous placement receipt reference.
* Candidate re-evaluation reference.
* Workload execution reference.
* Previous placement structure.
* Placement start timestamp.
* Runtime trigger structure.
* Trigger type registry.
* Trigger reason codes.
* Trigger severity.
* Trigger detection timestamp.
* State change records.
* Before-and-after state values.
* Measurement unit support.
* Threshold references.
* Evidence references for state changes.
* Re-evaluation structure.
* Re-evaluation requirement flag.
* Re-evaluation status.
* Candidate evaluation reference.
* Re-evaluation policy references.
* Migration decision structure.
* Migration decision classification.
* Decision mode classification.
* Migration reason codes.
* Destination placement structure.
* Destination placement receipt reference.
* Destination selection summary.
* Migration execution structure.
* Migration strategy registry.
* Migration execution status.
* State preservation status.
* Migration start timestamp.
* Migration completion timestamp.
* Execution reference.
* Rollback reference.
* Decision actor identification.
* Migration evidence references.

### Protocol Expansion

v0.4 extends the protocol from static placement reasoning:

```text
Task
  ↓
Model
  ↓
Compute Requirement
  ↓
Candidate Evaluation
  ↓
Placement
```

to dynamic placement transitions:

```text
Placement
    ↓
Runtime State Change
    ↓
Trigger
    ↓
Re-evaluation
    ↓
Transition Decision
    ↓
Destination Placement
    ↓
Migration Result
```

### Trigger and Decision Separation

v0.4 separates observed infrastructure or workload changes from the final transition decision.

A trigger can result in:

* migration,
* rebalancing,
* replication,
* scale-out,
* scale-in,
* remaining in place,
* termination.

This allows the protocol to preserve both action and deliberate non-action.

### Source and Destination Reasoning

Migration records distinguish:

```text
Why leave the source?
```

from:

```text
Why select the destination?
```

This separation improves traceability across adaptive placement decisions.

### Migration Execution

v0.4 supports migration execution strategies including:

* cold migration,
* warm migration,
* live migration,
* checkpoint restore,
* replica handoff,
* traffic shift,
* restart at destination.

### State Preservation

Migration receipts can record whether workload state was:

* fully preserved,
* partially preserved,
* not preserved,
* not applicable,
* unknown.

### Compute Trajectory

The protocol now supports a placement trajectory:

```text
Node A
  ↓
State Change
  ↓
Decision
  ↓
Node B
  ↓
State Change
  ↓
Decision
  ↓
Node C
```

### Deferred

The following capabilities were deferred to v0.5:

* unified lifecycle identifiers,
* lifecycle status,
* phase references,
* transition chains,
* cross-record integrity,
* completion records,
* lifecycle outcomes,
* placement audit summaries,
* end-to-end placement accountability.

---

## [0.3.0-candidate] - 2026-07-08

### Added

* Model-to-Compute Route Binding schema.
* Task reference structure.
* Workload reference support.
* Task type registry.
* Task priority field.
* Latency class field.
* Model selection structure.
* Model identifier.
* Model class registry.
* Model provider field.
* Model version field.
* Model selection reason codes.
* Model selection summary.
* Compute requirement structure.
* Accelerator requirement flag.
* Accelerator class registry.
* Minimum memory requirement.
* Preferred memory requirement.
* Memory type classification.
* Execution mode structure.
* Minimum node count.
* Preferred node count.
* Maximum latency requirement.
* Data residency requirements.
* Security class.
* Energy policy reference.
* Compute route structure.
* Selected compute type.
* Execution scope.
* Candidate evaluation reference.
* Placement receipt reference.
* Route policy references.
* Binding reason structure.
* Primary binding reason.
* Binding reason codes.
* Binding summary.
* Binding timestamp.
* Binding actor identification.
* Route binding evidence references.

### Protocol Expansion

v0.3 extends the protocol from:

```text
Candidate Nodes
      ↓
Evaluation
      ↓
Placement
```

to:

```text
Task
  ↓
Model Selection
  ↓
Compute Requirement
  ↓
Compute Route
  ↓
Candidate Evaluation
  ↓
Placement Decision
```

### Key Separation

v0.3 distinguishes three questions:

```text
Why this model?
```

```text
Why this compute type?
```

```text
Why this node?
```

These decisions can now be recorded as separate but connected layers.

### Compute Requirement Layer

A new intermediate layer connects model execution requirements to infrastructure evaluation.

It can record:

* accelerator requirements,
* device memory requirements,
* execution mode,
* node count,
* latency limits,
* data residency,
* security class,
* energy policy.

### Route Binding Model

The first three protocol layers now form:

```text
Model-to-Compute Route Binding
              ↓
Candidate Node Evaluation
              ↓
Placement Decision Receipt
```

Together, they can answer:

```text
What task?
    ↓
Why this model?
    ↓
What compute was required?
    ↓
Which nodes were considered?
    ↓
Why was the final node selected?
```

### Design Boundary

The protocol remains decision-system neutral.

It does not define:

* model selection algorithms,
* model routing algorithms,
* scheduler optimization methods,
* node discovery mechanisms,
* infrastructure control planes.

It records the resulting route binding and placement decision context.

### Deferred

The following capabilities were deferred to v0.4:

* runtime state transitions,
* congestion-triggered relocation,
* failure-driven migration,
* energy-triggered rebalancing,
* policy-triggered route changes,
* source-to-destination migration evidence,
* state preservation records,
* migration execution status.

---

## [0.2.0-candidate] - 2026-07-08

### Added

* Candidate Node Evaluation schema.
* Candidate compute node set.
* Evaluation dimension registry.
* Candidate node identity structure.
* Node type classification.
* Provider field.
* Region field.
* Eligibility status model.
* Failed constraint references.
* Conditional eligibility records.
* Per-dimension evaluation results.
* Observed value support.
* Measurement unit support.
* Policy references.
* Evidence references.
* Candidate decision status.
* Candidate selection status.
* Candidate rejection status.
* Reserve candidate status.
* Rejection reason codes.
* Candidate decision summaries.
* Selected candidate record.
* Selection summary.
* Evaluation timestamp.
* Evaluation actor identification.
* Evaluation evidence references.

### Protocol Expansion

v0.2 extends the protocol from:

```text
Selected Node
    ↓
Placement Reason
```

to:

```text
Candidate A ─┐
Candidate B ─┼→ Evaluation → Selection
Candidate C ─┘
```

The protocol can now record both:

* why a node was selected,
* why alternative candidates were not selected.

### Eligibility and Selection Separation

v0.2 separates:

```text
Eligibility
```

from:

```text
Selection
```

A compute node may satisfy mandatory workload constraints while still being rejected because another eligible candidate is preferred.

This allows the protocol to distinguish:

* impossible placement,
* possible but non-preferred placement,
* reserve placement,
* selected placement.

### Rejected Candidates as Evidence

v0.2 treats rejection records as first-class placement evidence.

The protocol can now answer:

```text
Why Fukuoka?
Why not Tokyo?
Why not Osaka?
```

rather than recording only the final result.

### Algorithm Neutrality

The protocol does not prescribe a scheduling or optimization algorithm.

Candidate evaluations may originate from:

* weighted scoring,
* rule-based schedulers,
* constraint satisfaction,
* optimization engines,
* policy engines,
* autonomous agents,
* human operators,
* hybrid systems.

### Deferred

The following capabilities were deferred to v0.3:

* explicit task-to-model binding,
* model selection reasons,
* compute requirements,
* accelerator requirements,
* memory requirements,
* execution mode,
* compute type selection,
* execution scope,
* route policy references.

---

## [0.1.0-candidate] - 2026-07-08

### Added

* Initial Placement Decision Receipt schema.
* JSON Schema for placement decision records.
* YAML example receipt.
* Protocol identifier.
* Schema version field.
* Placement receipt identifier.
* Workload reference structure.
* Task reference support.
* Model reference support.
* Selected compute node structure.
* Node type registry.
* Provider field.
* Region field.
* Placement reason structure.
* Primary placement reason.
* Placement reason codes.
* Placement summary.
* Constraint reference support.
* Decision timestamp.
* Decision actor structure.
* Decision actor type registry.
* Decision actor identifier.
* Evidence reference structure.
* Evidence type registry.
* Evidence digest support.

### Protocol Scope

v0.1 defines the minimum record required to answer:

> Why was this AI workload placed on this compute node?

The lifecycle is:

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
```

### Design Boundary

v0.1 intentionally does not define:

* candidate node comparison,
* candidate rankings,
* rejected alternatives,
* model routing,
* compute requirement binding,
* migration history,
* rebalancing triggers,
* execution control,
* scheduling algorithms.

The protocol begins with one minimal accountability unit:

```text
Selected Node
+
Reason
+
Constraints
+
Decision Actor
+
Evidence
```

### Initial Principle

The protocol establishes its central design principle:

> Record not only where computation happened, but why it happened there.

---

## First Arc Summary

The first candidate arc developed through five stages:

```text
v0.1
Placement Decision Receipt
        ↓
Record the selected node and placement reason

v0.2
Candidate Node Evaluation
        ↓
Record candidate comparison and rejection reasons

v0.3
Model-to-Compute Route Binding
        ↓
Connect task, model, compute requirement, and placement

v0.4
Rebalancing and Migration Receipt
        ↓
Record runtime state transitions and migration reasoning

v0.5
Unified Compute Placement Lifecycle
        ↓
Connect the complete lifecycle into an auditable chain
```

The resulting protocol chain is:

```text
Intent
  ↓
Task
  ↓
Model
  ↓
Compute Requirement
  ↓
Candidate Evaluation
  ↓
Placement
  ↓
Execution
  ↓
Observation
  ↓
Rebalancing
  ↓
Migration
  ↓
Completion
  ↓
Audit
```

The first arc is structurally complete through `v0.5.0-candidate`.
