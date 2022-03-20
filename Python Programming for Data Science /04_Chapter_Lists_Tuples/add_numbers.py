list1 = ['4', '3', '5']
list2 = ['6', '2', '1']
list1.reverse()
list2.reverse()
print(list1)

list1_com = int(list1[0] + list1[1] + list1[2])
list2_com = int(list2[0] + list2[1] + list2[2])
print(list1_com)


int_list1 = [int(i) for i in list1]
int_list2 = [int(i) for i in list2]
add_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if i ==j:
            add_list.append(int_list1[i] + int_list2[j])

print(add_list)

print(int_list2)
