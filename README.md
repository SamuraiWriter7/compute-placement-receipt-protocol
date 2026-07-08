# Compute Placement Receipt Protocol

An open protocol for recording why AI workloads are placed, routed, migrated, and executed across distributed compute resources.

## Overview

AI workloads are increasingly executed across heterogeneous and distributed compute environments.

A workload may be placed on:

- an edge device,
- an NPU,
- a local cluster,
- a regional datacenter,
- a cloud region,
- or a distributed GPU cluster.

Existing orchestration systems can make placement decisions.

However, the reasoning behind those decisions is often fragmented across scheduler logs, policy engines, telemetry systems, and infrastructure-specific records.

The Compute Placement Receipt Protocol defines a machine-readable receipt layer for recording:

- what workload required placement,
- which compute node was selected,
- why the node was selected,
- which constraints affected the decision,
- who or what made the decision,
- and which evidence supported the decision.

The protocol does not define a scheduler.

It defines an accountability layer for placement decisions.


## Core Question

The protocol answers:

> Why was this computation executed here?


## v0.1 — Placement Decision Receipt

Version 0.1 defines the minimum placement decision record.

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

A receipt records:

workload reference,
selected compute node,
primary placement reason,
reason codes,
policy or constraint references,
decision timestamp,
decision actor,
supporting evidence references.
Example
schema_version: "0.1"

protocol: "compute-placement-receipt-protocol"

placement_receipt_id: "cprp-20260708-0001"

workload_ref:
  workload_id: "workload-research-042"
  model_ref: "model-research-large-v3"

selected_node:
  node_id: "fukuoka-gpu-003"
  node_type: "gpu_cluster"
  region: "JP-FUK"

placement_reason:
  primary_reason: "energy"

  reason_codes:
    - "sufficient_gpu_memory"
    - "latency_within_policy"
    - "lower_energy_cost"

  summary: >
    The selected node satisfied workload requirements
    while reducing projected energy cost.

constraint_refs:
  - "policy://latency/jp-interactive-v1"
  - "policy://data-residency/jp-only"

decision_at: "2026-07-08T00:30:00Z"

decision_actor:
  actor_type: "scheduler"
  actor_id: "placement-scheduler-alpha"

evidence_refs:
  - evidence_type: "capacity_snapshot"
    ref: "evidence://capacity/fukuoka-gpu-003/20260708T003000Z"
Design Principles
1. Record decisions, do not replace schedulers

This protocol does not determine where workloads should run.

It records placement decisions made by schedulers, agents, policy engines, humans, or hybrid systems.

2. Reason, not only result

A node identifier alone is insufficient.

A useful receipt should preserve:

Selected Node
+
Reason
+
Constraints
+
Decision Actor
+
Evidence
3. Infrastructure neutrality

The protocol is designed to remain independent of:

cloud providers,
GPU vendors,
orchestration engines,
network architectures,
AI model providers.
4. Composable receipts

Placement receipts may be referenced by:

agent action receipts,
task execution records,
artifact provenance records,
synchronization audits,
compute allocation audits,
royalty readiness systems.
Relationship to Computational Pranayama

The protocols operate at different layers.

Computational Pranayama
When and how much should be computed?
          ↓
Auto-Pranayama
How should compute behavior adapt to changing conditions?
          ↓
Compute Placement Receipt
Where was computation placed, and why?

Computational Pranayama is a metabolism layer.

Compute Placement Receipt is a placement accountability layer.

Roadmap
v0.1 — Placement Decision Receipt

Record the selected node and the reason for placement.

v0.2 — Candidate Node Evaluation

Record candidate nodes, evaluation dimensions, rankings, and rejection reasons.

v0.3 — Model-to-Compute Route Binding

Bind:

Task
 ↓
Model
 ↓
Compute Type
 ↓
Node
v0.4 — Rebalancing and Migration Receipt

Record why an active workload was moved or rebalanced.

v0.5 — Unified Compute Placement Lifecycle

Integrate:

Workload Intent
      ↓
Resource Requirement
      ↓
Candidate Discovery
      ↓
Constraint Evaluation
      ↓
Placement Decision
      ↓
Execution
      ↓
Rebalancing
      ↓
Completion
      ↓
Placement Audit
Civilizational Position

AI infrastructure is moving from a model based only on compute ownership toward one increasingly shaped by compute discovery, selection, routing, and placement.

In such an environment, it becomes important not only to know:

What computation happened?

but also:

Why was the computation placed there?

The Compute Placement Receipt Protocol provides a minimal trace layer for that question.

## v0.2 — Candidate Node Evaluation

Version 0.2 extends the protocol from a single placement result to the evaluation context that produced the decision.

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
