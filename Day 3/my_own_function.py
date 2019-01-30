import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')


def main(arg):
    print(arg)


main(sys.argv[0])
