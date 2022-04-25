# 1 downloaded from https://github.com/almgru/svenska-ord.txt/blob/master/svenska-ord.txt
# 2 downloaded from https://github.com/titoBouzout/Dictionaries/blob/master/Swedish.dic
swedish_dict_filename_1 = "svenska-ord.txt"
swedish_dict_filename_2 = "Swedish.dic.txt"

def read_dictionary_txt_as_list(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            line_content = line.rstrip().split("/")
            word_part = line_content[0]
            if "-" in word_part or " " in word_part:
                continue
            
            lines.append(word_part.lower())
    return lines

word_list_1 = read_dictionary_txt_as_list(swedish_dict_filename_1)
word_list_2 = read_dictionary_txt_as_list(swedish_dict_filename_2)

unique_words = []

for i,word1 in enumerate(word_list_1):
    if not word1 in word_list_2:
        unique_words.append(word1)