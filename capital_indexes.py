def capital_indexes(word):
    myList = []
    count = 0
    for letter in word[: :1]:
        ##print("ascii value is:", ord(letter))
        if ord(letter) < 97:
            myList.append(count)
            ##print("list is:", myList)
        count += 1
        ##print("count is:", count)
    return myList