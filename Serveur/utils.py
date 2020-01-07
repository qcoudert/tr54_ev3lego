def deleteColumnContainingIP(listChecked, element):
    """Delete the IP address 'element' and the corresponding time in the list

    Used on the greenWay and orangeWay lists in main.py"""
    
    try:
        i = listChecked[0].index(element)
        listChecked[0].pop(i)
        listChecked[1].pop(i)
    except ValueError:
        return False
    return True