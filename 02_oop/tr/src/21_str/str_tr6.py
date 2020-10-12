languages = "PHP Ruby Python JavaScript Perl C"
target = "P"
for language in languages.split(" "):
    if language.startswith(target):
        print(language)