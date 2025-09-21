import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def return_book(record_id: int):
    try:
        response = sb.rpc('return_book_rpc', {'record_id': record_id}).execute()
        if response.get("error"):
            print(f"Error: {response['error']['message']}")
        else:
            print("Book returned successfully.")
    except Exception as e:
        print("Exception occurred:", e)
if __name__ == "__main__":
    record_id = int(input("Borrow Record ID: "))
    return_book(record_id)
