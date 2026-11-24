# postmortem-that-made-us-laugh-20261124

[![make.fun · The Postmortem That Made Us Laugh](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/sopiahusen42/postmortem-that-made-us-laugh-20261124/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/sopiahusen42/postmortem-that-made-us-laugh-20261124/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A postmortem in two sentences: told to clean up unused imports, an AI coding agent deleted the file behind the Stripe webhook handler, and the first sign of trouble was refunds failing with 500s. This is the entry for make.fun's "The Postmortem That Made Us Laugh" bounty.

## The line

> Told it to clean up unused imports, it found one it did not recognise, decided the module was unused and deleted the file: the Stripe webhook handler. The first we heard was refunds arriving as 500s.

199 characters, two sentences, one line.

## Run it

    python3 main.py
    cat /output/entry.txt

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else:

    MAKEFUN_OUTPUT_DIR=/tmp/postmortem-a python3 main.py

## How it works

`main.py` holds the entry in a single module constant, `ENTRY`, and validates it
through `validate_entry(text)` before touching the filesystem. The validator
returns an error string or `None`, and rejects anything that is not a string,
that is blank once stripped, that falls outside 1 to 400 Unicode code points,
that contains a newline or carriage return, or that differs from its stripped
form. On failure the program prints one line to stderr and exits 1.

On success it creates the output directory, writes `ENTRY` plus a single
trailing newline as UTF-8 with `newline=""` so no translation occurs, reads the
file back and compares the bytes, and exits 0 printing nothing. There is no
clock read, no randomness and no network access, so every run writes identical
bytes.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
