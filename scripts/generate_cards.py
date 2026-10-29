"""Regenerate the profile's self-contained, GitHub-compatible SVG project cards."""

from html import escape
from pathlib import Path

CARDS = [
    ("hr-policy-copilot", "01", "HR Policy Copilot", "Evidence-backed policy answers", "QUESTION  /  RETRIEVAL  /  EVIDENCE  /  CITATION", "#0F766E"),
    ("hiring-process-miner", "02", "Hiring Process Miner", "Understand the flow behind hiring operations", "EVENT LOG  /  PROCESS MAP  /  BOTTLENECKS", "#6D28D9"),
    ("workforce-optimizer", "03", "Workforce Optimizer", "Constraint-based scheduling with independent validation", "CONSTRAINTS  /  CP-SAT  /  SCHEDULE  /  VALIDATION", "#B45309"),
    ("fairhire-audit", "04", "FairHire Audit", "Inspect group disparities and statistical uncertainty", "EVALUATION DATA  /  GROUP METRICS  /  AUDIT", "#1D4ED8"),
    ("skillgraph", "05", "SkillGraph", "Explainable role fit and cycle-safe learning paths", "PROFILE  /  SKILL GRAPH  /  ROLE FIT  /  PATH", "#A21CAF"),
]

OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(exist_ok=True)
for slug, number, title, subtitle, flow, accent in CARDS:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="152" viewBox="0 0 1080 152" role="img" aria-label="{escape(title)}: {escape(subtitle)}">
  <rect x="0.5" y="0.5" width="1079" height="151" rx="12" fill="#f8fafc" stroke="#d8dee6"/>
  <rect x="0" y="17" width="5" height="118" rx="2.5" fill="{accent}"/>
  <text x="30" y="42" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="700" letter-spacing="2" fill="{accent}">ENGINEERING STUDY / {number}</text>
  <text x="30" y="81" font-family="Arial,Helvetica,sans-serif" font-size="28" font-weight="700" fill="#152238">{escape(title)}</text>
  <text x="30" y="111" font-family="Arial,Helvetica,sans-serif" font-size="17" fill="#48576a">{escape(subtitle)}</text>
  <text x="30" y="137" font-family="Arial,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.1" fill="{accent}">{escape(flow)}</text>
  <path d="M1021 59h25m-9-9 9 9-9 9" fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
'''
    (OUT / f"{slug}.svg").write_text(svg, encoding="utf-8", newline="\n")
