import os

ENTRY = "Give me your backlog: I'll read the whole codebase tonight, ship the fix before your first coffee, and you pay nothing until it works."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
