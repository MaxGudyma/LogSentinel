# LogSentinel 🔐

**Python-based Security Log Analyzer for Threat Detection and Security Monitoring**

LogSentinel is a modular security log analysis tool designed to identify suspicious activity, detect potential security threats, and generate structured reports from system authentication logs.

The project aims to demonstrate practical cybersecurity skills, including log analysis, threat detection, Python development, and security automation.

**Project Status: In Development**

## 🎯 Project Objectives
- Analyze Linux authentication logs and extract relevant security events.
- Detect suspicious login activity using configurable detection rules.
- Identify potential brute-force attacks and unusual authentication patterns.
- Generate structured security alerts with severity levels.
- Store and organize security events for further investigation.
- Produce readable reports for security analysis.

## ✨ Planned Features
- **Log Parsing:** Extract structured information from Linux authentication logs.
- **Threat Detection:** Identify suspicious behavior using rule-based detection.
- **Brute-Force Detection:** Detect repeated failed login attempts within configurable time windows.
- **IP Analysis:** Track authentication activity by source IP address.
- **Alert Management:** Classify detected events by severity.
- **Data storage:** Store events and alerts using SQLite.
- **Report Generation:** Export analysis results in JSON and CSV formats.
- **Command-Line Interface:** Run analyses and customize detection settings directly from the terminal.
- **Automated Testing:** Validate application functionality using unit tests.

## 🛠️ Tech Stack

| Technology | Purpose |
| :---: | :---: |
| Python 3.12+ | Core application development |
| SQLite | Event and alert storage |
| pytest | Automated testing |
| Rich | Terminal output and visualizatoin |
| Git | Version control |
| GitHub Actions | Continuous integration |

## 🏗️ Project Architecture

The applicatoin follows a modular architecture, separating log ingestion, parsing, event processing, threat detection, storage, and reporting.

```
LogSentinel/
│
├── src/
│   └── logsentinel/
│       ├── input/          # Log file ingestion
│       ├── parser/         # Log parsing
│       ├── processor/      # Event normalization
│       ├── detection/      # Threat detection engine
│       ├── storage/        # Database operations
│       ├── alerts/         # Alert management
│       ├── reports/        # Report generation
│       ├── cli.py          # Command-line interface
│       └── main.py         # Application entry point
│
├── tests/                  # Automated tests
├── data/                   # Sample log files
├── reports/                # Generated reports
├── docs/                   # Project documentation
│
├── requirements.txt
├── README.md
└── LICENSE
```

## 🔍 Detection Rules

The initial version is planned to include the following detection rules:

| Detection Rule | Description | Severity |
| :---: | :---: | :---: |
| Brute-Force Detection | Multiple failed login attempts from a single IP address within a defined time window | High |
| Multiple Failed Logins | Repeated failed authentication attempts targeting the same username | Medium |
| Successful authentication following multiple failed attempts | High |
| Invalid User Login | Authentication attempts involving non-existent usernames | Low |

Detection thresholds and time windows will be configurable.

Alerts indicate potentially suspicious activity and require further investigation. They do not automatically confirm malicious behavior.

## 🚀 Getting Started
**Prerequisites**
- Python 3.12 or newer
- Git
- A Linux authentication log file or the provided sample data

### Installation

**1. Clone the repository**
```
git clone https://github.com/MaxGudyma/LogSentinel.git
```
**2. Create a virtual environment**
```
python -m venv .vent
```
**3. Activate the virtual environment**

Linux / macOS:

```
source .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```
**4. Install dependencies**
```
pip install -r requirements.txt
```

>Installation and usage instructions will be updated as the application becomes functional.

## 📊 Example Output

The following is an illustrative example of the type of output LogSentinel aims to generate.
```
================================================== LOG SENTINEL SECURITY ANALYSIS ==================================================
[INFO] Log file: sample_auth.log
[INFO] Total events analyzed: 1250

---------------- SECURITY SUMMARY ----------------
[HIGH] Brute-force activity detected
       Source IP: 192.168.1.50
       Failed attempts: 12

[MEDIUM] Multiple failed logins
         Username: admin
         Failed attempts: 5

[LOW] Invalid user login
      Username: test
      Source IP: 192.168.1.75

---------------- ANALYSIS SUMMARY ----------------

Total events: 1250
Suspicious events: 18
Alerts generated: 3

==================================================
```

_Example output only. Detection and reporting functionality is not yet implemented._

## 🧪 Testing

The project will use ``` pytest ``` for automated testing.

Planned test coverage includes:

- Log parsing and event extraction.
- Invalid and malformed log entries.
- Detection rule accuracy.
- Event processing and normalization.
- Database operations.
- Report generation.

Run the test suite with:

pytest

## 🗺️ Development Roadmap

- [x] Initialize project structure and development environment
- [x] Implement log file ingestion
- [ ] Develop Linux authentication log parser
- [ ] Create a standardized security event model
- [ ] Implement the rule-based detection engine
- [ ] Add brute-force detection
- [ ] Implement alert classification
- [ ] Integrate SQLite storage
- [ ] Develop JSON and CSV report generation
- [ ] Build the command-line interface
- [ ] Add automated tests and CI
- [ ] Complete documentation and project demonstration

## 🔒 Security and Ethical Use

LogSentinel is intended for educational purposes, defensive security research, and authorized security monitoring.

- Analyze only logs you are authorized to access.
- Use synthetic or anonymized data when sharing examples.
- Avoid publishing sensitive information, credentials, or personally identifiable information.
- Treat detection results as indicators for investigation rather than definitive evidence of an attack.

## 👨‍💻 About

LogSentinel is an independent cybersecurity learning project developed to strengthen practical skills in Python programming, Linux security, log analysis, and threat detection.

The project is developed as part of my ongoing learning journey in cybersecurity.

## 📄 License

This project is intended to be released under the MIT License. See the ```LICENSE``` file for details.
