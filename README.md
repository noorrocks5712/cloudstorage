# ☁️ Cloud Storage Management System

This project is a cloud storage management system built using **FastAPI** (backend) and **Streamlit** (frontend). It provides RESTful APIs for managing users, files, storage data, and billing, along with a beautiful Streamlit interface to interact with the system.

---

## 📦 Features

- **User Management**: Add, view, update, and delete users.
- **File Management**: Upload, fetch, and list all stored files.
- **Storage Management**: Track storage usage and update allocation.
- **Billing System**: View billing details and process payments.
- **Usage Reports**: Monitor system usage and generate monthly reports.
- **Frontend**: Clean, interactive Streamlit UI for easy access.

---

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Streamlit (Python)
- **Database**: SQLite (or plug in your own)
- **Tools**: Requests, JSON, HTML/CSS for UI mockups

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cloud-storage-system.git
cd cloud-storage-system

python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For Linux/Mac
2. Create Virtual Environment (Optional but recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For Linux/Mac
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Backend (FastAPI)
bash
Copy
Edit
uvicorn main:app --reload
5. Run Frontend (Streamlit)
bash
Copy
Edit
streamlit run dashboard.py
🧪 Example CLI Commands (Simulated)
bash
Copy
Edit
# Add a user
python add_user.py --name "John Doe" --email "john@example.com" --role "Admin"

# View all users
python view_users.py

# Upload a file
python upload_file.py --filename "report.pdf"

# Check storage
python storage_usage.py

# Process a payment
python process_payment.py --amount 50
📁 Folder Structure
pgsql
Copy
Edit
📦 cloud-storage-system/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   └── database/
├── frontend/
│   └── dashboard.py
├── static/
│   └── cloud_ui.html
├── README.md
├── requirements.txt
└── .gitignore
💬 Notes
.pyc and __pycache__ are auto-generated and can be ignored or deleted.

Make sure FastAPI is running on the same API_URL used in Streamlit.

You can create HTML mockups for screenshots using the file: static/cloud_ui.html.


