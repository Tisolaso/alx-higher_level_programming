import sys

if __name__ == "__main__":
    args_list = sys.argv
    args_len = len(args_list) - 1

    if args_len == 0:
        print("{} arguments.".format(args_len))

    else:
        print("{} arguments:".format(args_len))

        for index, item in enumerate(args_list):
            print("{}: {}".format((index + 1), item))
