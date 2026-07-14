#!/usr/bin/env python3
def secure_archive(file_name: str,
                   mode: int = 0,
                   text: str = "") -> tuple[bool, str]:
    reussi = False
    lecture = ['r', 'w']
    message = ""
    try:
        with open(file_name, lecture[mode]) as f:
            if (mode == 0):
                message = f.read()
            elif (mode == 1):
                f.write(text)
                message = "Content successfully written to file"
            reussi = True
    except Exception as e:
        message = str(e)
    finally:
        return (reussi, message)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    file_name = "file/not/exist.txt"
    print("Using 'secure_archive' to read", end="")
    print(f" from a nonexistent file: {file_name}")
    print(secure_archive(file_name), "\n")
    file_name = "/etc/master.passwd"
    print("Using 'secure_archive' to read from a ", end="")
    print(f" inaccessible file: '{file_name}'")
    print(secure_archive(file_name), "\n")
    file_name = "regular_file.txt"
    print("Using 'secure_archive' to read", end="")
    print(" from a regular file:")
    print(secure_archive(file_name), "\n")
    file_name = "new_file.txt"
    print("Using 'secure_archive' to", end="")
    print(" write previous content to a new file:")
    print(secure_archive(file_name, 1, "Hello"))
