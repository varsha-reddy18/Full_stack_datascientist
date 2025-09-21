import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key) 
def add_member(name,email):
    payload = {"name": name,"email":email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data
if __name__ == "__main__":
    name = input("Enter member name: ").strip()
    email=input("Enter email:").strip()
    created = add_member(name,email)
    print("Inserted:", created)
def add_books(title, author, category, stock):
    payload = {"title":title,"author":author,"category":category,"stock":stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data
if __name__ == "__main__":
    title = input("Enter book title: ").strip()
    author=input("Enter book author:").strip()
    category=input("Enter category:").strip()
    stock=int(input("Enter stock:").strip())
    created = add_books(title, author, category, stock)
    print("Inserted:", created) 