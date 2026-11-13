{
  "site_id": "site_7f3a",
  "window_days": 30,
  "engine": null,
  "prompt_id": null,
  "sampled": {
    "runs": 42,
    "status": "ok",
    "presence": {
      "successes": 18,
      "runs": 42,
      "status": "ok",
      "rate": 0.4286,
      "ci95_low": 0.291,
      "ci95_high": 0.5778
    },
    "own_citation": {
      "successes": 9,
      "runs": 42,
      "status": "ok",
      "rate": 0.2143,
      "ci95_low": 0.1171,
      "ci95_high": 0.3594
    },
    "competitors": [
      {
        "name": "Rapid Rooter",
        "successes": 25,
        "runs": 42,
        "status": "ok",
        "rate": 0.5952,
        "ci95_low": 0.4448,
        "ci95_high": 0.7296
      }
    ],
    "competitors_total": 1,
    "competitors_truncated": false,
    "by_engine": [
      {
        "engine": "chatgpt",
        "surface": "app",
        "presence": {
          "successes": 11,
          "runs": 22,
          "status": "ok",
          "rate": 0.5,
          "ci95_low": 0.3072,
          "ci95_high": 0.6928
        },
        "own_citation": {
          "successes": 6,
          "runs": 22,
          "status": "ok",
          "rate": 0.2727,
          "ci95_low": 0.1315,
          "ci95_high": 0.4815
        }
      },
      {
        "engine": "perplexity",
        "surface": "app",
        "presence": {
          "successes": 7,
          "runs": 20,
          "status": "ok",
          "rate": 0.35,
          "ci95_low": 0.1812,
          "ci95_high": 0.5671
        },
        "own_citation": {
          "successes": 3,
          "runs": 20,
          "status": "ok",
          "rate": 0.15,
          "ci95_low": 0.0524,
          "ci95_high": 0.3604
        }
      }
    ]
  },
  "imported_first_party": {
    "label": "imported first-party numbers",
    "basis": "rows a person exported and imported; not added to sampled runs",
    "totals": [
      {
        "source": "bing_ai_performance",
        "metric": "citations",
        "total": 61,
        "rows": 14,
        "first_day": "2026-10-14",
        "last_day": "2026-11-10"
      }
    ]
  },
  "untrusted_text": true
}
