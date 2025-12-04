

SUBGRID_SIZE = 3
PADDING = 1


def count_adjacents_in_subgrid(grid: list[list[str]], center_row, center_col) -> int:
    count = 0
    for rowidx in range(center_row-PADDING, center_row+PADDING+1):
        for cellidx in range(center_col-PADDING, center_col+PADDING+1):
            if cellidx == center_col and rowidx == center_row:
                continue  # skip center
            if grid[rowidx][cellidx] == '@':
                count += 1

    return count


def extend_grid(grid: list[list[str]]) -> list[list[str]]:
    width = len(grid[0])
    # extend lines
    ogrid = []
    for row in grid:
        ogrid.append([""] + row + [""])

    # Add top and bottom
    ogrid.insert(0, [""] * (width + 2*PADDING))
    ogrid.append([""] * (width + 2*PADDING))
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
                count = count_adjacents_in_subgrid(grid, rowidx, cellidx)
                if count < 4:
                    loop_removed_amount += 1
                    total_count += 1
                    grid[rowidx][cellidx] = "x"
    print(total_count)


if __name__ == '__main__':
    main()
