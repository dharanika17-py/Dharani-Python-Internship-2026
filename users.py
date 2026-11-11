from storage import save_data

def register_user(data):
    print("\n--- USER REGISTRATION ---")

    name = input("Enter Name: ").strip()
    role = input("Register as (Donor/Volunteer): ").strip().title()
    phone = input("Enter Contact Number: ").strip()
    location = input("Enter Location: ").strip()

    if not name or not phone or not location:
        print("All fields are required!")
        return

    if role not in ["Donor", "Volunteer"]:
        print("Please enter Donor or Volunteer.")
        return

    user_id = f"USR{len(data['users']) + 1:03d}"

    user = {
        "id": user_id,
        "name": name,
        "role": role,
        "phone": phone,
        "location": location
    }

    data["users"].append(user)
    save_data(data)

    print("Registration successful!")
    print("Your User ID:", user_id)


def view_users(data):
    print("\n--- REGISTERED USERS ---")

    if not data["users"]:
        print("No registered users.")
        return

    for user in data["users"]:
        print("\nUser ID:", user["id"])
        print("Name:", user["name"])
        print("Role:", user["role"])
        print("Contact:", user["phone"])
        print("Location:", user["location"])