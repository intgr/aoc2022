import sys


def main():
    x = 1
    pc = 0
    sums = 0

    f = open(sys.argv[1], 'r')
    for line in f.readlines():
        instr = line.split()
        match instr:
            case ['noop']:
                increment = 0
                cycles = 1
            case ['addx', n]:
                increment = int(n)
                cycles = 2
            case wat:
                print(f"Unknown instruction {wat}")
                increment = 0
                cycles = 0

        for i in range(cycles):
            pc += 1
            if pc in (20, 60, 100, 140, 180, 220):
                print(f"Value at cycle {pc} is X={x}, total {x*pc}")
                sums += x * pc

        x += increment

    print(f"Result {sums}")
    print(f"End at {pc} X={x}")


if __name__ == '__main__':
    main()
