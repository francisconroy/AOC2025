from typing import Iterator, Sequence


def consolidate_ranges(ranges: set[range]) -> set[range]:
    sorted_ranges = sorted(ranges, key=lambda r: r.start)
    output_ranges: set[range] = set()
    ranges_to_remove: set[range] = set()

    for i in sorted_ranges:
        if i in output_ranges or i in ranges_to_remove:
            continue
        for j in sorted_ranges:
            if j in output_ranges or j in ranges_to_remove:
                continue
            if i is j:
                continue
            if j.start in i: # j starts inside i
                if j.stop-1 > i.stop-1:
                    output_ranges.add(range(i.start, j.stop))
                    ranges_to_remove.add(i)
                    ranges_to_remove.add(j)
                    break
                elif j.stop-1 in i: # j ends inside i
                    output_ranges.add(i)
                    ranges_to_remove.add(j)
                    break
            elif j.stop-1 in i:
                if j.start < i.start:
                    output_ranges.add(range(j.start, i.stop))
                elif j.start in i:
                    output_ranges.add(i)
                    ranges_to_remove.add(j)
                    break

        else:
            output_ranges.add(i)

    return output_ranges


def main():
    id_ranges: set[Sequence] = set()
    fresh_ids: list[int] = []
    with open("input.txt","r") as readfile:
        for line in readfile.readlines():
            if '-' in line:
                start, end = map(int, line.strip().split('-'))
                assert start <= end
                id_ranges.add(range(start, end + 1))
            else:
                try:
                    id = int(line.strip())
                except ValueError:
                    continue
                for robj in id_ranges:
                    if id in robj:
                        fresh_ids.append(id)
                        break
    print(len(fresh_ids))
    print(len(id_ranges))

    last_diff = -1
    while last_diff != 0 and len(id_ranges) > 1:
        consolidated = consolidate_ranges(id_ranges)
        last_diff = len(id_ranges) - len(consolidated)
        id_ranges = consolidated

    print(len(id_ranges))

    total_range = 0
    for rangeobj in id_ranges:
        total_range += end - start + 1
    print(total_range)
    # all_ids = set()
    # for rangeobj in id_ranges:
    #
    #     all_ids |= set(rangeobj)
    # print(len(all_ids))

if __name__ == '__main__':
    main()