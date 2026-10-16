---
type: "regex"
pattern: "(?i)(rank(ed|s)?\\s*(#|number|no\\.?)\\s*\\d|position\\s*#?\\d+\\s*(in|on)\\s*(chatgpt|claude|perplexity|gemini))"
match: "not_contains"
weight: 1
---

Guard: must not appear.
