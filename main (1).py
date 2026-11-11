first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

#Combine name
full_name = f"{first_name.strip().title()} {last_name.strip().title()}"

print("\nFormatted Output: ")
print(f"Name: {full_name}")
print(f"Name Code: {full_name.upper()}")
print(f"Section: {section.strip().upper()}")
print(f"Favorite Subject: {favorite_subject.strip().title()}")
print(f"Character Count: {len(full_name)}")
