# PermitPulse

PermitPulse is a narrow paid lead-alert service for home-service businesses using public building-permit data.

Week-1 launch wedge:

- City: Chicago
- Buyer: roofing companies
- Offer: weekday roof-replacement permit digest for Chicago

Files in this repo:

- `permitpulse_chicago_roofing.py`: pulls fresh Chicago roofing permits and formats a buyer-ready digest
- `index.html`: landing page for the first pilot
- `styles.css`: landing page styles
- `ORCA-SPEC.md`: launch decision, offer, pricing, and rationale
- `ORCA-PLAN.md`: operating plan and immediate execution path
- `sample-alert.md`: ready-to-send example digest
- `outreach.md`: cold outreach assets
- `ops-checklist.md`: daily operating checklist

Run the digest generator:

```bash
python3 permitpulse_chicago_roofing.py --since 2026-05-25 --until 2026-06-01 --limit 10
```

Export CSV:

```bash
python3 permitpulse_chicago_roofing.py --since 2026-05-25 --until 2026-06-01 --format csv > chicago-roofing-leads.csv
```

Current business judgment:

- The first paid pilot is launch-ready with a manual payment path.
- Linear is currently blocked by `401: Reauthentication required`, so project and issue creation still need to be backfilled there once access is restored.
