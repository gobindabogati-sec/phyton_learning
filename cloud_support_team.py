import random
from datetime import datetime, timedelta


# Stores all service desk tickets
tickets = {}

# Stores ticket submission order
ticket_order = []


def display_menu():
    """Display the main service desk menu."""
    print("\n" + "=" * 55)
    print("        CLOUD SUPPORT IT SERVICE DESK")
    print("=" * 55)
    print("1. Submit a new ticket")
    print("2. Check ticket status")
    print("3. Update ticket status")
    print("4. View unresolved tickets")
    print("5. View closed tickets")
    print("6. View all tickets")
    print("7. Exit")
    print("=" * 55)


def generate_ticket_number():
    """Generate a unique ticket number."""
    ticket_number = random.randint(1000, 9999)

    while ticket_number in tickets:
        ticket_number = random.randint(1000, 9999)

    return ticket_number


def select_cloud_service():
    """Allow the user to select the affected cloud service."""
    print("\nCloud Service:")
    print("1. Cloud Storage")
    print("2. Virtual Machine")
    print("3. Cloud Network")
    print("4. Cloud Database")
    print("5. Cloud Security")
    print("6. Other")

    while True:
        choice = input("Select the affected service (1-6): ")

        if choice == "1":
            return "Cloud Storage"
        elif choice == "2":
            return "Virtual Machine"
        elif choice == "3":
            return "Cloud Network"
        elif choice == "4":
            return "Cloud Database"
        elif choice == "5":
            return "Cloud Security"
        elif choice == "6":
            return "Other"
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


def select_urgency():
    """Classify the ticket according to its urgency."""
    print("\nTicket Urgency:")
    print("1. Low - Minor issue with no operational impact")
    print("2. Medium - Moderate issue with partial impact")
    print("3. High - Critical issue or cloud service outage")

    while True:
        choice = input("Select urgency (1-3): ")

        if choice == "1":
            return "Low"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "High"
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def get_deadline_hours(priority):
    """Get the response deadline hours based on priority."""
    if priority == "High":
        return 2  # 2 hours for critical issues
    elif priority == "Medium":
        return 8  # 8 hours for moderate issues
    else:  # Low
        return 24  # 24 hours for low priority issues


def is_ticket_overdue(ticket):
    """Check if a ticket is overdue (unresolved and past its deadline)."""
    if ticket["status"] == "Closed":
        return False
    return datetime.now() > ticket["deadline"]


def submit_ticket():
    """Create and store a new cloud support ticket."""
    print("\n--- SUBMIT NEW CLOUD SUPPORT TICKET ---")

    employee_name = input("Enter employee name: ").strip()

    while employee_name == "":
        print("Employee name cannot be empty.")
        employee_name = input("Enter employee name: ").strip()

    service = select_cloud_service()

    description = input("Describe the issue: ").strip()

    while description == "":
        print("Issue description cannot be empty.")
        description = input("Describe the issue: ").strip()

    urgency = select_urgency()

    ticket_number = generate_ticket_number()

    # Store datetime object for calculations
    submission_time = datetime.now()

    # Calculate deadline based on priority
    deadline_hours = get_deadline_hours(urgency)
    deadline = submission_time + timedelta(hours=deadline_hours)

    # Store ticket information in a dictionary
    tickets[ticket_number] = {
        "ticket_number": ticket_number,
        "employee_name": employee_name,
        "service": service,
        "description": description,
        "status": "Open",
        "priority": urgency,
        "created": submission_time,  # Store datetime object
        "deadline": deadline  # Store deadline datetime
    }

    # Store ticket number in submission order
    ticket_order.append(ticket_number)

    print("\nTicket submitted successfully.")
    print("Ticket Number:", ticket_number)
    print("Priority:", urgency)
    print("Status: Open")
    print("Created:", submission_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Response Deadline:", deadline.strftime("%Y-%m-%d %H:%M:%S"))


def find_ticket():
    """Find a ticket using its ticket number."""
    while True:
        ticket_input = input("Enter ticket number (or 0 to return): ")

        if ticket_input == "0":
            return None

        if ticket_input.isdigit():
            ticket_number = int(ticket_input)

            if ticket_number in tickets:
                return ticket_number
            else:
                print("Ticket not found. Please check the ticket number.")
        else:
            print("Please enter a valid ticket number.")


def check_ticket_status():
    """Display the details and current status of a ticket."""
    print("\n--- CHECK TICKET STATUS ---")

    ticket_number = find_ticket()

    if ticket_number is None:
        return

    # Reuse display_ticket for consistent output
    display_ticket(tickets[ticket_number])


def update_ticket_status():
    """Update the status of an existing ticket."""
    print("\n--- UPDATE TICKET STATUS ---")

    ticket_number = find_ticket()

    if ticket_number is None:
        return

    ticket = tickets[ticket_number]

    print("\nCurrent Status:", ticket["status"])

    # Guard against updating closed tickets
    if ticket["status"] == "Closed":
        print("\nThis ticket is already closed and cannot be updated.")
        return

    print("\nSelect new status:")
    print("1. Open")
    print("2. In Progress")
    print("3. Closed")

    while True:
        choice = input("Select status (1-3): ")

        if choice == "1":
            new_status = "Open"
            break
        elif choice == "2":
            new_status = "In Progress"
            break
        elif choice == "3":
            new_status = "Closed"
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    ticket["status"] = new_status

    print("\nTicket status updated successfully.")
    print("Ticket Number:", ticket_number)
    print("New Status:", new_status)


def display_ticket(ticket):
    """Display a ticket in a consistent format."""
    print("-" * 55)
    print("Ticket Number:", ticket["ticket_number"])
    print("Employee:", ticket["employee_name"])
    print("Cloud Service:", ticket["service"])
    print("Description:", ticket["description"])
    print("Priority:", ticket["priority"])
    print("Status:", ticket["status"])
    print("Created:", ticket["created"].strftime("%Y-%m-%d %H:%M:%S"))
    print("Deadline:", ticket["deadline"].strftime("%Y-%m-%d %H:%M:%S"))

    # Single source of truth for overdue check
    if is_ticket_overdue(ticket):
        print("** OVERDUE **")


def view_unresolved_tickets():
    """Display all tickets that are not closed, ordered by priority."""
    print("\n--- UNRESOLVED CLOUD SUPPORT TICKETS ---")

    found_ticket = False
    priority_order = ["High", "Medium", "Low"]

    # Loop through priorities in order: High, Medium, Low
    for priority in priority_order:
        for ticket_number in ticket_order:
            ticket = tickets[ticket_number]

            # Only show unresolved tickets with matching priority
            if ticket["status"] != "Closed" and ticket["priority"] == priority:
                display_ticket(ticket)
                found_ticket = True

    if not found_ticket:
        print("There are currently no unresolved tickets.")


def view_closed_tickets():
    """Display all closed tickets."""
    print("\n--- CLOSED CLOUD SUPPORT TICKETS ---")

    found_ticket = False

    for ticket_number in ticket_order:
        ticket = tickets[ticket_number]

        if ticket["status"] == "Closed":
            display_ticket(ticket)
            found_ticket = True

    if not found_ticket:
        print("There are currently no closed tickets.")


def view_all_tickets():
    """Display every ticket in the system."""
    print("\n--- ALL CLOUD SUPPORT TICKETS ---")

    if len(ticket_order) == 0:
        print("No tickets have been submitted.")
        return

    for ticket_number in ticket_order:
        display_ticket(tickets[ticket_number])


def main():
    """Run the Cloud Support Service Desk system."""
    print("\nWelcome to the Cloud Support IT Service Desk!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            submit_ticket()

        elif choice == "2":
            check_ticket_status()

        elif choice == "3":
            update_ticket_status()

        elif choice == "4":
            view_unresolved_tickets()

        elif choice == "5":
            view_closed_tickets()

        elif choice == "6":
            view_all_tickets()

        elif choice == "7":
            print("\nThank you for using the Cloud Support IT Service Desk.")
            print("System closed successfully.")
            break

        else:
            print("\nInvalid choice. Please select an option from 1 to 7.")


# Start the program with standard Python convention
if __name__ == "__main__":
    main()