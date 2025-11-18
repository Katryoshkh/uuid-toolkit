#!/usr/bin/env python3
import argparse
import sys
import uuid
import json
from typing import Iterable, Optional

BUILTIN_NAMESPACES = {
    "DNS": uuid.NAMESPACE_DNS,
    "URL": uuid.NAMESPACE_URL,
    "OID": uuid.NAMESPACE_OID,
    "X500": uuid.NAMESPACE_X500,
}

# Parse namespace input (builtin name or UUID string)
def parse_namespace(ns: Optional[str]) -> uuid.UUID:
    if not ns:
        raise ValueError("Namespace is required for this operation.")
    key = ns.upper()
    if key in BUILTIN_NAMESPACES:
        return BUILTIN_NAMESPACES[key]
    try:
        return uuid.UUID(ns)
    except Exception:
        raise ValueError(f"Invalid namespace UUID or unknown builtin name: {ns!r}")

# Generate a single uuid.UUID object for the requested version
def generate_single(version: str, namespace: Optional[uuid.UUID], name: Optional[str]) -> uuid.UUID:
    if version == "v1":
        return uuid.uuid1()
    if version == "v4":
        return uuid.uuid4()
    if version == "v3":
        if namespace is None or name is None:
            raise ValueError("v3 requires namespace and name.")
        return uuid.uuid3(namespace, name)
    if version == "v5":
        if namespace is None or name is None:
            raise ValueError("v5 requires namespace and name.")
        return uuid.uuid5(namespace, name)
    raise ValueError("Unsupported version: " + version)

# Validate a UUID string and optionally check version
def validate_uuid_str(value: str, version: Optional[int] = None) -> (bool, Optional[int]):
    try:
        u = uuid.UUID(value)
        v = u.version
        if version is None:
            return True, v
        return v == version, v
    except Exception:
        return False, None

def generate_many(version: str, count: int, namespace: Optional[uuid.UUID], name: Optional[str]) -> Iterable[str]:
    for _ in range(count):
        yield str(generate_single(version, namespace, name))

def write_output(items: Iterable[str], fmt: str, out_path: Optional[str], case: Optional[str]) -> None:
    if out_path:
        f = open(out_path, "w", newline="")
        close_after = True
    else:
        f = sys.stdout
        close_after = False
    try:
        if fmt == "plain":
            for it in items:
                s = it.upper() if case == "upper" else it.lower() if case == "lower" else it
                f.write(s + "\n")
        elif fmt == "json":
            arr = []
            for it in items:
                s = it.upper() if case == "upper" else it.lower() if case == "lower" else it
                arr.append(s)
            json.dump(arr, f, ensure_ascii=False, indent=2)
            if not str(f).endswith("closed"):
                f.write("\n")
        else:
            raise ValueError("Unsupported format: " + fmt)
    finally:
        if close_after:
            f.close()

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="uuid-toolkit.py", description="Simple UUID generator & validator (v1,v3,v4,v5)")
    sub = p.add_subparsers(dest="command")
    p_v1 = sub.add_parser("v1", help="Generate UUID v1 (time-based)")
    p_v1.add_argument("-n", "--count", type=int, default=1, help="Number of UUIDs")
    common_args(p_v1)

    p_v4 = sub.add_parser("v4", help="Generate UUID v4 (random)")
    p_v4.add_argument("-n", "--count", type=int, default=1, help="Number of UUIDs")
    common_args(p_v4)

    p_v3 = sub.add_parser("v3", help="Generate UUID v3 (MD5 namespace+name)")
    p_v3.add_argument("namespace", nargs="?", default="DNS", help="Namespace (DNS|URL|OID|X500 or UUID)")
    p_v3.add_argument("name", help="Name string")
    p_v3.add_argument("-n", "--count", type=int, default=1, help="Number of UUIDs (same result repeated)")
    common_args(p_v3)

    p_v5 = sub.add_parser("v5", help="Generate UUID v5 (SHA-1 namespace+name)")
    p_v5.add_argument("namespace", nargs="?", default="DNS", help="Namespace (DNS|URL|OID|X500 or UUID)")
    p_v5.add_argument("name", help="Name string")
    p_v5.add_argument("-n", "--count", type=int, default=1, help="Number of UUIDs (same result repeated)")
    common_args(p_v5)

    p_val = sub.add_parser("validate", help="Validate a UUID string")
    p_val.add_argument("uuid", help="UUID string to validate")
    p_val.add_argument("--version", "-v", type=int, choices=[1,3,4,5], help="Expected version")
    p_val.add_argument("--quiet", action="store_true", help="Exit 0 if valid, non-zero otherwise (no output)")

    return p

def common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format", "-f", choices=["plain","json"], default="plain", help="Output format")
    parser.add_argument("--output", "-o", help="Write output to file")
    parser.add_argument("--upper", action="store_true", help="Uppercase output")
    parser.add_argument("--lower", action="store_true", help="Lowercase output")

def main(argv: Optional[list] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "command", None):
        args.command = "v4"
        setattr(args, "count", 1)
        setattr(args, "format", "plain")
        setattr(args, "output", None)
        setattr(args, "upper", False)
        setattr(args, "lower", False)

    case = "upper" if getattr(args, "upper", False) else "lower" if getattr(args, "lower", False) else None

    try:
        if args.command == "validate":
            ok, ver = validate_uuid_str(args.uuid, version=getattr(args, "version", None))
            if args.quiet:
                return 0 if ok else 1
            if ok:
                if args.version is None:
                    print(f"VALID UUID (version {ver})")
                else:
                    print(f"VALID UUID and version matches {args.version}")
                return 0
            else:
                print("INVALID UUID")
                return 1

        # generation commands
        if args.command in ("v1","v3","v4","v5"):
            count = getattr(args, "count", 1)
            if count < 1:
                raise ValueError("count must be >= 1")

            ns = None
            name = None
            if args.command in ("v3","v5"):
                ns = parse_namespace(getattr(args, "namespace", None))
                name = getattr(args, "name", None)
                if not name:
                    raise ValueError("name is required for v3/v5")

            gen = generate_many(args.command, count, ns, name)
            write_output(gen, args.format, args.output, case)
            return 0

        parser.print_help()
        return 1

    except ValueError as e:
        print("Error:", e, file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\nAborted.", file=sys.stderr)
        return 130
    except Exception as e:
        print("Internal error:", e, file=sys.stderr)
        return 3

if __name__ == "__main__":
    sys.exit(main())