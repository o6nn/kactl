---
name: "sweeping"
description: "Technique for solving problems by processing events in a specific order."
---

# Sweeping

Technique for solving problems by processing events in a specific order.

## Sub-techniques

- Discretization (convert to events and sweep)
- Angle sweeping
- Line sweeping
- Discrete second derivatives

## When to Use

- Interval and range problems
- Geometric intersection problems
- Problems that can be decomposed into events
- Finding overlaps, intersections, or coverage

## Key Considerations

- Sort events by the sweep coordinate
- Maintain an appropriate data structure during the sweep
- Handle simultaneous events carefully (tie-breaking)
- Consider what information needs to be tracked during the sweep

## Troubleshooting

- **Wrong answer**: Check event ordering and tie-breaking rules
- **TLE**: Use efficient data structures (balanced BST, segment tree) during sweep
- **Edge cases**: Handle coincident events and boundary conditions
