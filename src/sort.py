def insertion_sort(items: [float]):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and key < items[j]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
        
    return items


def sort_items(items: [float]):
    items = insertion_sort(items)
    return items


