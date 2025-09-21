import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv() 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def borrow_book(member_id: int, book_id: int):
    try:
        response = sb.rpc('borrow_book_rpc', {
        'member_id': member_id,
        'book_id': book_id
        }).execute()
        if response.get("error"):
            print(f"Error: {response['error']['message']}")
        else:
            print("Book borrowed successfully.")

    except Exception as e:
        print("Exception occurred:", e)
if __name__ == "__main__":
    member_id = int(input("Enter Member ID: "))
    book_id = int(input("Enter Book ID: "))
    borrow_book(member_id, book_id)
