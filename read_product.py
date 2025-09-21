import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def list_products():
    resp = sb.table("products").select("*").order("prod_id", desc=False).execute()
    return resp.data
if __name__ == "__main__":
    products = list_products()
    for p in products:
        print(p)  # prints each product as a dictionary