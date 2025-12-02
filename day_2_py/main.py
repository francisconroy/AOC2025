import dataclasses


@dataclasses.dataclass
class ItemRange:
    start: int
    end: int

fancy_items = []
invalid_ids = []

def is_item_valid(item: int) -> bool:
    itstring = str(item)
    if len(itstring)%2 == 0:
        halflen = len(itstring)//2
        if itstring[0:halflen] == itstring[halflen:]:
            return False
    return True

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
print(sum(invalid_ids))
