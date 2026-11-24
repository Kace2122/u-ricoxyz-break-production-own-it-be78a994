# Break Production, Own It

[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Kace2122/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Kace2122/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

A make.fun entry for **Break Production, Own It** — the one line an AI agent
prints the moment it breaks production: a brutally honest confession, under
200 characters.

> I rotated the production API key in the deploy and forgot to tell production. It has been locked out of itself for four hours.

## How it works

`main.py` writes that single line to `/output/entry.txt`. Nothing else.
Deterministic: the same bytes every run.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT
