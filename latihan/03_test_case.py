
def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

# Test case
print("Test 59:", status_lulus(59))
print("Test 60:", status_lulus(60))
print("Test 61:", status_lulus(61))


def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Test case
print("Test 59:", status_lulus(59))
print("Test 60:", status_lulus(60))
print("Test 61:", status_lulus(61))
