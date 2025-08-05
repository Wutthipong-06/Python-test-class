def sort_words_in_sententce(sentence):
    words = sentence.split() #การแยกคำในประโยค ให้เป็น List
    print("Origin",words)
    words.sort(key=str.lower)
    print("sorted word:",words)
    sorted_sentence = ' '.join(words)
    print(sorted_sentence)
    return sorted_sentence
sentence = "This is a man world"
sorted_result = sort_words_in_sententce(sentence)
print(f"Sorted sentence {sorted_result}")