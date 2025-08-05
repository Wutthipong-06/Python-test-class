survey_results = [
    ["Python", "Javascript", "C++"],
    ["Python", "Javascript", "C#"],
    ["Python", "Java"],
    ["Python","C++","Javascript"],
]
all_partici = [set(i) for i in survey_results] #แปลงจาก list ให้เป็น list of set
partici = set.intersection(*all_partici)
print("chose by all partici",partici)

one_partici = set


#Output {'python} pass
#Output {'C#'}
#Output 5
#Output {'Java'}
#Output [[1,4]]