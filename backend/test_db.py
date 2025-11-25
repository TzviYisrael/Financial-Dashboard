import psycopg2
from dotenv import load_dotenv
import os

# Charge .env
load_dotenv()

# Connexion to Supabase
try:
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    
    # Test : 
    cursor.execute("SELECT email, created_at FROM users LIMIT 5;")
    users = cursor.fetchall()
    
    print("✅ Supabase !")
    print(f"📊 Number of user: {len(users)}")
    print("\n👥 Users :")
    for user in users:
        print(f"  - {user[0]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Problem of connexion: {e}")

