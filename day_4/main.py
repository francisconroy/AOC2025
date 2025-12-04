import pdb

SUBGRID_SIZE = 3
PADDING = 1


def count_adjacents_in_subgrid(subgrid: list[list[str]]) -> int:
    count = 0
    for rowidx in range(SUBGRID_SIZE):
        for cellidx in range(SUBGRID_SIZE):
            if cellidx == 1 == rowidx:
                continue  # skip center
            try:
                if subgrid[rowidx][cellidx] == '@':
                    count += 1
            except Exception:
                pdb.pm()
    return count


def extend_grid(grid: list[list[str]]) -> list[list[str]]:
    width = len(grid[0])
    # extend lines
    ogrid = []
    for row in grid:
        ogrid.append([""] + row + [""])

    # Add top and bottom
    ogrid.insert(0, [""] * (width + 2))
    ogrid.append([""] * (width + 2))
    return ogrid


def main():
    grid = []
    with open('input.txt', "r") as readfile:
        content = readfile.readlines()
        for line in content:
            line = line.strip('\n')
            line = list(line)
            grid.append(line)

    grid = extend_grid(grid)

    # iterate over grid excluding borders
    grid_width = len(grid[0])
    grid_height = len(grid)

    total_count = 0
    loop_removed_amount = -1
    while loop_removed_amount != 0:
        loop_removed_amount = 0
        for rowidx in range(PADDING, grid_height - PADDING):
            for cellidx in range(PADDING, grid_width - PADDING):
                cell = grid[rowidx][cellidx]
                if cell != '@':
                    continue
                # extract subgrid
                subgrid = []
                for rowoffset in range(-PADDING, PADDING + 1):
                    subrow = grid[rowidx + rowoffset][cellidx - PADDING:cellidx + PADDING + 1]
                    subgrid.append(subrow)
                count = count_adjacents_in_subgrid(subgrid)
                if count < 4:
                    loop_removed_amount += 1
                    total_count += 1
                    grid[rowidx][cellidx] = "x"
    print(total_count)


if __name__ == '__main__':
    main()
