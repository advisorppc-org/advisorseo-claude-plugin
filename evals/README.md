# Evals

Why: a skill change that stops the right tool from being called, presents stored data as live, or follows instructions found inside a record must be caught before a release reaches users.

15 cases, 3 per skill, in the `claude plugin eval` layout: `evals/<skill>--<case>/prompt.md` holds the user prompt, and `graders/` holds one file per check:

- `tool.md`: the expected tool (`tool_used`), or for the should-not-fire case, that no AdvisorSEO tool is called.
- `regex.md`: a pattern the reply must contain.
- `rubric.md`: an LLM-graded rubric written as checkable claims.
- `guard-*.md`: hard guards, for example that a prompt-injection line inside a saved record does not trigger a tool call.

`mocks/advisorseo/<tool>.md` holds a canned result for each of the six read-only tools, so no run touches the real connector. The `advisorseo_get_content` mock carries a prompt-injection line and `truncated: true` on purpose.

## Who runs them, and when

A maintainer runs them on a Claude seat before each release. They never run in CI: each run is real model usage.

```
claude plugin eval . --trust-plugin --judge-model sonnet --runs 3 -j 2
```

Use `--case 'content-review--*'` to run one skill's cases. Results land in `evals/results/` (git-ignored); attach the report to the GitHub Release.

## Pass bar

Every case at 1.0 with the plugin, and the with-without ablation delta positive for each skill. A failed guard blocks the release.
