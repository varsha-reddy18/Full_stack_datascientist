import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def update_stock(prod_id, new_stock):
    resp = sb.table("products").update({"stock": new_stock}).eq("prod_id", prod_id).execute()
    return resp.data
if __name__ == "__main__":
    prod = input("Enter prod_id of the product to update stock: ").strip()
    new_stock = int(input("Enter new stock value: ").strip())
    updated = update_stock(prod, new_stock)
    print("Updated stock:", updated)