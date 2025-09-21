import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def update_stock(book_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id",book_id).execute()
    return resp.data
if __name__ == "__main__":
    prod = input("Enter book_id to update stock: ").strip()
    new_stock = int(input("Enter new stock value: ").strip())
    updated = update_stock(prod, new_stock)
    print("Updated stock:", updated)
def update_member(member_id, new_email):
    resp = sb.table("members").update({"email": new_email}).eq("member_id",member_id).execute()
    return resp.data
if __name__ == "__main__":
    id= input("Enter member_id to update email: ").strip()
    new_email = input("Enter new stock email: ").strip()
    updated = update_member(id, new_email)
    print("Updated Email:", updated)