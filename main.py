def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_of_words = get_number_of_words(text)
    print(count_of_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(book):
    words = len(book.split())
    return words


main()
