{
  "domain": "brightplumbing.example",
  "bots": [
    {
      "bot": "OAI-SearchBot",
      "kind": "search",
      "status": "ok",
      "reason": "allowed by robots.txt, HTTP 200"
    },
    {
      "bot": "ChatGPT-User",
      "kind": "user-fetch",
      "status": "ok",
      "reason": "allowed, HTTP 200"
    },
    {
      "bot": "Claude-SearchBot",
      "kind": "search",
      "status": "ok",
      "reason": "allowed, HTTP 200"
    },
    {
      "bot": "Claude-User",
      "kind": "user-fetch",
      "status": "ok",
      "reason": "allowed, HTTP 200"
    },
    {
      "bot": "PerplexityBot",
      "kind": "search",
      "status": "blocked",
      "reason": "robots.txt: Disallow: / for PerplexityBot"
    },
    {
      "bot": "Perplexity-User",
      "kind": "user-fetch",
      "status": "blocked",
      "reason": "HTTP 403 from the CDN firewall"
    },
    {
      "bot": "Google-Extended",
      "kind": "search",
      "status": "ok",
      "reason": "no rule, default allow"
    }
  ]
}
