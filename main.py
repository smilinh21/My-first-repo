
with open("books/frankenstein.txt") as f:
    content = f.read()
    new_content = content.lower()

def count_words(content):
    words = content.split()
    return len(words)

def count_letters(new_content):
    words = new_content.split()
    count_dict = {}
    for word in words:
        for letter in word:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
    return count_dict

def sort_dict(new_content):
    count_dict = count_letters(new_content)
    count_list = list(count_dict.keys())
    count_list.sort()
    new_list = []
    for item in count_list:
        if item.isalpha():
            new_list.append(item)
    sorted_dict = {item: count_dict[item] for item in new_list}
    return sorted_dict
           
def report(new_content):
    sorted_dict = sort_dict(new_content)
    for item in sorted_dict:
        print(f'The {item} character was found {sorted_dict[item]} times') 


print('--- Begin report of books/frankenstein.txt ---')
print(f'{count_words(content)} words found in the document' + '\n')
report(new_content)
print('--- End report ---')