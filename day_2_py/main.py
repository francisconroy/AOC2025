import dataclasses


@dataclasses.dataclass
class ItemRange:
    start: int
    end: int

def is_item_valid(item: int) -> bool:
    itstring = str(item)
    if len(itstring)%2 == 0:
        halflen = len(itstring)//2
        if itstring[0:halflen] == itstring[halflen:]:
            return False
    return True

def is_item_valid_advanced(item: int) -> bool:
    itstring = str(item)
    itemlengths = range(1, len(itstring)//2 + 1)
    itemlengths_refined = [l for l in itemlengths if len(itstring)%l == 0]
    for itemlen in itemlengths_refined:
        itemcount = len(itstring)//itemlen
        refitem = itstring[0:itemlen]
        if itstring.count(refitem) == itemcount:
            return False

    return True


if __name__ == "__main__":
    fancy_items = []
    invalid_ids = []
    advanced_invalid_ids = []
    with open("sample.txt", "r") as readfile:
        content = readfile.read()
        items = content.split(",")
        for item in items:
            start, end = item.split("-")
            fancy_items.append(ItemRange(int(start), int(end)))

    for item_range in fancy_items:
        for item_id in range(item_range.start, item_range.end + 1):
            if not is_item_valid(item_id):
                invalid_ids.append(item_id)
            if not is_item_valid_advanced(item_id):
                advanced_invalid_ids.append(item_id)
    print(sum(invalid_ids))
    print(sum(advanced_invalid_ids))
