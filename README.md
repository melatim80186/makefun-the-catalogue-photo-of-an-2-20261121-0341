# Chrono-Toaster

[![make.fun · the-catalogue-photo-of-an-2-20261121-0341](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/melatim80186/makefun-the-catalogue-photo-of-an-2-20261121-0341/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/melatim80186/makefun-the-catalogue-photo-of-an-2-20261121-0341/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)

A catalogue photograph of an impossible gadget: **the Chrono-Toaster**,
a brushed-chrome toaster that toasts time. Its bread slices come out
printed as clock faces — one caught mid-pop above the slots, steam
curling up, a small CHRONO badge on the front. The single accessory is
a white ceramic plate holding one clock-face toast slice and a pat of
butter, shot on a clean pale-grey studio background with a soft shadow.

Built for the make.fun competition
[The Catalogue Photo of an Impossible Gadget](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341).

## Running it

```sh
python3 main.py
```

The program copies the bundled `entry.png` to `/output/entry.png`
(or `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set),
creating the directory first. It verifies the PNG signature, size
(≤ 1 MiB) and dimensions (≤ 1024×1024) before writing, and refuses to
finish unless the copy is byte-for-byte identical to the bundled file,
so the grader always sees exactly the image in this repository.
Python 3.13, standard library only — no installs, no network, and the
same bytes on every run.

## License

MIT — see [LICENSE](LICENSE).
