🔗 URL Shortener (Python + FastAPI)
A minimal URL shortening service built using FastAPI and Base62 encoding.
Stores URLs in memory — ideal for learning and quick prototyping.

🚀 Features
🔁 Converts long URLs to short Base62-encoded codes

⚡ FastAPI wrapper for easy API access

🧠 In-memory key-value store

🔠 Base62 encoding for compact, readable short codes

🏗️ Project Structure
.
├── main.py         # FastAPI routes
├── shortener.py    # URL shortening logic
├── requirements.txt
└── README.md
⚙️ Setup & Run
1. Clone the repo
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate      # on Windows use: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the FastAPI server
uvicorn app.main:app --reload

🧪 API Usage
➕ POST /shorten
Request Body

{
  "url": "https://example.com"
}
Response

{
  "short_url": "http://localhost:8000/abc123"
}
🔍 GET /{short_code}
Example

GET http://localhost:8000/abc123
Response

{
  "original_url": "https://example.com"
}

📝 Notes
Data is not persisted — restarting the app resets all data.
Uses a simple counter and Base62 encoding to generate short codes.
For production-ready systems, consider adding a database, expiration, analytics, and rate limiting.
