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
- Convex hull → [`content/geometry/ConvexHull.h`]
- Polygon cut → [`content/geometry/PolygonCut.h`]
- Closest pair → [`content/geometry/ClosestPair.h`]
- Coordinate-compression
- Quadtrees
- KD-trees → [`content/geometry/kdTree.h`]
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

## Available Implementations

The following implementations from the KACTL codebase are available for this technique:

### Geometric Primitives
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| 2D Point | `content/geometry/Point.h` | — | Point class with basic operations |
| 3D Point | `content/geometry/Point3D.h` | — | 3D point class |
| Line Distance | `content/geometry/lineDistance.h` | O(1) | Signed distance from point to line |
| Segment Distance | `content/geometry/SegmentDistance.h` | O(1) | Point-to-segment distance |
| Segment Intersection | `content/geometry/SegmentIntersection.h` | O(1) | Two segment intersection (handles unique/infinite) |
| Line Intersection | `content/geometry/lineIntersection.h` | O(1) | Two line intersection |
| Side Of | `content/geometry/sideOf.h` | O(1) | Point position relative to directed line |
| On Segment | `content/geometry/OnSegment.h` | O(1) | Point on segment test |
| Linear Transformation | `content/geometry/linearTransformation.h` | O(1) | Translate, rotate, scale |
| Line Projection/Reflection | `content/geometry/LineProjectionReflection.h` | O(1) | Point projection/reflection on line |
| Angle | `content/geometry/Angle.h` | — | Angle ordering class for rotational sweeping |

### Circles
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Circle-Circle Intersection | `content/geometry/CircleIntersection.h` | O(1) | Circle-circle intersection points |
| Circle-Line Intersection | `content/geometry/CircleLine.h` | O(1) | Circle-line intersection |
| Circle Tangents | `content/geometry/CircleTangents.h` | O(1) | External/internal tangent lines |
| Circle-Polygon Intersection | `content/geometry/CirclePolygonIntersection.h` | O(n) | Circle-polygon intersection area |
| Circumcircle | `content/geometry/circumcircle.h` | O(1) | Circumcircle of triangle |

### Polygons
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Convex Hull | `content/geometry/ConvexHull.h` | O(n log n) | Convex hull construction |
| Hull Diameter | `content/geometry/HullDiameter.h` | O(n) | Max distance on convex hull (rotating calipers) |
| Point Inside Hull | `content/geometry/PointInsideHull.h` | O(log N) | Point in convex hull test |
| Inside Polygon | `content/geometry/InsidePolygon.h` | O(n) | Point in arbitrary polygon |
| Polygon Area | `content/geometry/PolygonArea.h` | O(n) | Signed polygon area |
| Polygon Center | `content/geometry/PolygonCenter.h` | O(n) | Center of mass |
| Polygon Cut | `content/geometry/PolygonCut.h` | O(n) | Sutherland-Hodgman polygon cut |
| Polygon Union | `content/geometry/PolygonUnion.h` | O(N²) | Union area of multiple polygons |
| Line-Hull Intersection | `content/geometry/LineHullIntersection.h` | O(log n) | Line-convex polygon intersection |

### Point Set Problems
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Closest Pair | `content/geometry/ClosestPair.h` | O(n log n) | Closest pair of points |
| Minimum Enclosing Circle | `content/geometry/MinimumEnclosingCircle.h` | O(n) expected | Smallest enclosing circle |
| KD-Tree | `content/geometry/kdTree.h` | — | KD-tree for 2D queries |
| Manhattan MST | `content/geometry/ManhattanMST.h` | O(N log N) | MST for Manhattan distance |
| Delaunay Triangulation | `content/geometry/DelaunayTriangulation.h` | O(n²) | Delaunay triangulation |
| Fast Delaunay | `content/geometry/FastDelaunay.h` | O(n log n) | Fast Delaunay triangulation |

### 3D Geometry
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| 3D Convex Hull | `content/geometry/3dHull.h` | O(n²) | 3D convex hull |
| Polyhedron Volume | `content/geometry/PolyhedronVolume.h` | — | Polyhedron volume |
| Spherical Distance | `content/geometry/sphericalDistance.h` | O(1) | Distance on sphere |

### Cross-references

These implementations from other categories also relate to geometry:
- `content/data-structures/SubMatrix.h` — 2D submatrix sums (see also: data-structures skill)

### Test Coverage

Stress tests: `CircleIntersection`, `CircleLine`, `CirclePolygon`, `CircleTangents`, `ClosestPair`, `ConvexHull`, `DelaunayTriangulation`, `FastDelaunay`, `HullDiameter`, `LineHullIntersection`, `LineIntersection`, `LineProjectionReflection`, `ManhattanMST`, `MinimumEnclosingCircle`, `PointInsideHull`, `PolygonArea`, `PolygonCut`, `PolygonUnion`, `SegmentIntersection`, `insidePolygon`

## Troubleshooting

- **Wrong answer**: Check for degenerate cases; verify cross product sign conventions
- **Precision errors**: Use integer arithmetic or epsilon comparisons
- **TLE**: Use spatial data structures (KD-trees, quadtrees) for queries
- **Runtime error**: Handle division by zero in line intersection
