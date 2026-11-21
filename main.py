"""Chrono-Toaster — catalogue photograph of an impossible gadget.

Entry for the make.fun competition
"the-catalogue-photo-of-an-2-20261121-0341" (The Catalogue Photo of an
Impossible Gadget).

The program writes one image to /output/entry.png: a studio catalogue
photograph of a brushed-chrome toaster that toasts time — its bread
slices are printed as clock faces, one caught mid-pop above the slots,
steam curling up, a small CHRONO badge on the front. The single
accessory is a white ceramic plate holding one clock-face toast slice
and a pat of butter, on a clean pale-grey studio background.

The image is bundled in this repository as entry.png. This program
copies it byte-for-byte to the output path, so repeated runs produce
identical bytes. Python 3.13, standard library only — no installs,
no network.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Return (width, height) from a PNG's IHDR chunk."""
    if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file (bad signature)")
    if data[12:16] != b"IHDR":
        raise ValueError("not a PNG file (missing IHDR)")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.png"

    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    width, height = png_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"entry.png is {width}x{height}, over the 1024x1024 cap",
              file=sys.stderr)
        return 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)

    written = out_path.read_bytes()
    if written != data:
        print("output differs from bundled entry.png", file=sys.stderr)
        return 1
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {out_path} ({width}x{height}, {len(written)} bytes, "
          f"sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
