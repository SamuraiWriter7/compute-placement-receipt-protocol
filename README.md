# Compute Placement Receipt Protocol

An open protocol for recording why AI workloads are placed, routed, migrated, and executed across distributed compute resources.

---

## Overview

AI workloads are increasingly executed across heterogeneous and distributed compute environments.

A workload may run on:

* an edge device,
* an NPU,
* a local accelerator,
* an edge cluster,
* a regional datacenter,
* a cloud region,
* a GPU cluster,
* or a distributed compute fabric.

Existing orchestration systems can discover resources, schedule workloads, and move execution between nodes.

However, the reasoning behind those decisions is often fragmented across:

* scheduler logs,
* policy engines,
* telemetry systems,
* infrastructure control planes,
* energy management systems,
* network records,
* human operations,
* and provider-specific audit logs.

The **Compute Placement Receipt Protocol** defines a machine-readable accountability layer for recording:

* what workload required placement,
* which model and compute route were selected,
* which candidate nodes were evaluated,
* why one node was selected,
* why alternatives were rejected,
* what runtime changes triggered re-evaluation,
* why a workload was migrated or retained,
* and whether the complete placement lifecycle can be explained and audited.

The protocol does not define a scheduler.

It records the decisions made by schedulers, agents, orchestrators, policy engines, humans, and hybrid systems.

---

## Core Question

The protocol begins with one question:

> Why was this computation executed here?

As the lifecycle develops, that question expands into:

```text
What task was created?
        ↓
Why was this model selected?
        ↓
What compute characteristics were required?
        ↓
Which nodes were considered?
        ↓
Why was one node selected?
        ↓
What changed during execution?
        ↓
Why was the workload moved or retained?
        ↓
Can the complete lifecycle be explained?
```

---

## Design Philosophy

### 1. Record Decisions, Do Not Replace Schedulers

The protocol does not determine where workloads should run.

It records placement decisions made by:

* schedulers,
* model routers,
* AI agents,
* orchestrators,
* policy engines,
* human operators,
* or hybrid decision systems.

The protocol is an accountability layer, not a control plane.

---

### 2. Record Reason, Not Only Result

A node identifier alone is insufficient.

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

A placement receipt should preserve enough context to explain why a particular decision occurred.

---

### 3. Separate Decision Layers

The protocol distinguishes several different questions:

```text
Why this model?
        ↓
Model Selection

Why this compute type?
        ↓
Compute Requirement and Route Binding

Why this node?
        ↓
Candidate Evaluation and Placement Decision

Why move?
        ↓
Rebalancing and Migration Decision
```

These decisions may be made by different actors and supported by different evidence.

---

### 4. Integration Without Collapse

The protocol uses modular records.

It does not merge every decision into one monolithic document.

```text
Unified Lifecycle
       │
       ├── Route Binding Record
       ├── Candidate Evaluation Record
       ├── Placement Decision Receipt
       ├── Migration Receipt(s)
       ├── Completion Record
       └── Placement Audit Record
```

Each record remains independently usable and independently verifiable.

---

### 5. Infrastructure Neutrality

The protocol is designed to remain independent of:

* cloud providers,
* accelerator vendors,
* GPU vendors,
* AI model providers,
* orchestration engines,
* networking technologies,
* datacenter architectures,
* and scheduling algorithms.

---

## Protocol Architecture

The first protocol arc consists of five layers:

```text
v0.1
Placement Decision Receipt
        ↓
Where was the workload placed, and why?

v0.2
Candidate Node Evaluation
        ↓
Which alternatives were evaluated, selected, or rejected?

v0.3
Model-to-Compute Route Binding
        ↓
Why was the task bound to this model and compute class?

v0.4
Rebalancing and Migration Receipt
        ↓
Why did the workload move, rebalance, remain, replicate, or scale?

v0.5
Unified Compute Placement Lifecycle
        ↓
Can the complete placement history be traced and audited?
```

The combined lifecycle is:

```text
Workload Intent
      ↓
Task Formation
      ↓
Model Selection
      ↓
Compute Requirement
      ↓
Compute Route Binding
      ↓
Candidate Discovery
      ↓
Candidate Evaluation
      ↓
Initial Placement
      ↓
Execution
      ↓
Runtime Observation
      ↓
Re-evaluation
      ↓
Rebalancing / Migration
      ↓
Completion
      ↓
Placement Audit
      ↓
Lifecycle Closure
```

---

## Repository Structure

```text
compute-placement-receipt-protocol/
├── .github/
│   └── workflows/
│       └── validate.yml
├── schemas/
│   ├── placement-decision-receipt.schema.json
│   ├── candidate-node-evaluation.schema.json
│   ├── model-compute-route-binding.schema.json
│   ├── rebalancing-migration-receipt.schema.json
│   └── unified-compute-placement-lifecycle.schema.json
├── examples/
│   ├── placement-decision-receipt.example.yaml
│   ├── candidate-node-evaluation.example.yaml
│   ├── model-compute-route-binding.example.yaml
│   ├── rebalancing-migration-receipt.example.yaml
│   └── unified-compute-placement-lifecycle.example.yaml
├── scripts/
│   └── validate_examples.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── LICENSE
```

---

# v0.1 — Placement Decision Receipt

Version 0.1 defines the minimum placement decision record.

Its purpose is to answer:

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

A receipt can record:

* workload identity,
* task reference,
* model reference,
* selected compute node,
* node type,
* provider,
* region,
* primary placement reason,
* reason codes,
* policy and constraint references,
* decision timestamp,
* decision actor,
* supporting evidence references.

### Example Concept

```text
Workload:
research-task-042

Selected Node:
fukuoka-gpu-003

Primary Reason:
energy

Supporting Reasons:
- sufficient GPU memory
- latency within policy
- lower capacity pressure
- lower energy cost
- lower carbon intensity
```

v0.1 establishes the fundamental distinction between:

```text
Where was it placed?
```

and:

```text
Why was it placed there?
```

---

# v0.2 — Candidate Node Evaluation

Version 0.2 expands the protocol from a single placement result to the evaluation context behind that result.

The lifecycle is:

```text
Workload
    ↓
Candidate Discovery
    ↓
Candidate Node Set
    ↓
Evaluation Dimensions
    ↓
Eligibility Check
    ↓
Candidate Comparison
    ↓
Selection / Rejection
    ↓
Candidate Node Evaluation Record
    ↓
Placement Decision Receipt
```

The evaluation record can preserve:

* candidate node identity,
* node type,
* provider,
* region,
* eligibility status,
* failed constraints,
* conditional requirements,
* evaluation dimensions,
* observed values,
* measurement units,
* policy references,
* supporting evidence,
* selection status,
* rejection reasons,
* final selection summary.

---

## Eligibility and Selection Are Different

A candidate may be technically eligible without being selected.

```text
Eligible
   ↓
Meets mandatory constraints

Selected
   ↓
Chosen among eligible candidates
```

For example:

```text
Tokyo GPU
├── eligible
├── low latency
└── rejected: capacity pressure

Osaka GPU
├── eligible
└── rejected: unfavorable energy cost

Fukuoka GPU
├── eligible
├── acceptable latency
├── sufficient memory
├── lower capacity pressure
└── selected
```

This distinction allows the protocol to record whether a node:

* could not execute the workload,
* could execute the workload but was not preferred,
* was retained as a reserve candidate,
* or was selected.

---

## Rejected Candidates Are Evidence

The protocol treats rejected alternatives as first-class placement evidence.

A useful placement history should answer both:

> Why was this node selected?

and:

> Why were the alternatives not selected?

This transforms the protocol from a placement-result log into a record of the placement decision space.

---

## Algorithm Neutrality

The protocol does not require a universal scoring method.

Candidate evaluation may come from:

* weighted scoring,
* rule-based scheduling,
* constraint satisfaction,
* optimization systems,
* policy engines,
* autonomous agent reasoning,
* human review,
* or hybrid systems.

The protocol records evaluation context without prescribing the algorithm.

---

# v0.3 — Model-to-Compute Route Binding

Version 0.3 extends the protocol upstream from node placement to task, model, and compute route selection.

The route is:

```text
Task
  ↓
Model Selection
  ↓
Compute Requirement
  ↓
Compute Type
  ↓
Candidate Node Evaluation
  ↓
Placement Decision
```

The core question is:

> Why was this task bound to this model and this class of compute resource?

The record can preserve:

* task identity,
* workload identity,
* task class,
* task priority,
* latency class,
* selected model,
* model class,
* model provider,
* model version,
* model selection reasons,
* accelerator requirements,
* accelerator class,
* minimum memory requirements,
* preferred memory requirements,
* execution mode,
* node count requirements,
* latency constraints,
* data residency requirements,
* security class,
* energy policy,
* selected compute type,
* execution scope,
* route policies,
* candidate evaluation references,
* placement receipt references,
* binding actor,
* supporting evidence.

---

## Compute Requirement as an Intermediate Layer

The protocol does not use a simplistic chain such as:

```text
Model
↓
Node
```

Instead, it preserves:

```text
Model Selection
        ↓
Compute Requirement
        ↓
Candidate Evaluation
        ↓
Placement Decision
```

The intermediate Compute Requirement layer may describe:

* accelerator requirements,
* device memory requirements,
* execution mode,
* latency limits,
* distributed execution requirements,
* node count,
* residency rules,
* security constraints,
* energy policies.

This allows infrastructure evaluation to remain explainable.

---

## Lightweight and Large-Scale Routes

A lightweight route may look like:

```text
Simple Classification
        ↓
Small Language Model
        ↓
Low Memory Requirement
        ↓
NPU
        ↓
Device
```

A complex workload may follow:

```text
Complex Research
        ↓
Large Reasoning Model
        ↓
High Memory Requirement
        ↓
GPU
        ↓
Regional GPU Cluster
```

The protocol does not treat either route as universally superior.

It records why a route was appropriate for a particular workload.

The relevant relationship is:

```text
Task Fit
+
Model Fit
+
Compute Fit
+
Placement Fit
```

---

# v0.4 — Rebalancing and Migration Receipt

Version 0.4 adds time and state change to the placement lifecycle.

The core question is:

> Why was an active workload moved, rebalanced, retained, replicated, scaled, or terminated?

The lifecycle is:

```text
Current Placement
        ↓
Runtime State Change
        ↓
Rebalancing Trigger
        ↓
Re-evaluation
        ↓
Transition Decision
        ↓
Destination Placement
        ↓
Migration Execution
        ↓
Migration Receipt
```

Possible trigger categories include:

```text
Capacity
├── capacity pressure
├── queue growth
└── accelerator exhaustion

Network
├── latency degradation
├── packet loss
└── route failure

Energy
├── energy price change
├── power budget reduction
└── renewable availability change

Reliability
├── node failure
├── predicted failure
└── maintenance event

Policy
├── residency policy change
├── security policy change
└── compliance change

Workload
├── priority change
├── scale change
└── model change
```

---

## Trigger Is Not Decision

The protocol distinguishes:

```text
Observed State Change
        ↓
Trigger
        ↓
Re-evaluation
        ↓
Decision
```

A trigger does not automatically require migration.

For example:

```text
Temporary Latency Increase
        ↓
Re-evaluation
        ↓
Recovery Expected
        ↓
Remain
```

Another case may be:

```text
Capacity Pressure
        ↓
Re-evaluation
        ↓
SLA Risk
        ↓
Migrate
```

The transition decision may be:

* migrate,
* rebalance,
* replicate,
* scale out,
* scale in,
* remain,
* terminate.

Deliberate non-action can therefore be preserved as evidence.

---

## Source and Destination Reasoning

The protocol separately records:

```text
Why leave the current placement?
```

and:

```text
Why choose the destination placement?
```

For example:

```text
Why leave Fukuoka?
→ capacity pressure
→ queue growth
→ projected latency risk

Why choose Kanazawa?
→ available capacity
→ acceptable latency
→ compatible checkpoint restore
→ residency requirements preserved
```

These are connected but distinct reasoning layers.

---

## Migration Strategies

The protocol can record migration strategies including:

* cold migration,
* warm migration,
* live migration,
* checkpoint restore,
* replica handoff,
* traffic shift,
* restart at destination.

It can also record whether workload state preservation was:

* full,
* partial,
* none,
* not applicable,
* unknown.

---

## Compute Trajectory

With v0.4, placement becomes a trajectory rather than a point.

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

The protocol can therefore describe the changing physical execution history of an AI workload.

---

# v0.5 — Unified Compute Placement Lifecycle

Version 0.5 closes the first development arc.

It defines a lifecycle envelope that connects independent protocol records through references and transitions.

The lifecycle is:

```text
Workload Intent
      ↓
Model-to-Compute Route Binding
      ↓
Candidate Node Evaluation
      ↓
Placement Decision Receipt
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
      ↓
Lifecycle Closure
```

The core question is:

> Can the complete compute placement history of this workload be traced and explained?

---

## Reference-Based Integration

The lifecycle does not duplicate every lower-level record.

Instead, it connects them:

```text
Unified Lifecycle
       │
       ├── Route Binding Record
       ├── Candidate Evaluation Record
       ├── Initial Placement Receipt
       ├── Execution Record
       ├── Runtime Observation Record
       ├── Migration Receipt(s)
       ├── Completion Record
       └── Placement Audit Record
```

This preserves modularity while enabling end-to-end traceability.

---

## Phase and Transition Separation

The lifecycle distinguishes between:

```text
Phase Record
```

and:

```text
Transition Record
```

A phase records what existed at a particular point in the lifecycle.

A transition records how and why the lifecycle moved from one phase to another.

Example:

```text
Execution
    ↓
Runtime Observation
    ↓
Capacity Pressure Detected
    ↓
Re-evaluation
    ↓
Migration
    ↓
Execution Resumed
```

This creates a stronger accountability structure than a simple event log.

---

## Lifecycle Integrity

v0.5 can record:

* chain completeness,
* reference resolution status,
* evidence sufficiency,
* missing references,
* integrity warnings,
* verification references.

A workload can therefore be operationally successful while still being incomplete from an audit perspective.

For example:

```text
Execution:
successful

Placement reasoning:
complete

Migration evidence:
missing

Audit readiness:
partial
```

Operational success and explainability are not treated as the same thing.

---

## Lifecycle Outcomes

The lifecycle may end as:

* successful,
* successful with migration,
* successful with warning,
* partially successful,
* failed,
* cancelled.

Migration is not treated as failure by default.

```text
Initial Placement
        ↓
Runtime Change
        ↓
Adaptive Migration
        ↓
Execution Continued
        ↓
Successful Completion
```

A successful adaptive move can be part of a healthy compute lifecycle.

---

## Placement Audit

The lifecycle audit summary can independently evaluate:

* placement explainability,
* migration explainability,
* policy traceability,
* evidence completeness,
* overall audit readiness.

This allows the protocol to distinguish:

```text
Workload Completed
```

from:

```text
Placement Lifecycle Explainable
```

---

# Relationship to Computational Pranayama

The Compute Placement Receipt Protocol operates at a different layer from Computational Pranayama and Auto-Pranayama.

```text
Computational Pranayama
When and how much should be computed?
          ↓
Auto-Pranayama
How should compute behavior adapt to changing conditions?
          ↓
Compute Placement Receipt
Where was computation placed, and why?
```

Their roles can be summarized as:

```text
Computational Pranayama
→ Metabolism Layer

Auto-Pranayama
→ Adaptive Control Layer

Compute Placement Receipt
→ Placement Accountability Layer
```

Together, they can form a broader chain:

```text
Need for Computation
        ↓
Compute Intensity Decision
        ↓
Adaptive Routing Decision
        ↓
Model-to-Compute Binding
        ↓
Candidate Evaluation
        ↓
Placement
        ↓
Runtime Observation
        ↓
Migration / Rebalancing
        ↓
Audit
```

---

# Relationship to Trace and Audit Protocols

The protocol can be composed with upstream and downstream accountability systems.

For example:

```text
Question Ignition
        ↓
Trace Relay
        ↓
Origin Trace
        ↓
Agent Handoff
        ↓
Task Formation
        ↓
Model-to-Compute Route Binding
        ↓
Candidate Node Evaluation
        ↓
Placement Decision Receipt
        ↓
Compute Execution
        ↓
Rebalancing and Migration
        ↓
Artifact
        ↓
Contribution Causality
        ↓
Audit
        ↓
Royalty Readiness
```

In this broader architecture:

```text
Trace Causality
```

answers:

> Why did this artifact emerge?

while:

```text
Compute Placement Receipt
```

answers:

> Why was this computation executed here?

Together, they connect meaning-level causality with physical compute causality.

---

# Validation

The repository includes automated validation for JSON Schemas and YAML examples.

Validation covers:

```text
Placement Decision Receipt
Candidate Node Evaluation
Model-to-Compute Route Binding
Rebalancing and Migration Receipt
Unified Compute Placement Lifecycle
```

Run locally:

```bash
python scripts/validate_examples.py
```

The GitHub Actions workflow validates examples on:

* pushes to `main`,
* pull requests targeting `main`,
* manual workflow dispatch.

The current validation boundary covers:

```text
JSON Schema syntax
        ↓
YAML loading
        ↓
Schema ↔ Example validation
```

Potential future validation layers include:

```text
Phase 1
Schema ↔ Example Validation

Phase 2
Internal Reference Consistency

Phase 3
External Receipt Resolution

Phase 4
Digest and Signature Verification
```

---

# First Arc Summary

The first arc of the protocol is now structurally complete.

```text
v0.1
Placement Decision Receipt
        ↓
Where?

v0.2
Candidate Node Evaluation
        ↓
Why this candidate?

v0.3
Model-to-Compute Route Binding
        ↓
Why this route?

v0.4
Rebalancing and Migration Receipt
        ↓
Why move?

v0.5
Unified Compute Placement Lifecycle
        ↓
Can the whole journey be explained?
```

The resulting accountability chain is:

```text
Intent
  ↓
Task
  ↓
Model
  ↓
Compute Requirement
  ↓
Candidate Nodes
  ↓
Evaluation
  ↓
Initial Placement
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

---

# Civilizational Position

AI infrastructure is moving beyond a model defined only by compute ownership.

The emerging environment increasingly depends on:

```text
Discover
   ↓
Evaluate
   ↓
Select
   ↓
Route
   ↓
Execute
   ↓
Observe
   ↓
Rebalance
   ↓
Explain
```

In such an environment, it is no longer sufficient to know:

> What computation happened?

A distributed AI infrastructure also needs to answer:

> Why was this computation placed there?

> Why were other candidates rejected?

> Why was this model bound to this class of compute?

> Why did the workload move?

> Can the complete physical execution history be audited?

The Compute Placement Receipt Protocol provides a machine-readable foundation for answering those questions.

Its central transition is:

```text
Own
 ↓
Place
 ↓
Route
 ↓
Observe
 ↓
Rebalance
 ↓
Explain
```

The protocol treats compute placement not as a hidden scheduling detail, but as an auditable part of the AI lifecycle.

---

# Roadmap

## Completed First Arc

### v0.1 — Placement Decision Receipt

Record why a workload was placed on a selected compute node.

### v0.2 — Candidate Node Evaluation

Record candidate comparison, eligibility, selection, and rejection reasons.

### v0.3 — Model-to-Compute Route Binding

Record why a task was bound to a particular model and class of compute resource.

### v0.4 — Rebalancing and Migration Receipt

Record why a workload was moved, rebalanced, replicated, scaled, retained, or terminated.

### v0.5 — Unified Compute Placement Lifecycle

Connect the complete compute placement history into an auditable lifecycle chain.

---

## Possible Future Extensions

Future work may explore adjacent layers such as:

* distributed compute discovery,
* cross-provider compute identity,
* resource availability attestations,
* compute reservation receipts,
* permit-before-placement records,
* energy source attestations,
* carbon intensity evidence,
* cross-region routing receipts,
* cross-provider migration records,
* placement dispute and review,
* placement appeal records,
* compute allocation bridges,
* settlement readiness,
* cryptographic receipt chaining,
* signed placement evidence,
* cross-lifecycle compute trajectory analysis.

---

## Status

The first candidate arc of the **Compute Placement Receipt Protocol** is structurally complete through `v0.5.0-candidate`.

The protocol now provides a modular accountability chain from:

```text
Task
```

to:

```text
Model
```

to:

```text
Compute Requirement
```

to:

```text
Candidate Evaluation
```

to:

```text
Placement
```

to:

```text
Migration
```

to:

```text
Completion
```

to:

```text
Audit
```

The central principle remains simple:

> Record not only where computation happened, but why it happened there.
