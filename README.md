## UUID Toolkit

A professional, cross‑platform command‑line utility for generating, validating, formatting, and inspecting UUIDs. Designed for reliability, clarity, and operational consistency across multiple environments.

## Overview

The UUID Toolkit provides a unified interface for interacting with Universally Unique Identifiers (UUIDs). It includes commands for generating various UUID versions, validating existing UUID strings, converting formats, and retrieving metadata. The tool is built with clean, maintainable architecture and is suitable for enterprise‑grade workflows.


## Features

* Generate UUIDs (v1, v3, v4, v5)

* Validate and inspect UUID strings

* Convert UUID formats (uppercase, lowercase, URN)

* Batch generation

* Deterministic namespace‑based UUID creation

* Fully cross‑platform (Linux, macOS, Windows)

## Installation

**1. Requirements**

Ensure the following components are installed:

* Python 3.8+

* pip (Python package manager)

Recommended optional packages:
              
* virtualenv (for isolated environments)



**2. Installation on Linux / macOS**

* Debian/Ubuntu:
```
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/yourname/uuid-toolkit.git
cd uuid-toolkit
python3 uuid-toolkit.py v4
```

* Fedora / RHEL: 
```
sudo dnf install python3 python3-pip git -y
git clone https://github.com/yourname/uuid-toolkit.git
cd uuid-toolkit
python3 uuid-toolkit.py v4
```

* Arch / Manjaro:
```
sudo pacman -S python python-pip git
git clone https://github.com/yourname/uuid-toolkit.git
cd uuid-toolkit
python uuid-toolkit.py v4
```
  
* macOS Homebrew:
```
brew install python git
git clone https://github.com/yourname/uuid-toolkit.git
cd uuid-toolkit
python3 uuid-toolkit.py v4
```

* Android:
```
pkg update
pkg install python git -y
git clone https://github.com/yourname/uuid-toolkit.git
cd uuid-toolkit
python uuid-toolkit.py v4
```

* Windows (PowerShell):
> Install Python from [python.org](https://python.org)
```
git clone https://github.com/yourname/uuid-toolkit.git
cd uuid-toolkit
python uuid-toolkit.py v4
```

## Usage

Basic Command Structure:
```
python uuid-toolkit.py <command> [options]
```

## Command Reference

**Command Table**

| Command           | Arguments                | Description                                                         | Example Usage                                               | Notes                                                   |
|-------------------|---------------------------|---------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------|
| `v1`              | *(none)*                 | Generates a time-based UUID (timestamp + MAC address).             | `python uuid-toolkit.py v1`                                 | Not deterministic. May expose MAC address.             |
| `v3`              | `<namespace> <name>`     | Deterministic MD5-based UUID. Same inputs → same UUID.             | `python uuid-toolkit.py v3 DNS example.com`                 | Uses MD5 (weak hash).                                   |
| `v4`              | *(none)*                 | Generates a random UUID using secure RNG.                          | `python uuid-toolkit.py v4`                                 | Best general-purpose version.                          |
| `v5`              | `<namespace> <name>`     | Deterministic SHA-1-based UUID.                                    | `python uuid-toolkit.py v5 URL https://example.com`         | More secure than v3, deterministic.                    |
| `list-namespaces` | *(none)*                 | Displays available namespaces and their UUID values.                | `python uuid-toolkit.py list-namespaces`                    | Helpful for v3/v5 generation.                          |
| `validate`        | `<uuid>`                 | Validates whether a string is a valid UUID.                        | `python uuid-toolkit.py validate <uuid>`                    | Detects malformed or invalid UUIDs.                    |
| `info`            | `<uuid>`                 | Shows details of a UUID (version, variant, validity).              | `python uuid-toolkit.py info <uuid>`                        | Identify UUID version used by external systems.        |

## Detailed Command Specifications

**1. generate**

Generates a UUID of the selected version.

**Options:**

* v1 : Time‑based UUID

* v3 <namespace> <name> : MD5 namespace‑based UUID

* v4 : Random UUID

* v5 <namespace> <name> : SHA‑1 namespace‑based UUID


**Example:**
```
python uuid-toolkit.py v4
```

**2. validate**

Checks whether the provided UUID string is valid.

**Example:**
```
python uuid-toolkit.py validate 550e8400-e29b-41d4-a716-446655440000
```

**3. format**

Converts the UUID to different representations.

**Options:**

* --uppercase

* --lowercase

* --urn


**Example:**
```
python uuid-toolkit.py format --uppercase <uuid>
```

**4. inspect**

Displays metadata such as version, variant, timestamp (v1), and namespaces.

**Example:**
```
python uuid-toolkit.py inspect <uuid>
```

**5. batch**

Generates multiple UUIDs.

**Options:**

* --count <n>

* UUID version flags (v1, v4, etc.)


**Example:**
```
python uuid-toolkit.py batch --count 50 --v4
```

## License

This project is distributed under an open, corporate‑friendly license.


---

## Support

For enterprise support or integration guidance, contact the project maintainer.
