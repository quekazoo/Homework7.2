def correct_sentence():
    sentence1 = input("Введіть перше речення: ")
    sentence2 = input("Введіть друге речення: ")
    corrected_sentence1 = sentence1.capitalize()
    corrected_sentence2 = sentence2
    if not corrected_sentence2.endswith('.'):
        corrected_sentence2 += '.'
    print(f"{corrected_sentence1} {corrected_sentence2}")
correct_sentence()