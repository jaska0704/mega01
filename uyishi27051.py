def amal(list1, list2, list3):
    uzun_list = [{list1[i]: {list2[i]: list3[i]}} for i in range(len(list1))]
    return uzun_list

list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']
list3 = [10, 20, 30]

uzun_list = amal(list1, list2, list3)
print(uzun_list)