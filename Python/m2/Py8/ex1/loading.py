#!/usr/bin/env python3
import importlib


if __name__ == "__main__":
    list_mod = [('pandas', 'Data manipulation'),
                ('numpy',  'Numerical computation'),
                ('matplotlib', 'Visualization')]
    print("\nLOADING STATUS: Loading programs...\n")
    try:
        try:
            print("Checking dependencies: ....")
            for mod, msg in list_mod:
                module = importlib.import_module(mod)
                print(f"[OK] {module.__name__}\
 ({module.__version__}) - {msg} ready")
        except (ImportError, KeyError, Exception) as e:
            print(f"Got error: {e}")
            print("Please use pip install to install de dependence", mod)
            exit(1)

        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        try:
            matrix = np.random.randint(0, 10, 50)
            data = pd.DataFrame(matrix)
            x, y = (data.index.to_list(), data.values.tolist())
            plt.plot(x, y)
            name = "matrix_analysis.png"
            plt.savefig(name)
            print(f"file is saving in: {name}")
        except (Exception, KeyboardInterrupt) as e:
            print(f"Got error: {e}")
    except (Exception, KeyboardInterrupt) as e:
        print(f"Got error {e}")
