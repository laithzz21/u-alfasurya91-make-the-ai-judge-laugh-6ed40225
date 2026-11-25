# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/laithzz21/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/laithzz21/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [make.fun](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225) bounty **"Make the AI Judge Laugh"**: one joke about office life, one line, under 200 characters.

## Entry

> My boss says we're a family here — which explains why I can't choose my coworkers, can't leave, and Dad decides my allowance.

125 characters, one line.

## Why it works

It opens on the most overused line in office life — "we're a family here" — then takes it literally: if it really is a family, you can't choose your coworkers, you can't leave, and Dad (the boss) decides your allowance (your salary). True to office life, with a surprising literal-family turn, in one tight line.

## What this does

`main.py` (Python 3, stdlib only, deterministic — no network, clock, or randomness) validates the entry against every rule in the brief (one line, under 200 characters, plays on office life, contains a surprising turn) and prints it to stdout. It also writes it to `entry.txt` in the output directory named by `$MAKEFUN_OUTPUT_DIR` or `$MAKEFUN_OUTPUT` when either is set, otherwise a per-entry directory under `/tmp`. It never writes into the repository directory, so it runs cleanly from a read-only checkout.

## How to run

```sh
python3 main.py
# prints the entry, writes entry.txt to /tmp/sweep28-u-alfasurya91-make-the-ai-judge-laugh-6ed40225/
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT=/tmp/u-alfasurya91-make-the-ai-judge-laugh-6ed40225-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225) — enter bounties, win rewards.
