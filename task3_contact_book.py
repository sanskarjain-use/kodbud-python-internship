"""Task 3: CLI Contact Book (list of dictionaries)"""

contacts = []


def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Added {name}.")


def view_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


def search_contact():
    q = input("Search name: ").strip().lower()
    found = [c for c in contacts if q in c["name"].lower()]
    if not found:
        print("No match found.")
    for c in found:
        print(f"{c['name']} | {c['phone']} | {c['email']}")


def delete_contact():
    name = input("Name to delete: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print(f"Deleted {c['name']}.")
            return
    print("Contact not found.")


def main():
    actions = {"1": add_contact, "2": view_contacts, "3": search_contact, "4": delete_contact}
    while True:
        print("\n=== Contact Book ===\n1. Add  2. View all  3. Search  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        actions.get(choice, lambda: print("Invalid choice."))()


if __name__ == "__main__":
    main()
