# 🧠 Resume & Cover Letter Generator using AI

A web-based tool to instantly generate professional resumes and cover letters using GPT-3.5/4.  
Simply enter your name, job title, education, and experience — and let AI craft job-ready documents for you.

## 👤 Author

**Mahimha Arun Kavitha**

---

## 🎯 Purpose

To automate the creation of professional resumes and cover letters using GPT-3.5/4 based on user input.

---

## 🚀 Key Features

- ✨ Generate Resume  
- ✉️ Generate Cover Letter  
- ➕ Add multiple experiences and education entries  
- 💡 Powered by OpenAI GPT-3.5/4  
- 🎨 Stylish UI with gradient background  

---

## 📂 Project Structure

resume_cover_ai/
├── backend/
│ ├── app.py # Flask backend with OpenAI integration
│ ├── requirements.txt # Flask + openai
│ └── .env # Contains your OpenAI API key
│
├── frontend/
│ └── ibm.html # UI with JS logic and styling
│
├── README.md # ← You’re here


---

⚙️ How to Run Locally
1. Clone this repo
 git clone https://github.com/Mahimha13/resume-cover-ai.git cd resume-cover-ai 
2. Set up Python backend
 cd backend python3 -m venv venv source venv/bin/activate pip install -r requirements.txt 
3. Add your .env file with OpenAI key
 Create a `.env` file in the `backend/` folder with: OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
4. Run Flask server
python app.py
5. Open the frontend
 cd frontend open ibm.html   # Or double-click to open in browser 


📜 License
This project is open source and created for educational/demo purposes.
