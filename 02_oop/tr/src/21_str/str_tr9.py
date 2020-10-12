text = """
Control syntax branch structure if statement. Control syntax Iterative structure while statement. Control syntax Iterative structure for statement. 
"""

words = text.strip().replace(".", "").split(" ")

word_dict = {}
for word in words:
    count = 0
    if word in word_dict:
        count = word_dict[word]
    count += 1
    word_dict[word] = count

for word, count in word_dict.items():
    print(word, count)