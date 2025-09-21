
import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def add_product(prod_id,name,price,stock):
    payload = {"prod_id":prod_id,"name": name,"price": price, "stock": stock,"category":"electronics"}
    resp = sb.table("products").insert(payload).execute()
    return resp.data
 
if __name__ == "__main__":
    prod=int(input("Enter product id:").strip())
    name = input("Enter product name: ").strip()
    price = float(input("Enter price: ").strip())
    stock = int(input("Enter stock: ").strip())
    created = add_product(prod,name,price,stock)
    print("Inserted:", created)
 