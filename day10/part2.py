import sys


def main():
    x = 1
    pc = 0
    sums = 0

    row = []

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

        for _ in range(cycles):
            column = pc % 40
            if column == 0 and row:
                print(''.join(row))
                row = []

            if x-1 <= column <= x+1:
                row.append('##')
            else:
                row.append('..')

            pc += 1

        x += increment
    print(''.join(row))


if __name__ == '__main__':
    main()
