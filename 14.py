lines = []
print("Enter multiple lines of text (enter an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("You entered:")
for line in lines:
    print(line)