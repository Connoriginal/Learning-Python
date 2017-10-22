
def anagram():
    print("hello")
    my_list = ["0952",'5239','1270','8581','7458','3414','7906','2356','4360','3491','6232','5927','2735','2509','5849','8457','9340','1858','8602','5784']
    sort_list = ["0952",'5239','1270','8581','7458','3414','7906','2356','4360','3491','6232','5927','2735','2509','5849','8457','9340','1858','8602','5784']
    num_list = [0]*len(my_list)
    same_list = []

    #sort the list
    for i in range(len(sort_list)):
        temp_list = []
        string = ""
        for q in range(4):
            temp_list += sort_list[i][q]
        temp_list.sort()
        for k in range(4):
            string += temp_list[k]
        sort_list[i] = string




    #find anagram
    for i in range(len(sort_list)):
        for k in range(i+1, len(sort_list)):
            if sort_list[i] == sort_list[k]:
                num_list[i] = sort_list[i]
                num_list[k] = sort_list[i]

    #print anagram
    for i in range(len(num_list)):
        if num_list[i] != 0:
            for k in range(i+1,len(num_list)):
                if num_list[i] == num_list[k]:
                    print(my_list[k], end =" ")
                    num_list[k] = 0
            print(my_list[i])
            num_list[i] = 0

anagram()
