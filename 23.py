def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Convert from (C)elsius or (F)ahrenheit? Enter C or F: ").upper()
temp = float(input("Enter the temperature: "))

if choice == 'C':
    print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp):.2f}°F")
elif choice == 'F':
    print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp):.2f}°C")
else:
    print("Invalid choice.")