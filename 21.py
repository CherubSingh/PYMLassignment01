element = input("Enter the element to count: ")
lst = input("Enter the list of elements separated by spaces: ").split()
count = lst.count(element)
print(f"The element '{element}' occurs {count} times in the list.")