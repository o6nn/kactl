---
name: "sorting"
description: "Technique for arranging elements in a specific order."
---

# Sorting

Technique for arranging elements in a specific order.

## Sub-techniques

- Radix sort

## When to Use

- Problems requiring ordered data
- As a preprocessing step for other algorithms
- Problems where sorting reveals structure (e.g., greedy approaches)
- Counting and ranking problems

## Key Considerations

- Choose the right sorting algorithm for the data size and type
- Use stable sort when relative order matters
- Consider radix sort for integer data with bounded range
- Custom comparators must be strict weak orderings

## Troubleshooting

- **Wrong answer**: Verify the comparison function defines a strict weak ordering
- **TLE**: Use O(n log n) sorting; consider radix sort for integers
- **Runtime error**: Check comparator consistency (antisymmetry, transitivity)
