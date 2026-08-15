#!/usr/bin/env python3
import os


if __name__ == "__main__":
    try:
        try:
            from dotenv import load_dotenv
            is_env = load_dotenv()
        except ImportError as e:
            raise Exception(f"{e}, please install the module before\n\
            do: pip install python-dotenv or the comment for install it")
        if not is_env:
            raise Exception("The .env file is missing")
        conf = [("Mode", "MATRIX_MODE"),
                ("Database", "DATABASE_URL"),
                ("API Access", "API_KEY"),
                ("Log Level", "LOG_LEVEL"),
                ("Zion Network", "ZION_ENDPOINT")]
        values: list[str] = []
        mode = None
        for _, key in conf:
            if (os.getenv(key)):
                values.append(os.getenv(key))
            else:
                raise Exception("missing key or value in .env file ;p")
        for key in values:
            if key.lower() in ("development", "production"):
                mode = key.lower()
                break
        if mode == "development":
            print(f"Mode : {mode}\n\
                Database : in localhost\n\
                API Access : key api is load\n\
                Log Level : DEBUG\n\
                Zion Network : net zion")
        if mode == "production":
            print(f"Mode : {mode}\n\
                Database : in the server\n\
                API Access : key api is load\n\
                Log Level : ONLINE\n\
                Zion Network : net zion")

    except Exception as e:
        print(f"Got error: {e}")
