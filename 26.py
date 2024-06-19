user_input = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

starts_with = user_input.startswith(prefix)
ends_with = user_input.endswith(suffix)

print(f"Does the string start with '{prefix}'? {'Yes' if starts_with else 'No'}")
print(f"Does the string end with '{suffix}'? {'Yes' if ends_with else 'No'}")