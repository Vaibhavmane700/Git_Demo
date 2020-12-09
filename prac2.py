My_list = ["Vaibhav","Ankita","pranita"]
print(My_list)
print(My_list[1:])
print(My_list[-2:-1])

My_list = ['Vaibhav','Ankita','Pranita']
My_list[1] = 'Reeya'
print(My_list)

for x in My_list:
    print(x)

My_list1 = ["Vaibhav","Ankita","Pranita"]
if "Vaibhav" in My_list1:
    print("Vaibhav is in the list")


List_1 = ["Apple","Banana","Cherry"]
List_1.append("Orange")
print(List_1)

List_1.insert(1,"Mangos")
print(List_1)

List_1.remove("Banana")
print(List_1)

List_1.pop()
print(List_1)

del List_1[0]
print(List_1)

List_2 = List_1.copy()
print(List_2)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
