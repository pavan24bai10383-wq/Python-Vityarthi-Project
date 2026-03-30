def get_valid_copies(prompt):
    while True:
        copies = input(prompt).strip()
        if copies.isdigit() and int(copies) >= 0:
            return int(copies)
        print("Invalid input! Copies must be a non-negative integer.")