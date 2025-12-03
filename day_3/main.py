

def process_bank(digits_to_select: int, bank_array: list[int]) -> int:
    selected_digits = []
    selection_array = bank_array.copy()
    for i in range(digits_to_select, 0, -1):
        number_remaining = i-1
        if number_remaining <=0:
            possibles = selection_array
        else:
            possibles = selection_array[0:-number_remaining]
        selected_digit = max(possibles)
        selected_digits.append(selected_digit)
        digpos = selection_array.index(selected_digit)
        selection_array = selection_array[digpos + 1:]
    comb = "".join([str(i) for i in selected_digits])
    return int(comb)

if __name__ == '__main__':
    part_1_joltages = []
    with open("sample.txt", "r") as readfile:
        bank_strings = [l.strip() for l in readfile.readlines()]
        bank_arrays = []
        for bank_string in bank_strings:
            bank_array = [int(digit) for digit in bank_string]
            bank_arrays.append(bank_array)

    for bank_array in bank_arrays:
        part_1_joltages.append(process_bank(2, bank_array))

    part_2_joltages = []
    for bank_array in bank_arrays:
        part_2_joltages.append(process_bank(12, bank_array))



    print(part_1_joltages)

    print(sum(part_1_joltages))
    print(sum(part_2_joltages))
