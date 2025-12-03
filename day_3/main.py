

if __name__ == '__main__':
    joltages = []
    with open("sample.txt", "r") as readfile:
        bank_strings = [l.strip() for l in readfile.readlines()]
        bank_arrays = []
        for bank_string in bank_strings:
            bank_array = [int(digit) for digit in bank_string]
            bank_arrays.append(bank_array)

            first_digit = max(bank_array[0:-1])
            digpos = bank_array.index(first_digit)
            end_array = bank_array[digpos + 1 :]
            second_digit = max(end_array)
            comb = int(f"{first_digit}{second_digit}")
            joltages.append(comb)

    print(joltages)

    print(sum(joltages))
