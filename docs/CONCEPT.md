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
- **Platform:** React Native / Expo (mobile-first, cross-platform)
- **Storage:** Local only for MVP (SQLite on device)
- **Auth:** Local username + recovery key, no backend
- **Note:** No cloud sync for MVP — data stays on device

## Version Roadmap
- **V1** — Symptom, lifestyle, dietary, and medication logging with PDF report generation
- **V2** — Data visualization, pattern tracking, trend analysis
- **V3** — Optional cloud sync, multi-device support