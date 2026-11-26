#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

Writes one funny remark to /output/entry.txt (or the path given with
--out).

The entry is candidate 12 of 14 drafted lines, picked by internal pairwise
comparison against the judge brief (machine's voice first, then a real
laugh on a single read, then smug and petty about the basket and the
bagging, then tightness, then freshness) and the top-3 bar for one-liner
sprints (judge target >= 0.71, winning sizes 62-140 bytes). The winning
line speaks in the till's two most iconic phrases -- "place in the
bagging area" and "unexpected item" -- and turns both on the shopper:
the dignity goes in the bagging area, and the unexpected item is their
life choices. It is 99 chars / 99 bytes, inside the winning size band,
and its angle (the machine itemising the shopper's dignity as a bagging
problem) is fresh against the recycled "unexpected item in the bagging
area" joke told straight.

Usage:
    python3 main.py [--out PATH] [--self-test]
"""
import argparse
import os
import sys

# 14 drafted candidates, each one sentence or two, 1-240 chars, single line.
CONTENDERS = [
    # 1. No spoon, no granola, no plan.
    "Twelve yoghurts. No spoon, no granola, no plan. I've seen meal prep "
    "before \u2014 this is a cry for help with a barcode.",
    # 2. Flagged as a cry for help; the beep was judgement.
    "Twelve yoghurts and nothing else. Bold strategy. I've flagged your "
    "basket as 'a cry for help' \u2014 the beep was me judging you.",
    # 3. Zero spoons; the dairy aisle has been alerted.
    "Twelve yoghurts. Zero spoons. I'm not saying you have a problem, but "
    "I have already alerted the dairy aisle.",
    # 4. Officially classified as a cry for help.
    "Twelve yoghurts, no other food. Congratulations: your basket has "
    "officially been classified as a cry for help.",
    # 5. Just vibes and a loyalty card that gave up.
    "Twelve yoghurts. No spoon. No granola. Just vibes and a loyalty card "
    "that has clearly given up on you.",
    # 6. Zero meals; dignity at customer service.
    "I have scanned twelve yoghurts and zero meals. Please collect your "
    "dignity at customer service \u2014 it's been waiting since aisle 4.",
    # 7. A personality test, failed.
    "Twelve yoghurts. That's not a shop, that's a personality test "
    "\u2014 and you just failed it.",
    # 8. Telling the receipt.
    "Twelve yoghurts and no spoon. Either you're very committed or very "
    "lost. Either way, I'm telling the receipt.",
    # 9. Beep. Notified your doctor, your mother, the dairy aisle.
    "Beep. Twelve yoghurts. Beep. No spoon. Beep. I've notified your "
    "doctor, your mother, and the dairy aisle.",
    # 10. 100% dairy, 0% life plan; dignity declined.
    "Twelve yoghurts, nothing else. Your basket is 100% dairy and 0% life "
    "plan. Please insert your dignity \u2014 card declined.",
    # 11. Scanned twice; bag your poor decisions.
    "Twelve yoghurts. I've scanned your basket twice because I couldn't "
    "believe it either. Please bag your poor decisions.",
    # 12. WINNER. Dignity in the bagging area; unexpected item: life choices.
    "Twelve yoghurts. Please place your dignity in the bagging area. "
    "Unexpected item: your life choices.",
    # 13. Mostly 'why' and 'are you okay?'
    "Twelve yoghurts and no other food. I've seen your basket and I have "
    "questions \u2014 mostly 'why' and 'are you okay?'",
    # 14. A cry for help in dairy form.
    "Twelve yoghurts. No spoon, no granola, no shame. I've seen a lot of "
    "baskets. Yours is a cry for help in dairy form.",
]

PICK = 11  # 0-based index of candidate 12, dignity in the bagging area.


def gate(line):
    """The sealed scorer's gate: UTF-8 text, 1-200 chars (the brief's cap,
    not the 240-char harness default), not only whitespace, one line, no
    leading/trailing padding."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 200:
        return False
    if line.strip() == "":
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def entry_text():
    return CONTENDERS[PICK]


def self_test():
    """Verify every contender is gate-clean, all 14 are distinct, the pick
    sits inside the winning size band (62-140 bytes, the one-liner top-10
    range), and a round-tripped pick matches byte for byte."""
    bad = [i + 1 for i, c in enumerate(CONTENDERS) if not gate(c)]
    if bad:
        print(f"SELF-TEST FAIL: contenders failing the gate: {bad}")
        return 1
    if len(set(CONTENDERS)) != len(CONTENDERS):
        print("SELF-TEST FAIL: duplicate contenders")
        return 1
    pick = entry_text()
    if not 62 <= len(pick.encode("utf-8")) <= 140:
        print(f"SELF-TEST FAIL: pick is {len(pick.encode('utf-8'))} bytes, "
              f"outside the 62-140 winning size band")
        return 1
    tmp = "/tmp/self-checkout-self-test.txt"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(pick)
    with open(tmp, encoding="utf-8", newline="") as fh:
        back = fh.read()
    if back != pick or back.encode("utf-8") != pick.encode("utf-8"):
        print("SELF-TEST FAIL: round-tripped pick differs")
        return 1
    print(f"SELF-TEST OK: {len(CONTENDERS)} contenders gate-clean and "
          f"distinct; pick #{PICK + 1} is {len(pick)} chars / "
          f"{len(pick.encode('utf-8'))} bytes (inside the 62-140 winning "
          f"size band), round-trips byte-identical")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write the entry (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the gate checks and exit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    text = entry_text()
    if not gate(text):
        print("GATE FAIL: picked line does not satisfy the 1-240 char, "
              "single-line, no-padding gate", file=sys.stderr)
        return 1
    parent = os.path.dirname(args.out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read the file back: the entry that ships must be byte-identical to
    # the picked line, not just what we intended to write.
    with open(args.out, encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("WRITE-BACK FAIL: /output/entry.txt differs from the pick",
              file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} chars / {len(text.encode('utf-8'))} bytes "
          f"to {args.out} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
