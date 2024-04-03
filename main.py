def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_of_words = get_number_of_words(text)
    count_of_chars = count_characters(text)
    print(create_book_report(count_of_words, count_of_chars))


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(book):
    words = len(book.split())
    return words


def count_characters(book):
    words = book.split()
    char_dict = {}
    for word in words:
        lowered_word = word.lower()
        for l in lowered_word:
            if l in char_dict:
                char_dict[l] += 1
            else:
                char_dict[l] = 1
    return char_dict


def create_book_report(word_count, chars_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count, " words found in the document")
    for char in chars_dict:
        if char.isalpha():
            print("The '{char}' character was found {chars_dict[char]} times")
    print("--- End report ---")


main()
