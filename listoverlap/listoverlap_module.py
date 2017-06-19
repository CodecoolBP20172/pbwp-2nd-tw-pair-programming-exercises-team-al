def listoverlap(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            if i in list3:
                pass
            else:
                list3.append(i)
    return list3


def main():
    print(listoverlap())


if __name__ == '__main__':
    main()
