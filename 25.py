source_file = 'source.txt'  # Change this to the path of your source file
destination_file = 'destination.txt'  # Change this to the path of your destination file

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dest:
    dest.write(content)

print(f"The contents of {source_file} have been copied to {destination_file}.")