from pathlib import Path
from collections.abc import Iterator

def read_log_file(file_path: str) -> Iterator[str]:
    """
    Read a log file line by line.

    Args:
        file_path: Path to the log file.

    Yields:
        Individual log lines without trailing newline characters.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Log file {file_path} does not exist.")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    with path.open("r", encoding="utf-8", errors="replace") as file:
        for line in file:
            line = line.rstrip("\r\n")

            if line:
                yield line
