#!/usr/bin/env python3
import sys
import importlib


def check_dependencies() -> bool:
    packages = [
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computation"),
        ("matplotlib", "Visualization"),
    ]
    print("Checking dependencies:")
    all_ok = True
    for mod, msg in packages:
        try:
            module = importlib.import_module(mod)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {mod} ({version}) - {msg} ready")
        except ImportError:
            print(f"[MISSING] {mod} - {msg}")
            all_ok = False
    return all_ok


def show_package_manager_info() -> None:
    print("\n--- Dependency management comparison ---")
    print("pip  : uses requirements.txt")
    print("       Install with: pip install -r requirements.txt")
    print("Poetry: uses pyproject.toml")
    print("       Install with: poetry install")
    print("       Run with    : poetry run python loading.py")
    print("Both files are provided in this project.")


def run_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    n_points = 1000
    print("\nAnalyzing Matrix data...")
    print(f"Processing {n_points} data points...")

    rng = np.random.default_rng(seed=42)
    signal = rng.normal(loc=0.0, scale=1.0, size=n_points).cumsum()
    noise = rng.uniform(-0.5, 0.5, size=n_points)
    matrix_data = signal + noise

    df = pd.DataFrame({"step": range(n_points), "value": matrix_data})

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["step"], df["value"], color="green", linewidth=0.8)
    ax.set_title("Matrix Data Stream")
    ax.set_xlabel("Step")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.3)

    output_file = "matrix_analysis.png"
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close(fig)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        print(
            "\nSome dependencies are missing. Install them with:\n"
            "  pip    : pip install -r requirements.txt\n"
            "  Poetry : poetry install"
        )
        sys.exit(1)

    show_package_manager_info()

    try:
        run_analysis()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(0)
    except Exception as e:
        print(f"Got error during analysis: {e}")
        sys.exit(1)
