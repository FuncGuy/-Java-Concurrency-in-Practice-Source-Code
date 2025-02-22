import sys
import os
import zlib


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
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
    _mode, hash = args
    hash_lead = hash[0:2]
    hash_tail = hash[2:]
    content = open(".git/objects/{}/{}".format(hash_lead, hash_tail), "rb")
    content = content.read()
    decompressed = zlib.decompress(content)
    decompressed = decompressed.decode("utf-8")
    decompressed = decompressed[8:]

    sys.stdout.write(decompressed)

if __name__ == "__main__":
    main()
