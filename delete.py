import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv() 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def delete_member(member_id):
    resp=sb.table("members").delete().eq("member_id",member_id).execute()
    return resp.data
if __name__ == "__main__":
    mid=int(input("Enter member id:").strip())
    confirm=input("Are you sure u want to delete(yes/no):").strip().lower()
    if confirm=="yes":
        delete=delete_member(mid)
        if delete:
            print("Deleted:",delete)
        else:
            print("No member deleted")
    else:
        print("Delete Cancelled")
def delete_book(book_id):
    resp=sb.table("books").delete().eq("book_id",book_id).execute()
    return resp.data
if __name__ == "__main__":
    bid=int(input("Enter book id:").strip())
    confirm=input("Are you sure u want to delete(yes/no):").strip().lower()
    if confirm=="yes":
        delete=delete_member(bid)
        if delete:
            print("Deleted:",delete)
        else:
            print("No member deleted")
    else:
        print("Delete Cancelled")