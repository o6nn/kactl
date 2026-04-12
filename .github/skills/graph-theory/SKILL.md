---
name: "graph-theory"
description: "Technique for solving problems modeled as graphs with vertices and edges."
---

# Graph Theory

Technique for solving problems modeled as graphs with vertices and edges.

## Sub-techniques

- Dynamic graphs (extra book-keeping)
- Breadth first search
- Depth first search
  - Normal trees / DFS trees
- Dijkstra's algorithm
- MST: Prim's algorithm
- Bellman-Ford
- Konig's theorem and vertex cover
- Min-cost max flow
- Lovasz toggle
- Matrix tree theorem
- Maximal matching, general graphs
- Hopcroft-Karp
- Hall's marriage theorem
- Graphical sequences
- Floyd-Warshall
- Euler cycles
- Flow networks
  - Augmenting paths
  - Edmonds-Karp
- Bipartite matching
- Min. path cover
- Topological sorting
- Strongly connected components
- 2-SAT
- Cut vertices, cut-edges and biconnected components
- Edge coloring
  - Trees
- Vertex coloring
  - Bipartite graphs (=> trees)
  - 3^n (special case of set cover)
- Diameter and centroid
- K'th shortest path
- Shortest cycle

## When to Use

- Problems involving networks, connections, or relationships
- Shortest path problems
- Connectivity and component analysis
- Matching and flow problems
- Cycle detection and topological ordering

## Key Considerations

- Choose the right graph representation (adjacency list vs. matrix)
- Handle directed vs. undirected graphs correctly
- Watch for negative edge weights (Bellman-Ford vs. Dijkstra)
- Consider whether the graph is sparse or dense for algorithm selection

## Troubleshooting

- **Wrong answer**: Check for off-by-one in node indexing (0-based vs 1-based)
- **TLE**: Verify graph representation efficiency; consider adjacency list over matrix
- **Runtime error**: Check for accessing non-existent nodes or edges
- **MLE**: Use adjacency list for sparse graphs
