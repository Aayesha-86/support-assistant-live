1. Create virtual environment:
   python -m venv .venv
   .venv\Scripts\activate  (Windows)
   source .venv/bin/activate  (Mac/Linux)

2. Install requirements:
   pip install -r requirements.txt

3. Set up your email credentials in .env file (Gmail recommended).

4. Start backend:
   python -m uvicorn backend.main:app --reload

5. Start frontend (new terminal):
   streamlit run frontend/app.py

6. Open Streamlit URL in browser:
   - Click "Fetch Real Emails" to import emails from your inbox
   - Enter Email ID and draft text, then click "Send Draft" to reply
