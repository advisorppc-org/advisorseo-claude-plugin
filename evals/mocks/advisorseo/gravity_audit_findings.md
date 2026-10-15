{
  "run_id": "run_0911",
  "findings": [
    {
      "severity": "high",
      "page": "/services/drain-cleaning",
      "issue": "noindex meta tag on a service page",
      "evidence": "<meta name=robots content=noindex>"
    },
    {
      "severity": "high",
      "page": "/",
      "issue": "title tag missing",
      "evidence": "no <title> in head"
    },
    {
      "severity": "medium",
      "page": "/blog/",
      "issue": "12 images without alt text",
      "evidence": "12 <img> with empty alt"
    },
    {
      "severity": "low",
      "page": "/contact",
      "issue": "slow largest contentful paint",
      "evidence": "LCP 4.1 s on mobile"
    }
  ]
}
