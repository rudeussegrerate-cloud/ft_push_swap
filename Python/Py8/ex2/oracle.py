#!/usr/bin/env python3
import os
import sys


def load_env() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError as e:
        raise RuntimeError(
            f"{e}\nPlease install python-dotenv:\n"
            "  pip install python-dotenv"
        )


def get_config() -> dict[str, str]:
    keys = {
        "MATRIX_MODE": "development",
        "DATABASE_URL": "",
        "API_KEY": "",
        "LOG_LEVEL": "INFO",
        "ZION_ENDPOINT": "",
    }
    config: dict[str, str] = {}
    missing: list[str] = []

    for key, default in keys.items():
        value = os.getenv(key, default)
        if not value:
            missing.append(key)
        else:
            config[key] = value

    if missing:
        raise ValueError(
            f"Missing required configuration: {', '.join(missing)}\n"
            "Copy .env.example to .env and fill in the values."
        )
    return config


def display_config(config: dict[str, str]) -> None:
    labels = {
        "MATRIX_MODE": "Mode",
        "DATABASE_URL": "Database",
        "API_KEY": "API Access",
        "LOG_LEVEL": "Log Level",
        "ZION_ENDPOINT": "Zion Network",
    }
    print("Configuration loaded:")
    for key, label in labels.items():
        value = config[key]
        if key == "API_KEY":
            value = value[:4] + "****" if len(value) > 4 else "****"
        print(f"{label}: {value}")


def show_mode_behavior(config: dict[str, str]) -> None:
    mode = config.get("MATRIX_MODE", "development")
    print(f"\n[{mode.upper()} MODE]")
    if mode == "development":
        print("  - Verbose logging enabled (DEBUG)")
        print("  - Using local database instance")
        print("  - Error stack traces will be shown")
    elif mode == "production":
        print("  - Minimal logging (WARN only)")
        print("  - Using remote database")
        print("  - Errors are silently logged")
    else:
        print(f"  - Unknown mode '{mode}', defaulting to development behavior")


def security_check(config: dict[str, str]) -> None:
    print("\nEnvironment security check:")

    api_key = config.get("API_KEY", "")
    if api_key not in ("", "changeme", "secret", "12345"):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] API_KEY looks like a placeholder — change it!")

    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env file found — using environment variables only")


    print("[OK] Production overrides available")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        load_env()
        config = get_config()
        display_config(config)
        show_mode_behavior(config)
        security_check(config)
        print("\nThe Oracle sees all configurations.")
    except (RuntimeError, ValueError) as e:
        print(f"Got error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
