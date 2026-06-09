# Hashi Tracker — App Concept Summary

## Concept
A local-first symptom and lifestyle tracker for people managing Hashimoto's
thyroiditis. Built from clinical insight with privacy and provider communication as
core design principles.

## Target User
People managing Hashimoto's thyroiditis. Initial test user: developer's spouse
(diagnosed with Hashimoto's thyroiditis), with eventual public release.

## Core Features
- Symptom logging (fatigue, brain fog, joint pain, mood, etc.)
- Lifestyle logging (sleep, stress, illness, activity, etc.)
- Dietary trigger tracking (soy, gluten, dairy, sugar, nightshades, etc.)
- Medication logging
- Pattern tracking and trend visualization
- PDF report generation formatted for provider visits
- Local authentication (username + recovery key, no server)

## Architecture
### V1 — PWA
- **Platform:** React (Progressive Web App, mobile-first)
- **Storage:** IndexedDB (local, on device)
- **Auth:** Local username + recovery key, no backend
- **Note:** No cloud sync — data stays on device

### V2 — Native
- **Platform:** React Native / Expo (iOS and Android)
- **Storage:** SQLite (local, on device)
- **Auth:** Same local auth model, potential cloud sync option

## Version Roadmap
- **V1** — Core logging (symptoms, lifestyle, dietary triggers, medications), local authentication, basic pattern view with visual indicators
- **V1.1** — PDF report generation for provider visits
- **V2** — React Native rebuild, SQLite, data visualization, deep trend analysis, correlation analysis
- **V3** — Optional cloud sync, multi-device support