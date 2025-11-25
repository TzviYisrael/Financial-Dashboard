### 4. Create .env file

Copy the example file and fill in the values:
```bash
cp .env.example .env
nano .env
```

**Required values:**

1. **DATABASE_URL**: Replace `YOUR_PASSWORD` with the Supabase password
   - Full URL provided by Dylan: `postgresql://postgres:qoffew-boHrij-6muwfo@db.xvudhknhpcrmqzvwqzfq.supabase.co:5432/postgres`
   
2. **SECRET_KEY**: Generate a secure key (or use a temporary one for development)
```bash
   # Generate a secure key:
   python -c "import secrets; print(secrets.token_urlsafe(32))"
```

3. **Other values**: Keep the defaults from `.env.example`

**Example .env file:**
```env
APP_NAME=Personal Portfolio Copilot API
DEBUG=True
API_VERSION=v1
HOST=0.0.0.0
PORT=8000

# Replace with real Supabase URL (ask Dylan)
DATABASE_URL=postgresql://postgres:qoffew-boHrij-6muwfo@db.xvudhknhpcrmqzvwqzfq.supabase.co:5432/postgres

# Generate your own or use this temporary one
SECRET_KEY=temporary-secret-key-for-development

ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

**⚠️ IMPORTANT:** 
- Never commit `.env` to Git (it's in `.gitignore`)
- Each team member should create their own `.env` file locally
