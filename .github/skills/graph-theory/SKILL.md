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
- Bellman-Ford → [`content/graph/BellmanFord.h`]
- Konig's theorem and vertex cover → [`content/graph/MinimumVertexCover.h`]
- Min-cost max flow → [`content/graph/MinCostMaxFlow.h`]
- Lovasz toggle
- Matrix tree theorem
- Maximal matching, general graphs → [`content/graph/GeneralMatching.h`]
- Hopcroft-Karp → [`content/graph/HopcroftKarp.h`]
- Hall's marriage theorem
- Graphical sequences
- Floyd-Warshall → [`content/graph/FloydWarshall.h`]
- Euler cycles → [`content/graph/EulerWalk.h`]
- Flow networks → [`content/graph/Dinic.h`], [`content/graph/PushRelabel.h`]
  - Augmenting paths
  - Edmonds-Karp → [`content/graph/EdmondsKarp.h`]
- Bipartite matching → [`content/graph/DFSMatching.h`], [`content/graph/HopcroftKarp.h`]
- Min. path cover
- Topological sorting → [`content/graph/TopoSort.h`]
- Strongly connected components → [`content/graph/SCC.h`]
- 2-SAT → [`content/graph/2sat.h`]
- Cut vertices, cut-edges and biconnected components → [`content/graph/BiconnectedComponents.h`]
- Edge coloring → [`content/graph/EdgeColoring.h`]
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

## Available Implementations

The following implementations from the KACTL codebase are available for this technique:

### Shortest Paths
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Bellman-Ford | `content/graph/BellmanFord.h` | O(VE) | Shortest paths with negative weights, cycle detection |
| Floyd-Warshall | `content/graph/FloydWarshall.h` | O(N³) | All-pairs shortest paths |

### Network Flow
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Dinic's Algorithm | `content/graph/Dinic.h` | O(VE log U) | Max flow; O(√V · E) for bipartite |
| Edmonds-Karp | `content/graph/EdmondsKarp.h` | O(VE²) | Max flow via BFS augmenting paths |
| Push-Relabel | `content/graph/PushRelabel.h` | O(V²√E) | Max flow with gap heuristic |
| Min-Cost Max-Flow | `content/graph/MinCostMaxFlow.h` | O(FE log V) | Minimum-cost maximum flow |
| Min Cut | `content/graph/MinCut.h` | — | Min-cut from max-flow residual graph |
| Global Min Cut | `content/graph/GlobalMinCut.h` | O(V³) | Stoer-Wagner algorithm |
| Gomory-Hu Tree | `content/graph/GomoryHu.h` | — | All-pairs max-flow tree |

### Matching
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| DFS Matching | `content/graph/DFSMatching.h` | O(VE) | Simple bipartite matching |
| Hopcroft-Karp | `content/graph/HopcroftKarp.h` | O(E√V) | Fast bipartite matching |
| General Matching | `content/graph/GeneralMatching.h` | O(N³) | Non-bipartite matching |
| Weighted Matching | `content/graph/WeightedMatching.h` | O(N²M) | Min-cost bipartite matching (Hungarian) |
| Minimum Vertex Cover | `content/graph/MinimumVertexCover.h` | — | König's theorem for bipartite graphs |

### Tree Algorithms
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Binary Lifting | `content/graph/BinaryLifting.h` | O(N log N + Q log N) | LCA via 2^k-jumps |
| LCA | `content/graph/LCA.h` | O(N log N + Q) | Lowest common ancestor via RMQ |
| Heavy-Light Decomposition | `content/graph/HLD.h` | O((log N)²) | Path queries/updates on trees |
| Link-Cut Tree | `content/graph/LinkCutTree.h` | O(log N) amortized | Dynamic forest operations |
| Compress Tree | `content/graph/CompressTree.h` | O(\|S\| log \|S\|) | Virtual tree for node subset |

### Connectivity & Components
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| SCC | `content/graph/SCC.h` | O(E+V) | Tarjan's strongly connected components |
| Biconnected Components | `content/graph/BiconnectedComponents.h` | O(E+V) | Bridges and biconnected components |
| 2-SAT | `content/graph/2sat.h` | O(N+E) | Boolean satisfiability via SCC |
| Topological Sort | `content/graph/TopoSort.h` | O(\|V\|+\|E\|) | DAG topological ordering |

### Euler Paths & Cycles
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Euler Walk | `content/graph/EulerWalk.h` | O(V+E) | Eulerian path/cycle |

### Coloring & Cliques
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Edge Coloring | `content/graph/EdgeColoring.h` | O(NM) | Edge coloring of simple graphs |
| Maximal Cliques | `content/graph/MaximalCliques.h` | O(3^(n/3)) | Bron-Kerbosch enumeration |
| Maximum Clique | `content/graph/MaximumClique.h` | — | Maximum clique with pruning |
| Maximum Independent Set | `content/graph/MaximumIndependentSet.h` | — | Via complement graph |

### Directed Graphs
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Directed MST | `content/graph/DirectedMST.h` | O(E log V) | Minimum spanning arborescence |

### Cross-references

These implementations from other categories also relate to graph theory:
- `content/data-structures/UnionFind.h` — Disjoint-set for connectivity (see also: data-structures skill)
- `content/data-structures/UnionFindRollback.h` — Union-Find with undo for offline graph algorithms
- `content/geometry/ManhattanMST.h` — MST for Manhattan distance (see also: geometry skill)

### Test Coverage

Stress tests: `2sat`, `DirectedMST`, `EdgeColoring`, `EulerWalk`, `GomoryHu`, `HLD`, `LCA`, `LinkCutTree`, `MaximalCliques`, `MaximumClique`, `MinCostMaxFlow`, `MinimumVertexCover`, `SCC`, `TopoSort`, `WeightedMatching`, `maxflow`
Old unit tests: `DFSMatching`, `HopcroftKarp`

## Troubleshooting

- **Wrong answer**: Check for off-by-one in node indexing (0-based vs 1-based)
- **TLE**: Verify graph representation efficiency; consider adjacency list over matrix
- **Runtime error**: Check for accessing non-existent nodes or edges
- **MLE**: Use adjacency list for sparse graphs
