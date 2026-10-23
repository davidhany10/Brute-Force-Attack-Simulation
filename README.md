 
# 🔐 Python Brute Force Attack Demonstration

<p align="center">
  <img src="docs/images/banner.png" alt="Python Brute Force Attack Project Banner" width="100%">
</p>

<p align="center">
  A Python-based cybersecurity project demonstrating password-list generation and HTTP login testing in an educational lab context.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/HTTP-Requests-informational" alt="HTTP Requests">
  <img src="https://img.shields.io/badge/Concurrency-Threading-blueviolet" alt="Threading">
  <img src="https://img.shields.io/badge/Domain-Cybersecurity-red" alt="Cybersecurity">
</p>

---

## 📌 Overview

This project demonstrates how password lists and automated HTTP login requests can be used to study authentication security in an authorized testing environment.

The main Python script, `stealth_attack.py`, loads candidate passwords from a wordlist and submits HTTP POST requests to a configured login endpoint. It uses multiple threads, displays progress in the terminal, and records a matching candidate when the configured response condition is met.

The project also includes `generate_list.py`, which creates a sample password list for demonstration purposes.

## ✨ Project Components

### 1. HTTP Login Testing — `stealth_attack.py`

The main script includes:

- A configurable target URL, username, and form field names.
- Wordlist loading from a text file.
- Multiple worker threads for processing candidate passwords.
- HTTP POST requests using the `requests` library.
- Request timeouts and terminal progress messages.
- A response-based condition for identifying a potential match.
- Optional recording of a detected candidate in `cracked_log.txt`.

**Important:** The script's success condition is based on HTTP response indicators. A redirect alone does not prove authentication succeeded; the response logic should be validated against a controlled test application.

### 2. Wordlist Generation — `generate_list.py`

This script creates a sample file named `passwords.txt`.

Its current configuration includes:

- A list of common base words.
- Random numeric suffixes for generated entries.
- A configurable number of output lines.
- A designated position for a demonstration password.

The generated list is intended for controlled demonstrations, not for use against accounts or systems without permission.

### 3. Password List — `passwords.txt`

A text file containing candidate strings, with one entry per line. The main script reads this file when initializing the wordlist queue.

### 4. Sample Data — `user_data.txt`

The archive also includes a sample username and a field labelled as an encrypted password. The file does not establish that the value is a securely encrypted password or that the main script uses it.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| `requests` | HTTP communication |
| `threading` | Concurrent request processing |
| `queue.Queue` | Candidate-password queue |
| `random` | Selecting sample user-agent strings and generating demo entries |
| Text files | Wordlist and sample data storage |

## 📂 Project Structure

```text
bruteforce-attack/
│
├── stealth_attack.py
├── generate_list.py
├── passwords.txt
├── user_data.txt
│
├── docs/
│   └── images/
│       └── banner.png
│
└── README.md
```

The supplied archive also contains a `tools/sqlmap/` directory with a separate copy of sqlmap and its supporting files. That third-party tool is distinct from the main Python scripts described above.

## ⚙️ Installation

### Prerequisites

- Python 3
- pip
- A controlled lab application or a system for which you have explicit authorization to test authentication

### 1. Create a Virtual Environment

**Windows:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Linux or macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install the Dependency

The main script requires the Python `requests` package:

```bash
python -m pip install requests
```

## 🧪 Educational Workflow

A controlled demonstration can be organized into these stages:

1. Configure an isolated test login application with test-only accounts.
2. Generate a small sample wordlist using `generate_list.py`.
3. Configure the script for the authorized lab endpoint and its actual form fields.
4. Run the experiment within the lab's permitted request limits.
5. Compare the tool's reported result with the test application's authentication logs.
6. Document response behavior, request failures, and any false positives.

Do not run automated password attempts against third-party systems without explicit authorization.

## 🔍 Security Concepts Demonstrated

- Wordlist-based password guessing.
- HTTP form submission and response handling.
- Concurrent request processing.
- Candidate-list generation.
- Authentication failure and success indicators.
- The importance of reliable success detection and controlled testing.

## ⚠️ Current Limitations

- The script is configured with a specific demo login URL and form-field names.
- It does not implement a general-purpose protocol framework for SSH, FTP, or Telnet.
- Its response-based success detection may produce false positives.
- Exceptions during requests are silently ignored, limiting diagnostic information.
- The stop flag is shared across threads without an explicit synchronization mechanism.
- The included wordlist generator uses predictable base words and numeric suffixes.
- No verified performance or accuracy benchmark is included in the supplied files.

## 🔐 Defensive Recommendations

Authentication systems can reduce password-guessing risk through:

- Rate limiting and request throttling.
- Progressive delays after repeated failures.
- Multi-factor authentication.
- Monitoring for repeated login failures.
- Strong password policies and breached-password screening.
- Secure session handling and consistent authentication responses.

## 🚀 Future Improvements

- Add structured logging and clearer error handling.
- Improve test coverage using a local mock authentication service.
- Validate successful authentication using application-specific evidence.
- Add configurable concurrency and request limits for authorized testing.
- Separate configuration from source code.
- Document repeatable lab scenarios and expected outcomes.
- Add unit tests for wordlist parsing and response evaluation.

## ⚖️ Responsible Use

This project is intended for cybersecurity education and authorized testing only. Do not use it to access accounts, services, or systems without permission. Follow applicable laws, testing agreements, and the rules of the environment being assessed.

## 👨‍💻 Author

**David Hany**

Computer Science & Artificial Intelligence

GitHub: [@davidhany10](https://github.com/davidhany10)

---

<p align="center">
  <strong>Understand the Attack. Strengthen the Defense.</strong>
</p>
