import base64
ok = 1

while ok:
    answer = int(input("Alegeti o optiune: \n1 Introducere flag\n2 Hint\n"))
    if answer == 2:
        print("\n\nTry to shuffle some words\n\n")
    elif answer == 1:
        flag = input("\n\nIntrodu flag-ul:")
        if flag == base64.b64decode("Y2NjZGRkYWFhZGRkYWJiYWE=".encode('ascii')).decode('ascii'):
            print("\n\nblack jack\n\n")
            # trb sa adaug luminite pe matrice
            ok = 0
        else:
            print("\n\nWrong flag\n\n")
            #animatie matrice cu x
    else:
        print("\n\nChoose a valid option\n\n")
