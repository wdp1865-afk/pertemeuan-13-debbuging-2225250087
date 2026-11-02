
def rata_rata(data):
    # Penanganan list kosong
    if len(data) == 0:
        return "Data kosong, rata-rata tidak dapat dihitung"

    total = sum(data)
    return total / len(data)


# Pengujian program
print("Test 1:", rata_rata([80, 90, 70]))
print("Test 2:", rata_rata([80, 90]))
print("Test 3:", rata_rata([60, 70, 80, 90]))
print("Test 4:", rata_rata([]))
