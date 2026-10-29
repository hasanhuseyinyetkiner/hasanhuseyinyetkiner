# Portfolio README design notes

This document records the design decisions for the profile and the five product READMEs. It is a maintenance note, not a claim of application maturity.

## Baseline · 29 October 2026

- **Profile:** the previous README repeated a large project table beneath a logo grid. The profile's systems background was present but the HR collection dominated the opening. Project descriptions and career details were retained in a shorter hierarchy.
- **Policy Copilot:** real answer, source and abstention screenshots existed; the first screenshot followed several overview tables. The held-out evaluation exposed a revision-scoped query gap.
- **Process Miner:** process map, bottleneck and variant captures existed; important metric and optional PM4Py licensing caveats needed to remain discoverable.
- **Workforce Optimizer:** real screenshots and solver evidence existed; validator boundaries and infeasibility semantics needed to stay explicit. Existing captures use a light interface.
- **FairHire:** group, quality and report screenshots existed; small-group suppression, statistical uncertainty and threshold limitations needed prominence.
- **SkillGraph:** real graph, role and path captures existed; the synthetic evaluation and separation between mandatory requirements and related-skill credit needed context.

Each product is a single-operator local MVP; existing screenshots are synthetic examples, not proof of production readiness. The product READMEs link to their source evaluation and security documents. The five repositories were public when checked; visibility can change.

## Visual direction

Use short, direct headings, a compact logo, two meaningful badges, an authentic screen early, and an architecture diagram grounded in code. Keep documentation and limitation links close to the implementation evidence. Existing accent colors distinguish the products. The profile now leads with devices and tooling, highlights two applied systems experiments, and links to the remaining experiments without giving each a full promotional card.

The earlier profile cards remain available as static SVG assets; they are not used by the current profile README. Regenerate them from the profile repository root with `python scripts/generate_cards.py` if needed. Product screenshots use existing light/dark pairs where available.

Each product README also links to an optional GIF recorded from its actual UI with synthetic data. The static screenshot remains the default for readers who prefer not to view motion. All five product repositories include recorder scripts; check each README for the platform, installed dependencies, and retained temporary-data notes. When committing documentation changes, include the new GIFs, scripts and profile SVGs as well as the README edits.

## Reference review

The [awesome README collection](https://github.com/matiassingers/awesome-readme), [profile README collection](https://github.com/abhisheknaiidu/awesome-github-profile-readme), [README template](https://github.com/othneildrew/Best-README-Template), [profile templates](https://github.com/kautukkundan/Awesome-Profile-README-templates), and the [profile](https://github.com/rahuldkjain/github-profile-readme-generator) and [README](https://github.com/kefranabg/readme-md-generator) generators informed the hierarchy and navigation, without copying a template.

The product presentation in [Twenty](https://github.com/twentyhq/twenty), [Dify](https://github.com/langgenius/dify), [Netdata](https://github.com/netdata/netdata), [Prefect](https://github.com/PrefectHQ/prefect), [Gradio](https://github.com/gradio-app/gradio), and [Streamlit](https://github.com/streamlit/streamlit) informed the balance of a clear introduction, visual proof, practical entry points and deeper documentation.

[Shields](https://github.com/badges/shields) supplies restrained license badges; [Simple Icons](https://github.com/simple-icons/simple-icons) and [Skill Icons](https://github.com/tandpfun/skill-icons) were considered but a logo wall would add little evidence. [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats), [Typing SVG](https://github.com/DenverCoder1/readme-typing-svg), and [Profile Trophy](https://github.com/ryo-ma/github-profile-trophy) were considered but omitted: a project showcase adds more useful information without relying on a third-party dynamic rendering service. GitHub Readme Stats also documents public-instance rate limits and the public-repository scope of its default statistics.
