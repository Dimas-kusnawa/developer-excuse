#!/usr/bin/env python3
"""Write one funny excuse a developer gives when code breaks in production.

First-person developer voice, one specific failure, and a reveal:
the thing that broke production was the fix itself.
"""

import os

LINE = "I fixed the bug we'd all been working around for two years, and production went down — turns out the workaround was the product."
# The twist a developer recognises: the fix is what broke it.
# Everyone knew the bug, nobody touched it, and the workaround quietly became the product.


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE == LINE.strip(), "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
