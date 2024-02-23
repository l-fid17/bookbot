def main():
    book = "frankenstein.txt"
    with open(f"books/{book}") as f:
        content = f.read()
        print_report(book.split(".")[0].upper(), content)
        


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

def sort_on(dict):
    return dict["name"]

def convert_dict_to_list(dict):
    list = []
    for item in dict.keys():
            if item.isalpha():
                list.append({"name": item, "num": dict[item]})
    return list

def print_report(title, content):
    print("-------- BEGIN REPORT --------")
    print(f"BOOK: {title}\n")
    print(f"WORD COUNT: {str(word_count(content))}\n")

    chars = count_distinct_characters(content)
    
    letters = convert_dict_to_list(chars)
    letters.sort(reverse=False, key=sort_on)
    
    for letter in letters:
        print(f"Letter '{letter["name"]}' found {letter["num"]} times.")

    print("\n--------- END REPORT ---------")

main()