survey_results = [
    ["Python", "Javascript", "C++"], #0
    ["Python", "Javascript", "C#"],  #1
    ["Python", "Java"], #2 
    ["Python","C++","Javascript"], #3
    ["Python","Javascript","C++","Java"] #4
]

choices_sets = [set(p) for p in survey_results]
common_languages = set.intersection(*choices_sets)
print(f'Languages use all partici: {common_languages}')

languages = {}
for i in choices_sets:
    for lang in i:
        languages[lang] = languages.get(lang, 0) + 1
only_one_languages = {lang for lang, count in languages.items() if count == 1}
print(f'Languages only chosen by one participant: {only_one_languages}')

num_of_uniq = len(languages)
print(f'Number of unique languages: {num_of_uniq}')

only_one_languages = {lang for lang, count in languages.items() if count == 2}
print(f'Languages chosen by exactly two participant: {only_one_languages}')

language = {}

for i, langs in enumerate(survey_results, 1): 
    key = frozenset(langs)  # ใช้ frozenset เพื่อไม่สนลำดับ
    if key in language:
        language[key].append(i)
    else:
        language[key] = [i]

duplicate_indices = [indices for indices in language.values() if len(indices) > 1]
print(duplicate_indices)
