# UUID Toolkit

UUID Toolkit is a professional, cross‑platform command‑line utility for generating, and validating. Designed for reliability, clarity, and operational consistency across multiple environments. The UUID Toolkit provides a unified interface for interacting with Universally Unique Identifiers (UUIDs). 

# Features

* Generate UUIDs (v1, v3, v4, v5)

* Validate UUID strings

* Batch generation

* Deterministic namespace‑based UUID creation

* Fully cross‑platform (Linux, macOS, Windows)

* Output formatting (upper/lower/plain/JSON)

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
| `help` | *(none)*                 | Displays help feature               | `python uuid-toolkit.py --help`                    | -                          |
| `validate`        | `<uuid>`                 | Validates whether a string is a valid UUID.                        | `python uuid-toolkit.py validate <uuid>`                    | Detects malformed or invalid UUIDs.                    |

## **Detailed Command Specifications**

**1. Generate**

Generates a UUID of the selected version. Each version has its own method of generation:



**Options:**

* v1 : Time‑based UUID, derived from the current timestamp and MAC address. Deterministic for a given time and node, but may expose MAC address.

* v3 <namespace> <name> : Deterministic MD5-based UUID. Same namespace and name will always produce the same UUID. Uses MD5 hashing.

* v4 : Random UUID using a secure random number generator. Best choice for general purposes.

* v5 <namespace> <name> : Deterministic SHA-1-based UUID. More secure than v3, same inputs produce same UUID.


**Example:**
```
python uuid-toolkit.py v4
```


**2. Validate**



**Options:**

Validates whether a provided UUID string is correctly formatted and optionally checks for a specific version.

* `<uuid>` : The UUID string to validate.  
* `--version <1|3|4|5>` : (Optional) Check if the UUID matches the specified version.  
* `--quiet` : Suppress output; exit code 0 if valid, non-zero otherwise.

**Example:**
```
python uuid-toolkit.py validate 550e8400-e29b-41d4-a716-446655440000
```


**3. Format**


**Options:**

Adjusts the output representation of UUIDs. Can be combined with generation or batch commands.

* `--upper` : Converts UUIDs to uppercase letters.  
* `--lower` : Converts UUIDs to lowercase letters.  
* `--format json` : Outputs UUIDs in a JSON array.  
* `--format plain` : Outputs UUIDs as plain text, one per line (default).


**Example:**
```
python uuid-toolkit.py v4 --upper
```
```
python uuid-toolkit.py v4 --lower
```
```
python uuid-toolkit.py v4 --format json
```
```
python uuid-toolkit.py v4 --format plain
```



**4. Batch**

Generates multiple UUIDs in a single command.



**Options:**

* `--count <n>` or `-n <n>` : Specifies the number of UUIDs to generate. Must be ≥ 1.  
* Compatible with all generation versions (`v1`, `v3`, `v4`, `v5`).

**Example:**
```
python uuid-toolkit.py v4 --count 50
```
```
python uuid-toolkit.py v4 -n 50
```

**5. Saving Results to a File**

Redirects the command output to an external file instead of standard output.

* `--output <path>` or `-o <path>` : Specifies the file path to save the UUIDs. Overwrites if file exists.

**Example:**
```
python uuid-toolkit.py v4 --output uuid.txt
```
```
python uuid-toolkit.py v4 -o uuid.txt
```

## License

This project is licensed under the Apache License 2.0. You may use, modify, and distribute the software under the terms defined in the Apache 2.0 license.
