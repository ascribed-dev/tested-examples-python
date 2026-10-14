"""One test for each example in examples/: run it, and compare what it prints
with the output file beside it, which the docs show too. A new example and its
.out.txt file are tested with no change here."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = sorted(Path("examples").glob("*.py"))


@pytest.mark.parametrize("example", EXAMPLES, ids=lambda path: path.name)
def test_prints_its_output_file(example: Path) -> None:
    printed = subprocess.run(
        [sys.executable, str(example)],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    # Reading in text mode reads a Windows checkout's CRLF as LF.
    expected = example.with_suffix(".out.txt").read_text(encoding="utf-8")
    assert printed == expected
