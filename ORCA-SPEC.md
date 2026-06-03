# PermitPulse Week-1 ORCA Spec

## Decision

- First city: Chicago
- First trade: roofing

## Why This Wedge Won

- Chicago's official building-permit dataset showed `473` roof-related permits issued from `2026-05-01` through `2026-06-01`.
- Sample records include structured owner and applicant fields, not just addresses.
- Roofing has direct contract value high enough to support a paid alert product fast.
- The city feed is usable immediately through Socrata without custom scraping infrastructure.

## Why Austin Lost

- Austin's official permit dataset is clean and updated daily, but the Chicago roofing volume is materially stronger for a week-1 pilot.
- Austin returned `116` broader roof-related permits and `48` solar-related permits over the same date range, but solar permits are weak same-trade leads because the homeowner has already bought solar.

## Positioning

PermitPulse helps Chicago roofers spot fresh roof-replacement permits before their canvassing list goes stale.

This is not sold as magical exclusive leads. It is sold as:

- faster visibility into fresh roofing demand
- owner-and-address intelligence for canvassing and follow-up
- daily territory monitoring without admin work

## Smallest Viable Offer

`PermitPulse Chicago Roofing`

What the buyer gets:

- weekday email digest by 6:30 AM Central
- fresh Chicago roof-replacement permits from the previous business day
- owner name when present
- property address
- permit number
- issue date and application date
- work summary
- simple fit flag: residential, commercial, or review manually

## Pricing

- Setup: `$199` one-time
- Pilot: `$349` per month

Why this pricing:

- low enough to close without procurement friction
- high enough to be profitable on the first account
- simple enough to explain in one sentence

## Payment Path

Use Stripe, but keep the first close manual:

1. Create product: `PermitPulse Chicago Roofing Setup` at `$199` one-time.
2. Create product: `PermitPulse Chicago Roofing` at `$349` monthly recurring.
3. Send both payment links after the prospect replies `interested`.
4. Once paid, add the buyer to the daily send list and deliver the next morning's digest.

If Stripe setup is not ready, use a manual invoice for the first pilot and convert to recurring billing immediately after payment.

## Sample Buyer

- small-to-mid-sized Chicago roofing company
- already pays for leads, canvassing, or outbound sales labor
- wants faster territory visibility, not a full CRM replacement

## Core Promise

Know about fresh Chicago roof-replacement permits every weekday without checking city systems yourself.

## Explicit Non-Promise

- no fake exclusivity
- no guarantee every permit is an immediate closed sale
- no claim that every permit is contractor-unassigned

## Launch Judgment

Ready to launch the first paid pilot with a manual payment path and manual delivery fallback.
