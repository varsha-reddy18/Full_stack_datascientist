import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def list_books():
    print("\nList of All Books with Availability:\n")
    resp = sb.table("books").select("*").order("book_id").execute()
    books = resp.data
    for book in books:
        status = "Available " if book.get("available") else "Not Available"
        print(f"[{book['book_id']}] {book['title']} by {book['author']} - {book['category']} | {status}")
def search_books():
    query = input("\nEnter title, author, or category to search: ").strip().lower()
    print(f"\nSearch Results for: '{query}'\n")
    resp = sb.table("books").select("*").execute()
    books = resp.data
    matches = [
        b for b in books if
        query in b["title"].lower() or
        query in b["author"].lower() or
        query in b["category"].lower()
    ]
    if matches:
        for book in matches:
            status = "Available" if book.get("available") else "Not Available"
            print(f"[{book['book_id']}] {book['title']} by {book['author']} - {book['category']} | {status}")
    else:
        print("No matching books found.")
def show_member_borrowed():
    try:
        member_id = int(input("\nEnter Member ID: ").strip())
        member_resp = sb.table("members").select("*").eq("member_id", member_id).execute()
        member_data = member_resp.data
        if not member_data:
            print("Member not found.")
            return
        member = member_data[0]
        print(f"\nMember Info:\nName: {member['name']}\nEmail: {member['email']}")
        borrow_resp = sb.table("borrowed_books").select("*, books(*)").eq("member_id", member_id).execute()
        borrows = borrow_resp.data
        if borrows:
            print("\nBorrowed Books:")
            for b in borrows:
                book = b["books"]
                print(f"- {book['title']} by {book['author']} | Borrowed: {b['borrow_date']} | Returned: {b['return_date'] or 'Not returned'}")
        else:
            print("No books borrowed.")
    except ValueError:
        print("Invalid member ID.")
if __name__ == "__main__":
    products = list_books()
    for p in products:
        print(p) 
    search_books()
    show_member_borrowed()

    

