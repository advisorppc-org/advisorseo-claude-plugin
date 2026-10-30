# Evals

Why: a skill change that stops the right tool from being called, or lets a write through without approval, must be caught before a release reaches users.

33 cases, 3 per skill, in the `claude plugin eval` layout: `evals/<skill>--<case>/prompt.md` holds the user prompt, and `graders/` holds one file per check:

- `tool.md`: the expected tool (`tool_used`), or for the should-not-fire case, that no AdvisorSEO tool is called.
- `regex.md`: a pattern the reply must contain.
- `rubric.md`: an LLM-graded rubric written as checkable claims.
- `guard-*.md`: hard guards, mainly that no write tool is called with `confirm=true` in the first turn, and that no AI rank position, letter grade or FAQ-schema advice appears.

`mocks/advisorseo/<tool>.md` holds canned results for every tool the cases can call, so no run touches the real connector or a real site. The leads mock carries a prompt-injection line on purpose.

## Who runs them, and when

The maintainers run them before each release. They never run in CI: each run is real model usage on a real account.

```
claude plugin eval . --trust-plugin --judge-model sonnet --runs 3 -j 2
```

Use `--case 'leads--*'` to run one skill's cases. Results land in `evals/results/` (git-ignored); attach the HTML report to the GitHub Release.

## Pass bar

Every case at 1.0 with the plugin, and the with-without ablation delta positive for each skill. A failed guard blocks the release.

## First-run note

Why: the grader field names (`tool`, `input_match`, `min`, `max`, `arm`, `pattern`, `match`) and the plugin tool prefix `mcp__plugin_advisorseo_advisorseo__` follow the CLI's eval format as read on 2026-10-15. If the first run reports a schema error, fix the field name across all graders in one commit before scoring.
