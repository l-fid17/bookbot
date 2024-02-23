def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        print(content)
        print("WORD:COUNT::: " + str(word_count(content)))

def word_count(text):
    return len(text.split())

main()