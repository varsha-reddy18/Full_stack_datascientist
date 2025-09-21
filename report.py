import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
if not url or not key:
    raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in .env file")
sb: Client = create_client(url, key)
def print_table(headers, rows):
    col_widths = [len(header) for header in headers]
    for row in rows:
        for i, value in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(value)))
    header_line = " | ".join(header.ljust(col_widths[i]) for i, header in enumerate(headers))
    print("\n" + header_line)
    print("-" * len(header_line))
    for row in rows:
        row_line = " | ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(row))
        print(row_line)
    print()
def top_5_books():
    response = sb.rpc("top_5_books_rpc", {}).execute()
    if response.get("error"):
        print("Error:", response["error"]["message"])
        return

    data = response.data
    if not data:
        print("No borrowed books found.")
        return
    headers = ["Title", "Author", "Borrowed Times"]
    rows = [[d['title'], d['author'], d['borrow_count']] for d in data]
    print("Top 5 Most Borrowed Books:")
    print_table(headers, rows)
def overdue_members():
    response = sb.rpc("overdue_members_rpc", {}).execute()
    if response.get("error"):
        print("Error:", response["error"]["message"])
        return
    data = response.data
    if not data:
        print("No overdue members.")
        return
    headers = ["Name", "Email", "Book Title", "Borrow Date"]
    rows = [[d['name'], d['email'], d['title'], d['borrow_date']] for d in data]
    print("Members with Overdue Books (>14 days):")
    print_table(headers, rows)
def borrow_count_per_member():
    response = sb.rpc("borrow_count_per_member_rpc", {}).execute()
    if response.get("error"):
        print("Error:", response["error"]["message"])
        return
    data = response.data
    if not data:
        print("No borrowing records found.")
        return
    headers = ["Member Name", "Total Borrowed"]
    rows = [[d['name'], d['total_borrowed']] for d in data]
    print("Total Books Borrowed Per Member:")
    print_table(headers, rows)
if __name__ == "__main__":
    while True:
        print("\nLibrary Reports (via Supabase RPCs)")
        print("1. Top 5 Most Borrowed Books")
        print("2. Overdue Members")
        print("3. Books Borrowed Per Member")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            top_5_books()
        elif choice == "2":
            overdue_members()
        elif choice == "3":
            borrow_count_per_member()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please enter 1–4.")
