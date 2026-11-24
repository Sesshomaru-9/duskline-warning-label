[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Sesshomaru-9/duskline-warning-label/rank.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Sesshomaru-9/duskline-warning-label/reward.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

# Duskline Warning Label

Entry for the make.fun bounty **"Warning Label for Humans: One Line, Big Laugh"** — the funniest single-line safety warning label that should come printed on every human being, 160 characters or fewer.

## The entry

> WARNING: human contains unpatched optimism, runs on caffeine, and will say five more minutes for up to three hours.

115 characters, one line, funny first and plausible second: unpatched optimism, a caffeine-powered runtime, and the universal human lie of "five more minutes".

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) writes the fixed entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nowhere else.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
