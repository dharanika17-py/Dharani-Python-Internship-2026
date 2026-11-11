from storage import load_data, save_data
from users import register_user, view_users
from donation import (
    create_donation,
    view_donations,
    claim_donation,
    update_status
)


def main():
    data = load_data()

    while True:
        print("\n================================")
        print("   FOOD DONATION MANAGEMENT")
        print("================================")
        print("1. Register User")
        print("2. View Registered Users")
        print("3. Create Food Donation")
        print("4. View Available Donations")
        print("5. Claim Donation")
        print("6. Update Donation Status")
        print("7. View All Donations")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            register_user(data)

        elif choice == "2":
            view_users(data)

        elif choice == "3":
            create_donation(data)

        elif choice == "4":
            view_donations(data)

        elif choice == "5":
            claim_donation(data)

        elif choice == "6":
            update_status(data)

        elif choice == "7":
            print("\n--- ALL DONATIONS ---")
            if not data["donations"]:
                print("No donations found.")
            else:
                for donation in data["donations"]:
                    print(donation)

        elif choice == "8":
            save_data(data)
            print("Thank you for using Food Donation System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()