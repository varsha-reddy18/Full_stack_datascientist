import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def delete_product(prod_id):
    resp=sb.table("products").delete().eq("prod_id",prod_id).execute()
    return resp.data
if __name__ == "__main__":
    pid=int(input("Enter product id:").strip())
    confirm=input("Are you sure u want to delete(yes/no):").strip().lower()
    if confirm=="yes":
        delete=delete_product(pid)
        if delete:
            print("Deleted:",delete)
        else:
            print("No product deleted")
    else:
        print("Delete Cancelled")