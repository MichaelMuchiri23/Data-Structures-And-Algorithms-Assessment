def remove_duplicates(sequence):
    list_of_elements = []
    for item in sequence:
        if item not in list_of_elements:
             list_of_elements.append(item)

    if isinstance(sequence, list):
        return list_of_elements
    else:
        return (type(sequence))(list_of_elements)     


print(remove_duplicates([1,1,2,3,3,4]))
print(remove_duplicates((1,1,2,3,3,4)))
        

   