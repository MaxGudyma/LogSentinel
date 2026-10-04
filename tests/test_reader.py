from pathlib import Path

import pytest

from logsentinel.input.reader import read_log_file

def test_read_log_file(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "First event\nSecond event",
        encoding="utf-8"
    )

def test_empty_lines_are_skipped(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "First event\n\nSecond event\n",
        encoding="utf-8"
    )

    result = list(read_log_file(str(log_file)))

    assert result == ["First event", "Second event"]

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        list(read_log_file("nonexistent.log"))