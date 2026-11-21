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
import struct
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SOURCE = os.path.join(_HERE, "entry.png")
_DEST = "/output/entry.png"
_MAX_BYTES = 1_048_576
_PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _png_dimensions(path: str) -> tuple[int, int]:
    """Read width/height from a PNG's IHDR chunk (stdlib only)."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != _PNG_SIGNATURE or header[12:16] != b"IHDR":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    if not os.path.isfile(_SOURCE):
        print(f"missing bundled image: {_SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(_DEST), exist_ok=True)
    shutil.copyfile(_SOURCE, _DEST)
    size = os.path.getsize(_DEST)
    if size > _MAX_BYTES:
        print(f"output too large: {size} bytes > {_MAX_BYTES}", file=sys.stderr)
        return 1
    width, height = _png_dimensions(_DEST)
    if width > 1024 or height > 1024:
        print(f"output too big: {width}x{height}", file=sys.stderr)
        return 1
    print(f"wrote {_DEST} ({size} bytes, {width}x{height} PNG)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
