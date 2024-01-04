#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    
    args_list = argv[1:]
    args_len = len(args_list)

    if args_len <= 0:
        print("{} arguments.".format(args_len))

    else:
        print("{} argument{}".format(args_len, "s:" if args_len > 1 else ":"))

        for index, item in enumerate(args_list):
            print("{}: {}".format((index + 1), item))
