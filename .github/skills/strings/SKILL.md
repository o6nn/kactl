---
name: "strings"
description: "Technique for solving problems involving text and pattern matching."
---

# Strings

Technique for solving problems involving text and pattern matching.

## Sub-techniques

- Longest common substring
- Palindrome subsequences
- Knuth-Morris-Pratt (`content/strings/KMP.h`)
- Tries
- Rolling polynomial hashes (`content/strings/Hashing.h`)
- Suffix array (`content/strings/SuffixArray.h`)
- Suffix tree (`content/strings/SuffixTree.h`)
- Aho-Corasick (`content/strings/AhoCorasick.h`)
- Manacher's algorithm (`content/strings/Manacher.h`)
- Letter position lists
- Z-function (`content/strings/Zfunc.h`)
- Min Rotation (`content/strings/MinRotation.h`)
- Hashing for Codeforces (`content/strings/Hashing-codeforces.h`)

## When to Use

- Pattern matching and searching
- String comparison and similarity
- Palindrome detection
- Multiple pattern matching
- Substring and suffix queries

## Key Considerations

- Choose the right string algorithm for the problem type
- Use hashing for probabilistic matching (with collision handling)
- Consider suffix arrays over suffix trees for memory efficiency
- Handle character encoding and alphabet size

## Available Implementations

| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| KMP | `content/strings/KMP.h` | O(n) | Knuth-Morris-Pratt failure function |
| Z-function | `content/strings/Zfunc.h` | O(n) | Longest common prefix of s[i:] and s |
| Manacher | `content/strings/Manacher.h` | O(N) | Longest palindrome at each position |
| Min Rotation | `content/strings/MinRotation.h` | O(N) | Lexicographically smallest rotation |
| Suffix Array | `content/strings/SuffixArray.h` | O(n log n) | Suffix array + LCP array |
| Suffix Tree | `content/strings/SuffixTree.h` | O(26N) | Ukkonen's online suffix tree |
| Hashing | `content/strings/Hashing.h` | — | Polynomial hashing mod 2^64-1 |
| Hashing (Codeforces) | `content/strings/Hashing-codeforces.h` | — | Double hashing for adversarial data |
| Aho-Corasick | `content/strings/AhoCorasick.h` | O(26N) | Multiple pattern matching automaton |

**Stress tests available for:** AhoCorasick, Hashing, Hashing-codeforces, KMP, MinRotation, SuffixArray, Zfunc

## Troubleshooting

- **Wrong answer**: Check hash collision handling; verify pattern boundary conditions
- **TLE**: Use appropriate string algorithm (KMP over naive, suffix array over brute force)
- **MLE**: Use suffix arrays instead of suffix trees for large inputs
- **Off-by-one**: Check string indexing (0-based vs 1-based)
