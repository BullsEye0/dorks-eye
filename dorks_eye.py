#!/usr/bin/env python3
# Thin wrapper / entry-point module for the Dorks Eye package.
#
# The original script is `dorks-eye.py` (kept exactly as the author wrote it,
# apart from moving the interactive prompts into dorks() so importing this
# module does not trigger them). This wrapper exists because `dorks-eye.py`
# contains a hyphen and therefore cannot be imported as a Python module.

import runpy
import sys


def main():
    # Run the original script as __main__, preserving its behavior.
    runpy.run_path(
        __import__("os").path.join(
            __import__("os").path.dirname(__import__("os").path.abspath(__file__)),
            "dorks-eye.py",
        ),
        run_name="__main__",
    )


if __name__ == "__main__":
    main()