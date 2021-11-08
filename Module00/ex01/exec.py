import sys

args = sys.argv[1:]
args = [args[i][::-1].swapcase() for i in range(0, len(args))]
args.reverse()
if len(args) > 0:
    print(*args, sep=' ')
