import time
import random

SINS = [
    "lying", "sloth", "envy", "pride", "greed",
    "wrath", "gluttony", "gossip", "vanity", "lust",
    "procrastination", "judging others", "eating the last slice",
    "ghosting someone", "replying 'lol' to end a conversation",
    "pretending to be busy", "forgetting birthdays",
    "skipping leg day", "double texting", "loud chewing",
]

def confess():
    print("\n" + "░" * 44)
    print("   ✝  COUNT YOUR SINS  ✝")
    print("░" * 44)

    total = 0
    sin_log = []

    while True:
        print(f"\n  sins committed: {total}")
        print("  [ENTER] to sin again | 'confess' | 'quit'")
        user_input = input("  > ").strip().lower()

        if user_input == "quit":
            print("\n  Go in peace. (you won't.)\n")
            break

        elif user_input == "confess":
            if not sin_log:
                print("\n  You are pure. Suspicious.")
            else:
                print(f"\n  Your {len(sin_log)} sin(s):")
                for i, s in enumerate(sin_log, 1):
                    print(f"    {i}. {s}")
                print("\n  ...and you thought no one was watching.")
            continue

        # Commit a sin
        sin = random.choice(SINS)
        total += 1
        sin_log.append(sin)

        # Dramatic falling animation
        width = 36
        indent = random.randint(2, width - len(sin) - 2)
        indent = max(2, indent)

        rows = 8
        for row in range(rows):
            delay = 0.04 if row < rows - 2 else 0.1
            print(f"{' ' * indent}⚡ {sin}")
            time.sleep(delay)
            print("\033[A\033[K", end="", flush=True)

        # Bounce
        for b in range(2):
            print(f"{' ' * indent}⚡ {sin}")
            time.sleep(0.12 + b * 0.06)
            print("\033[A\033[K", end="", flush=True)
            print(f"{' ' * (indent + 1)}⚡ {sin}")
            time.sleep(0.08)
            print("\033[A\033[K", end="", flush=True)

        # Settle
        print(f"{' ' * indent}⚡ {sin}")
        print(f"\n  {'🔴 ' * min(total, 20)}")
        print(f"  sin #{total}: {sin}")


if __name__ == "__main__":
    confess()