# Contact Management Application

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email
    }
    contacts.append(contact)
    print(f"Contact for {name} added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    print()


def update_contact():
    view_contacts()
    if not contacts:
        return

    index = int(input("Enter the contact number's index to update: ")) - 1

    if 0 <= index < len(contacts):
        name = input("Enter new name (leave blank to keep current): ") or contacts[index]["Name"]
        phone = input("Enter new phone number (leave blank to keep current): ") or contacts[index]["Phone"]
        email = input("Enter new email (leave blank to keep current): ") or contacts[index]["Email"]

        contacts[index].update({"Name": name, "Phone": phone, "Email": email})
        print(f"Contact updated successfully!\n")
    else:
        print("Invalid contact number.\n")


def delete_contact():
    view_contacts()
    if not contacts:
        return

    index = int(input("Enter the contact number's index to delete: ")) - 1

    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Contact for {deleted_contact['Name']} deleted successfully!\n")
    else:
        print("Invalid contact number.\n")


def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()