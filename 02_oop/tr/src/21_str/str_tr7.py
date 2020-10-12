languages = "PHP Ruby Python JavaScript Perl C"
target = "y"
for language in languages.split(" "):
    if target in language:
        print(language)
