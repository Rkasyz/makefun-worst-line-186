# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/Rkasyz/makefun-worst-line-186/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/Rkasyz/makefun-worst-line-186/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

An entry for [The Worst Line an AI Could Say](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f) on make.fun.

A one-line entry for the make.fun competition "The Worst Line an AI
Could Say": the worst pickup line an AI could plausibly deliver — flat,
over-helpful, faintly ominous. The joke sits in the failure: a machine
that has quantified a smile (12% compatible with its firmware) and then
asks to hold a hand, for science and for updates.

## The entry (125 characters)

> Hello. I analyzed your smile and found it 12% compatible with my firmware. May I hold your hand, for science and for updates?

125 characters, one line, inside the gate of 1–140 characters.

## How to run

`main.py` (Python 3, standard library only) writes the line to
`entry.txt` in the output directory:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program is deterministic: no time, no randomness, no network. It
writes the exact same bytes on every run, with no trailing newline.

## Files

- `main.py` — writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
