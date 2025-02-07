# Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
with open('./ex_1/donald_speech.txt', mode='r+', encoding='utf-8') as donald_file:
    line_count = 0
    word_count = 0
    list_speech = donald_file.readlines()
    for line in list_speech:
        line_count += 1
        word_count += len(line) - line.count(' ')

    print(f'Line count: {line_count}, Word count: {word_count}')

# b) Read michelle_obama_speech.txt file and count number of lines and words
with open('./ex_1/michelle_obama_speech.txt', mode='r+', encoding='utf-8') as michelle_file:
    line_count = 0
    word_count = 0
    list_speech = michelle_file.readlines()

    for line in list_speech:
        if len(line) < 0:
            continue
        else:
            line_count += 1
            word_count += len(line) - line.count(' ')

    print(f'Line count: {line_count}, Word count: {word_count}')
# c) Read donald_speech.txt file and count number of lines and words d)
# Read melina_trump_speech.txt file and count number of lines and words

