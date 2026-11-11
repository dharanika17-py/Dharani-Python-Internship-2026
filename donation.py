from datetime import datetime
from storage import save_data


def create_donation(data):
    print("\n--- CREATE DONATION ---")

    food = input("Food Name: ").strip()
    quantity = input("Quantity (example: 20 Meals): ").strip()
    location = input("Location: ").strip()
    available_until = input("Available Until: ").strip()
    contact = input("Contact Information: ").strip()

    if not all([food, quantity, location, available_until, contact]):
        print("All fields are required!")
        return

    donation_id = f"DON{len(data['donations']) + 1:03d}"

    donation = {
        "id": donation_id,
        "food": food,
        "quantity": quantity,
        "location": location,
        "available_until": available_until,
        "contact": contact,
        "status": "Available",
        "volunteer": None,
        "created_at": datetime.now().isoformat()
    }

    data["donations"].append(donation)
    save_data(data)

    print("Donation created successfully!")
    print("Donation ID:", donation_id)
    print("Status: Available")


def view_donations(data):
    print("\n--- AVAILABLE DONATIONS ---")

    available = [
        d for d in data["donations"]
        if d["status"] == "Available"
    ]

    if not available:
        print("No available donations.")
        return

    for d in available:
        print("\nDonation ID:", d["id"])
        print("Food:", d["food"])
        print("Quantity:", d["quantity"])
        print("Location:", d["location"])
        print("Available Until:", d["available_until"])
        print("Status:", d["status"])


def claim_donation(data):
    donation_id = input("Enter Donation ID: ").strip().upper()
    volunteer_id = input("Enter Volunteer ID: ").strip().upper()

    volunteer = next(
        (u for u in data["users"]
         if u["id"] == volunteer_id and u["role"] == "Volunteer"),
        None
    )

    if not volunteer:
        print("Valid volunteer not found!")
        return

    donation = next(
        (d for d in data["donations"] if d["id"] == donation_id),
        None
    )

    if not donation:
        print("Donation not found!")
        return

    if donation["status"] != "Available":
        print("This donation cannot be claimed.")
        return

    donation["status"] = "Claimed"
    donation["volunteer"] = volunteer_id

    save_data(data)
    print("Donation claimed successfully!")


def update_status(data):
    donation_id = input("Enter Donation ID: ").strip().upper()

    donation = next(
        (d for d in data["donations"] if d["id"] == donation_id),
        None
    )

    if not donation:
        print("Donation not found!")
        return

    next_status = {
        "Claimed": "Picked Up",
        "Picked Up": "Delivered"
    }

    current = donation["status"]

    if current not in next_status:
        print("Status cannot be updated from", current)
        return

    donation["status"] = next_status[current]
    save_data(data)

    print("New Status:", donation["status"])