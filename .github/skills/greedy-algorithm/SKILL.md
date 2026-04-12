---
name: "greedy-algorithm"
description: "Technique for solving optimization problems by making locally optimal choices at each step."
---

# Greedy Algorithm

Technique for solving optimization problems by making locally optimal choices at each step.

## Sub-techniques

- Scheduling
- Max contiguous subvector sum
- Invariants
- Huffman encoding

## When to Use

- Problems where a locally optimal choice leads to a globally optimal solution
- Scheduling and interval problems
- Minimum spanning trees
- Huffman coding and data compression
- Problems with optimal substructure and greedy choice property

## Key Considerations

- Prove that the greedy choice property holds before implementing
- Verify optimal substructure
- Consider whether sorting the input first enables a greedy approach
- Watch for cases where greedy fails and DP is needed instead

## Troubleshooting

- **Wrong answer**: The greedy choice property may not hold; consider DP or other approaches
- **Edge cases**: Check empty input, single-element input, and tied values
- **Sorting issues**: Verify the comparison function is correct and consistent
