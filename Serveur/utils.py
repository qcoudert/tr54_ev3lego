def deleteColumnContainingIP(listChecked, element):
    try:
        i = listChecked[0].index(element)
        listChecked[0].pop(i)
        listChecked[1].pop(i)
    except ValueError:
        return False
    return True