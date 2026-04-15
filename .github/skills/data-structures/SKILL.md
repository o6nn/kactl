---
name: "data-structures"
description: "Technique for organizing and accessing data efficiently."
---

# Data Structures

Technique for organizing and accessing data efficiently.

## Sub-techniques

- LCA (2^k-jumps in trees in general) → see `content/graph/LCA.h` and `content/graph/BinaryLifting.h` (cross-ref)
- Pull/push-technique on trees
- Heavy-light decomposition → see `content/graph/HLD.h` (cross-ref)
- Centroid decomposition
- Lazy propagation → `content/data-structures/LazySegmentTree.h`
- Self-balancing trees → `content/data-structures/Treap.h`
- Convex hull trick (wcipeg.com/wiki/Convex_hull_trick) → `content/data-structures/LineContainer.h`
- Monotone queues / monotone stacks / sliding queues — no dedicated implementation
- Sliding queue using 2 stacks
- Persistent segment tree

## When to Use

- Problems requiring efficient range queries and updates
- Tree path queries
- Problems needing dynamic order statistics
- Maintaining sorted or prioritized data under modifications

## Key Considerations

- Choose the right data structure for the query and update types
- Consider lazy propagation for range updates on segment trees
- Use heavy-light or centroid decomposition for tree path queries
- Persistent structures for versioned or historical queries

## Available Implementations

The following implementations from the KACTL codebase are available for this technique:

| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Segment Tree | `content/data-structures/SegmentTree.h` | O(log N) | Zero-indexed max-tree |
| Lazy Segment Tree | `content/data-structures/LazySegmentTree.h` | O(log N) | Range updates with lazy propagation |
| Union-Find | `content/data-structures/UnionFind.h` | O(α(N)) | Disjoint-set data structure |
| Union-Find Rollback | `content/data-structures/UnionFindRollback.h` | O(log N) | Disjoint-set with undo |
| Fenwick Tree | `content/data-structures/FenwickTree.h` | O(log N) | Binary indexed tree for partial sums |
| Fenwick Tree 2D | `content/data-structures/FenwickTree2d.h` | O(log² N) | 2D Fenwick tree for submatrix sums |
| RMQ | `content/data-structures/RMQ.h` | O(\|V\| log \|V\| + Q) | Sparse table range minimum queries |
| Treap | `content/data-structures/Treap.h` | O(log N) | Randomized BST with split/merge |
| HashMap | `content/data-structures/HashMap.h` | — | ~3x faster than unordered_map |
| Order Statistic Tree | `content/data-structures/OrderStatisticTree.h` | O(log N) | Set with n'th element and rank |
| Matrix | `content/data-structures/Matrix.h` | — | Square matrix operations and exponentiation |
| Line Container | `content/data-structures/LineContainer.h` | O(log N) | Convex hull trick for max queries |
| SubMatrix | `content/data-structures/SubMatrix.h` | O(N² + Q) | 2D prefix sums |
| Mo's Queries | `content/data-structures/MoQueries.h` | O(N√Q) | Offline interval queries |

### Cross-references

These implementations from other categories also relate to data structures:
- `content/graph/BinaryLifting.h` — LCA via 2^k-jumps (see also: graph-theory skill)
- `content/graph/LCA.h` — LCA via RMQ (see also: graph-theory skill)
- `content/graph/HLD.h` — Heavy-light decomposition for tree path queries (see also: graph-theory skill)
- `content/graph/LinkCutTree.h` — Dynamic tree operations (see also: graph-theory skill)
- `content/various/IntervalContainer.h` — Disjoint interval set with merging (see also: sweeping skill)

### Test Coverage

Stress tests: `FenwickTree`, `FenwickTree2d`, `LazySegmentTree`, `LineContainer`, `MoQueries`, `RMQ`, `SegmentTree`, `Treap`
Old unit tests: `Matrix`, `intervalUnion`, `unionFind`

## Troubleshooting

- **Wrong answer**: Check lazy propagation push-down logic; verify tree indexing
- **TLE**: Ensure data structure operations are O(log n); avoid unnecessary copies
- **MLE**: Use memory-efficient representations; limit persistent tree nodes
- **Runtime error**: Check array bounds; verify tree construction
