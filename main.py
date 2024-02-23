def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        print(content)
        print("WORD:COUNT::: " + str(word_count(content)))
        print(count_distinct_characters(content))

def word_count(text):
    return len(text.split())

def count_distinct_characters(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars


main()