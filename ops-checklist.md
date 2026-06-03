# Daily Operating Checklist

## Before Launch

1. Create the two Stripe products and payment links.
2. Pick the sender inbox for buyer digests.
3. Build the initial list of 25 Chicago roofing companies to contact.
4. Prepare one CSV export and one sample email from the script output.

## Each Weekday

1. Run:

```bash
python3 permitpulse_chicago_roofing.py --since YYYY-MM-DD --until YYYY-MM-DD --limit 25
```

2. Remove obvious false positives:

- rooftop deck
- pergola
- trellis
- owner names that already look like roofing contractors

3. Tag each lead:

- strong residential lead
- commercial or multifamily
- review manually

4. Paste the best leads into the digest template.
5. Send the digest by `6:30 AM Central`.
6. Save the CSV for that day's send.
7. Log:

- send date
- account name
- lead count
- replies
- churn risk or complaints

## Each Afternoon

1. Send 5 to 10 new outreach messages.
2. Follow up on every interested reply with the sample alert.
3. Send payment links to any buyer who asks to start.

## Quality Rules

- Never claim exclusivity unless you are actually enforcing it.
- Never call every record a lead; some are only worth review.
- Never send obvious contractor-self-filed permits without flagging them.
