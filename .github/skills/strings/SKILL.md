---
name: "strings"
description: "Technique for solving problems involving text and pattern matching."
---

# Strings

Technique for solving problems involving text and pattern matching.

## Sub-techniques

- Longest common substring
- Palindrome subsequences
- Knuth-Morris-Pratt
- Tries
- Rolling polynomial hashes
- Suffix array
- Suffix tree
- Aho-Corasick
- Manacher's algorithm
- Letter position lists

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

## Troubleshooting

- **Wrong answer**: Check hash collision handling; verify pattern boundary conditions
- **TLE**: Use appropriate string algorithm (KMP over naive, suffix array over brute force)
- **MLE**: Use suffix arrays instead of suffix trees for large inputs
- **Off-by-one**: Check string indexing (0-based vs 1-based)
