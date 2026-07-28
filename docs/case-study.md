# UX design — HashiTracker
 
## Problem
 
Managing Hashimoto's thyroiditis means tracking symptoms, lifestyle factors, diet, and medications to identify patterns that lead to flare-ups. Most existing health-tracking tools are clinical, multi-step, and demanding to use — a real barrier for anyone trying to log data while already dealing with flare-up symptoms like brain fog or low mood.
 
## Research
 
Design decisions were informed by user research interviews and personas developed for people managing Hashimoto's (see `research/` for full interview notes and personas). These conversations surfaced a recurring pain point: navigating multi-page, multi-step tools is genuinely difficult during a flare, when cognitive load is already high.
 
## Design
 
Two decisions came directly out of that research (see `design/` for wireframes and full design notes):
 
- **Progressive disclosure** — all logging happens on one home page, where users choose what to log and skip what doesn't apply that day, rather than navigating between separate pages per category.
- **A soft, muted color palette** — a deliberate departure from the bright, clinical look common in health-tracking apps.
Both choices are aimed at reducing cognitive load specifically for users logging data while symptomatic.
 
## Build
 
Built with HTML, CSS, and a Flask + SQLite backend (server-rendered Jinja2 templates over the existing HTML/CSS). Deployed at concoctory.com/hashitracker/. Features include daily symptom and lifestyle-factor logging, and pattern analysis to help identify flare-up triggers.
 
## Testing
 
Accessibility was verified throughout — HTML/CSS was checked against accessibility standards, and a contrast checker confirmed the muted color palette meets readability requirements despite its soft tones.
 
