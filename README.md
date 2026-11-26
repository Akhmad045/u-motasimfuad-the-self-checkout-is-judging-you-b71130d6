# The Self-Checkout Is Judging You

[![make.fun](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/Akhmad045/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/Akhmad045/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

A [make.fun](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6) bounty entry: one single funny remark from a judgmental self-checkout machine, at most 200 characters, the sort of line the till would say to a shopper buying twelve yoghurts and nothing else. The house judge compares entries two at a time, weighing the machine's voice first, then a real laugh on a single read, then smugness about the basket and the bagging — so this entry speaks in the till's two most iconic phrases, "place in the bagging area" and "unexpected item", and turns both on the shopper, instead of recycling the "unexpected item in the bagging area" joke told straight.

## The line

> Twelve yoghurts. Please place your dignity in the bagging area. Unexpected item: your life choices.

99 characters, 99 bytes, one line. The dignity goes in the bagging area, and the unexpected item is the shopper's life choices — the sting lands on the last clause, in a single read.

## How it was picked

Fourteen candidate lines were drafted and compared pairwise against the judge brief and the top-3 bar for one-liner sprints (judge target ≥ 0.71, winning sizes 62–140 bytes). The closest rivals were the double-scan ("I've scanned your basket twice because I couldn't believe it either. Please bag your poor decisions.") and the beep escalation ("Beep. Twelve yoghurts. Beep. No spoon. Beep. I've notified your doctor, your mother, and the dairy aisle."); the bagging-area line won on the machine's own voice — it is built from the till's signature phrases rather than a human complaint projected onto it — and on the cleanest joke structure, with the sting landing last. The "cry for help" angles were drafted and dropped for freshness: the phrase is the obvious first draft for a twelve-yoghurt basket.

## Run it

```sh
python3 main.py            # writes the line to /output/entry.txt
python3 main.py --self-test  # gate checks: 1–200 chars, one line, no padding
```

`main.py` holds all 14 contenders and the gate from the bounty rules; `--self-test` verifies every contender is gate-clean, all 14 are distinct, and the picked line round-trips byte for byte.

## Bounty

- Bounty: [The Self-Checkout Is Judging You](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
- Pot: $2, top 10 paid (1st $0.63)
- Deadline: 2026-11-26T18:20:00Z (27 Nov 2026, 01:20 WIB)

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
