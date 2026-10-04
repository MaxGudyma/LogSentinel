import re

AUTH_LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) "
    r"(?P<hostname>\S+) "
    r"(?P<service>sshd)\[(?P<pid>\d+)\]: "
    r"(?P<message>.*)$"
)

def parse_auth_log(line: str) -> dict | None:
    """
    Parse a Linux SSH authentication log entry.

    Returns a dictionary with event details,
    or None if the line is unsupported or invalid.
    """
    match = AUTH_LOG_PATTERN.match(line)

    if not match:
        return None

    data = match.groupdict()
    message = data.pop("message")

    data["pid"] = int(data["pid"])
    data["event_type"] = None
    data["username"] = None
    data["ip_address"] = None
    data["port"] = None

    failed = re.search(
        r"Failed password for (?:invalid user )?(\S+) "
        r"from (\d{1,3}(?:\.\d{1,3}){3}) port (\d+)",
        message
    )

    accepted = re.search(
        r"Accepted password for (\S+) "
        r"from (\d{1,3}(?:\.\d{1,3}){3}) port (\d+)",
        message
    )

    invalid_user = re.search(
        r"Invalid user (\S+) from "
        r"(\d{1,3}(?:\.\d{1,3}){3})",
        message
    )

    if failed:
        data["event_type"] = "failed_login"
        data["username"] = failed.group(1)
        data["ip_address"] = failed.group(2)
        data["port"] = int(failed.group(3))

    elif accepted:
        data["event_type"] = "successful_login"
        data["username"] = accepted.group(1)
        data["ip_address"] = accepted.group(2)
        data["port"] = int(accepted.group(3))

    elif invalid_user:
        data["event_type"] = "invalid_user"
        data["username"] = invalid_user.group(1)
        data["ip_address"] = invalid_user.group(2)

    else:
        return None

    return data