import csv

FILENAME = "library.csv"
library = {}  # {book_id: (title, author, copies)}

def load_library():
    """Load data from CSV into library dict."""
    try:
        with open(FILENAME, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) != 4:
                    continue
                book_id, title, author, copies = row
                try:
                    copies = int(copies)
                except ValueError:
                    copies = 0
                library[book_id] = (title, author, copies)
    except FileNotFoundError:
        pass

def save_library():
    """Save library dict to CSV."""
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['book_id', 'title', 'author', 'copies'])
        for book_id, (title, author, copies) in library.items():
            writer.writerow([book_id, title, author, copies])