# UUID Toolkit

A professional, cross‑platform command‑line utility for generating, validating, formatting, and inspecting UUIDs. Designed for reliability, clarity, and operational consistency across multiple environments.

The UUID Toolkit provides a unified interface for interacting with Universally Unique Identifiers (UUIDs). It includes commands for generating various UUID versions, validating existing UUID strings, converting formats, and retrieving metadata.


# Features

* Generate UUIDs (v1, v3, v4, v5)

* Validate and inspect UUID strings

* Convert UUID formats (uppercase, lowercase, URN)

* Batch generation

* Deterministic namespace‑based UUID creation

* Fully cross‑platform (Linux, macOS, Windows)

# Installation

**1. Requirements**

Ensure the following components are installed:

* Python 3.8+

* pip (Python package manager)




**2. Installation**

* Debian/Ubuntu:
```
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/katryoshkh/uuid-toolkit.git
cd uuid-toolkit
```

* Fedora / RHEL: 
```
sudo dnf install python3 python3-pip git -y
git clone https://github.com/katryoshkh/uuid-toolkit.git
cd uuid-toolkit
```

* Arch / Manjaro:
```
sudo pacman -S python python-pip git
git clone https://github.com/katryoshkh/uuid-toolkit.git
cd uuid-toolkit
```
  
* macOS Homebrew:
```
brew install python git
git clone https://github.com/katryoshkh/uuid-toolkit.git
cd uuid-toolkit
```

* Android (Termux):
```
pkg update
pkg install python git -y
git clone https://github.com/katryoshkh/uuid-toolkit.git
cd uuid-toolkit
```

* Windows (PowerShell):
> Install Python from [python.org](https://python.org)
```
git clone https://github.com/katryoshkh/uuid-toolkit.git
cd uuid-toolkit
```

# Usage

Basic Command Structure:
```
python uuid-toolkit.py <command> [options]
```

# Command Reference

## **Command Table**

| Command           | Arguments                | Description                                                         | Example Usage                                               | Notes                                                   |
|-------------------|---------------------------|---------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------|
| `v1`              | *(none)*                 | Generates a time-based UUID (timestamp + MAC address).             | `python uuid-toolkit.py v1`                                 | Not deterministic. May expose MAC address.             |
| `v3`              | `<namespace> <name>`     | Deterministic MD5-based UUID. Same inputs → same UUID.             | `python uuid-toolkit.py v3 DNS example.com`                 | Uses MD5 (weak hash).                                   |
| `v4`              | *(none)*                 | Generates a random UUID using secure RNG.                          | `python uuid-toolkit.py v4`                                 | Best general-purpose version.                          |
| `v5`              | `<namespace> <name>`     | Deterministic SHA-1-based UUID.                                    | `python uuid-toolkit.py v5 URL https://example.com`         | More secure than v3, deterministic.                    |
| `list-namespaces` | *(none)*                 | Displays available namespaces and their UUID values.                | `python uuid-toolkit.py list-namespaces`                    | Helpful for v3/v5 generation.                          |
| `validate`        | `<uuid>`                 | Validates whether a string is a valid UUID.                        | `python uuid-toolkit.py validate <uuid>`                    | Detects malformed or invalid UUIDs.                    |
| `info`            | `<uuid>`                 | Shows details of a UUID (version, variant, validity).              | `python uuid-toolkit.py info <uuid>`                        | Identify UUID version used by external systems.        |

## **Detailed Command Specifications**

**1. Generate**

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

**2. Validate**

Checks whether the provided UUID string is valid.

**Example:**
```
python uuid-toolkit.py validate 550e8400-e29b-41d4-a716-446655440000
```

**3. Format**

Converts the UUID to different representations.

**Options:**

* --upper

* --lower

**Example:**
```
python uuid-toolkit.py v4 --upper
```
```
python uuid-toolkit.py v4 --lower
```

**4. Batch**

Generates multiple UUIDs.

**Options:**

* --count <n>
* -n

**Example:**
```
python uuid-toolkit.py v4 --count 50
```
```
python uuid-toolkit.py v4 -n 50
```

**5. Saving Results to a File**

Saving output results to a external file.

**Options:**

* --output <path>
* -o <path>

**Example:**
```
python uuid-toolkit.py v4 --output uuid.txt
```
```
python uuid-toolkit.py v4 --o uuid.txt
```

## License

This project is distributed under Apache 2.0 license.
