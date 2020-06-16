
favourite_languages = {
    'julu': ['python', 'c'],
    'mithila': ['java', 'java script'],
    'bornav': ['python'],
    'amit': ['java', 'java script'],
    'afra': ['c', 'c++'],
    'bristy': ['c++'],
    'mostahid': ['c', 'c++']
}

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favourite languages are: ")
        for language in languages:
            print(language)
    else:
        print("\n" + name.title() + "'s favourite language is: ")
        for language in languages:
            print(language)

