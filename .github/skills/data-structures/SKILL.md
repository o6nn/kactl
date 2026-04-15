---
name: "data-structures"
description: "Technique for organizing and accessing data efficiently."
---

# Data Structures

Technique for organizing and accessing data efficiently.

## Sub-techniques

- LCA (2^k-jumps in trees in general)
- Pull/push-technique on trees
- Heavy-light decomposition
- Centroid decomposition
- Lazy propagation
- Self-balancing trees
- Convex hull trick (wcipeg.com/wiki/Convex_hull_trick)
- Monotone queues / monotone stacks / sliding queues
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

## Troubleshooting

- **Wrong answer**: Check lazy propagation push-down logic; verify tree indexing
- **TLE**: Ensure data structure operations are O(log n); avoid unnecessary copies
- **MLE**: Use memory-efficient representations; limit persistent tree nodes
- **Runtime error**: Check array bounds; verify tree construction
