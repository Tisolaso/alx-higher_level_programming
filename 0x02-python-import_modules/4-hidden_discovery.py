#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    hidden_names = dir(hidden_4)

    for name in hidden_names:
        if not name.startswith("__"):
            print(name)
