#!/usr/bin/env python3
"""Chrono-Toaster — The Catalogue Photo of an Impossible Gadget.

Entry program for make.fun competition
the-catalogue-photo-of-an-2-20261121-0341.

The entry is a single studio catalogue photograph of an impossible
gadget: a brushed-chrome toaster that toasts time itself, its slots
popping up slices of bread printed as clock faces, with one plate of
clock-face toast and butter as the single accessory.

This program writes the photograph to /output/entry.png. It is fully
deterministic: it copies the bundled image bytes verbatim, so repeated
runs produce byte-identical output. It uses only the Python standard
library and makes no network requests.
"""

import os
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SOURCE = os.path.join(_HERE, "entry.png")
_DEST = "/output/entry.png"


def main() -> int:
    if not os.path.isfile(_SOURCE):
        print(f"missing bundled image: {_SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(_DEST), exist_ok=True)
    shutil.copyfile(_SOURCE, _DEST)
    size = os.path.getsize(_DEST)
    print(f"wrote {_DEST} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
