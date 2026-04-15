---
name: "geometry"
description: "Technique for solving problems involving geometric objects and spatial relationships."
---

# Geometry

Technique for solving problems involving geometric objects and spatial relationships.

## Sub-techniques

- Coordinates and vectors
  - Cross product
  - Scalar product
- Convex hull
- Polygon cut
- Closest pair
- Coordinate-compression
- Quadtrees
- KD-trees
- All segment-segment intersection

## When to Use

- Problems involving points, lines, polygons, and circles
- Convex hull and polygon operations
- Distance and intersection computations
- Spatial partitioning and nearest neighbor queries

## Key Considerations

- Use integer arithmetic where possible to avoid floating-point errors
- Handle degenerate cases (collinear points, overlapping segments)
- Use cross product for orientation tests
- Consider coordinate compression for discrete geometry

## Troubleshooting

- **Wrong answer**: Check for degenerate cases; verify cross product sign conventions
- **Precision errors**: Use integer arithmetic or epsilon comparisons
- **TLE**: Use spatial data structures (KD-trees, quadtrees) for queries
- **Runtime error**: Handle division by zero in line intersection
