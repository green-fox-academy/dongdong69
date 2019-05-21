def anagram(word, other_word):
    word_dic = word_to_dic(word)
    other_word_dic = word_to_dic(other_word)

    return word_dic == other_word_dic

def word_to_dic(word):
    word_dic = {}
    for char in word:
        if char not in word_dic:
            word_dic[char] = 1
        else:
            word_dic[char] += 1

    return word_dic