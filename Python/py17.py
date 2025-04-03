def translate(english_words):
    sum = ' '
    text = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
    
    translated_words = [text.get(word, word) for word in english_words] 

    return ' '.join(translated_words)


word = list('merry christmas'.split())

print(translate(word))



