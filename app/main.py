import sys
import os
import zlib


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage

    command = sys.argv[1]
    args = sys.argv[2:]
    if command == "init":
        init()
    elif command == "cat-file":
        cat_file(*args)
    else:
        raise RuntimeError(f"Unknown command #{command}")


def init():
    os.mkdir(".git")
    os.mkdir(".git/objects")
    os.mkdir(".git/refs")
    with open(".git/HEAD", "w") as f:
        f.write("ref: refs/heads/master\n")
    print("Initialized git directory1")


def cat_file(*args):
    file = None
    if len(args) < 2:
        file = args[0]
    if args[0] == "-p":
        file = args[1]
    folder, file = file[:2], file[2:]
    with open(f".git\objects\{folder}\{file}", "rb") as f:
        sys.stdout.write(zlib.decompress(f.read()).decode("utf-8")[8:])

if __name__ == "__main__":
    main()
