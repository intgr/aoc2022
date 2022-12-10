import sys
import re
from typing import IO

splitter = re.compile(r'(...)( |$)')


def parse_stacks(f: IO[str]) -> list[list[str]]:
    stacks: list[list[str]] = []

    for line in f:
        line = line.removesuffix('\n')
        if line.startswith(' 1 '):
            continue

        if line == '':
            for i in range(len(stacks)):
                stacks[i] = list(reversed(stacks[i]))
            return stacks

        assert line.startswith('[') or line.startswith('   ')

        for i, match in enumerate(splitter.finditer(line)):
            crate = match.group(1)
            if crate != '   ':
                while len(stacks) <= i:
                    stacks.append([])
                stacks[i].append(crate[1])

    raise AssertionError("Where am I?")


def operate_crane(f: IO[str], stacks: list[list[str]]) -> list[list[str]]:
    for line in f:
        words = line.split()
        match words:
            case ['move', num, 'from', frm, 'to', to]:
                i_frm = int(frm) - 1
                i_to = int(to) - 1
                i_num = int(num)

                stacks[i_to].extend(stacks[i_frm][-i_num:])
                del stacks[i_frm][-i_num:]
            case wat:
                raise AssertionError(f"Cannot parse {wat}")
    return stacks


def print_stacks(stacks: list[list[str]]):
    for i, stack in enumerate(stacks):
        print(f'{i+1}: ' + ' '.join(f'[{n}] ' for n in stack))

    print()


def main(f: IO[str]) -> None:
    stacks = parse_stacks(f)
    # print_stacks(stacks)
    stacks = operate_crane(f, stacks)

    # print_stacks(stacks)
    print(''.join(stack.pop() for stack in stacks))


if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    main(f)
