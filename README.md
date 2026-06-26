# **PermitPulse is a demo of the capabilities of [ORCA Framework](https://github.com/henryvn27/orca-framework)**

## Writeup:
I wanted to test [ORCA](https://github.com/henryvn27/orca-framework) by giving it a real business task and seeing how far it could get autonomously.

I told Codex to identify and make a business that could feasibly bring in profit that would take <1 week to build. It came up with PermitPulse, a paid lead-alert service for contractors using public info. ORCA then defined the next step: pick the best first city and trade, define the smallest viable offer, build the week-1 business path, create all the launch assets, and keep going until it either hits a real blocker or gets the business to first-outreach-ready.

It ended up choosing Chicago roofing as the wedge, set the offer as a weekday roofing-permit digest, priced it at $199 setup + $349/mo, built the landing page, sample alert, outreach packet, ops checklist, legal pages, GitHub repo, Notion project structure, and a working script to pull and format the permit data.

Obviously, this is just a test, and I haven't deployed it, so it hasn't made any profit, but it is a clear testament to the functionality of ORCA. 

ORCA can work at any involvement layer, from someone who wants to learn how to develop with AI and go step by step, to someone who just wants to follow the troupe: "Claude makes me a $1M business, no mistakes," and come back the next morning to something real.

**Read more [here](https://www.linkedin.com/embed/feed/update/urn:li:share:7467953199941861376)**


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
