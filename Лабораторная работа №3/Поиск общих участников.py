# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, div=','):
    group1 = group1.split(div)
    group2 = group2.split(div)
    group1 = set(group1)
    group2 = set(group2)
    group3 = group1.intersection(group2)
    return sorted(list(group3))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group,'|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
