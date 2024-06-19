main_str = input("Enter the main string: ")
sub_str = input("Enter the substring: ")
if sub_str in main_str:
    print(f"The substring '{sub_str}' is present in the main string.")
else:
    print(f"The substring '{sub_str}' is not present in the main string.")