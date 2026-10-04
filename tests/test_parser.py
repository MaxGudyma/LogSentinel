from logsentinel.parser.auth_parser import parse_auth_log

def test_failed_login():
    line = (
        "Oct 3 20:15:32 server sshd[1234]: "
        "Failed password for invalid user admin "
        "from 192.168.1.50 port 54321 ssh2"
    )

    result = parse_auth_log(line)

    assert result["event_type"] == "failed_login"
    assert result["username"] == "admin"
    assert result["ip_address"] == "192.168.1.50"
    assert result["port"] == 54321


def test_successful_login():
    line = (
        "Oct 3 20:16:45 server sshd[1236]: "
        "Accepted password for maksym "
        "from 192.168.1.20 port 54323 ssh2"
    )

    result = parse_auth_log(line)

    assert result["event_type"] == "successful_login"
    assert result["username"] == "maksym"

def test_unsupported_log():
    line = "This is not an SSH authentication log"

    assert parse_auth_log(line) is None