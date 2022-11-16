def count_occurrence(sentence):
    end_sentence = ""
    seps = [",", "."]
    for sep in seps:
        sentence = sentence.replace(sep, ' ')
    words_in_sentence = sentence.split()
    for currentWord in words_in_sentence:
        word_occurrence_count = 0
        for word in words_in_sentence:
            if word == currentWord:
                word_occurrence_count = word_occurrence_count + 1
        if end_sentence != "":
            end_sentence = end_sentence + ","
        end_sentence = end_sentence + currentWord + "=" + word_occurrence_count.__str__()
    return end_sentence


print(count_occurrence('Tom, eats. and, eats.'))



