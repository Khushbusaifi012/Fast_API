"# Fast_API" 

🩺 REST API for Patient Records (Python Project)
This is a simple REST API built using Python to manage patient records. It reads and writes data from a patients.json file, and is structured for easy understanding and modification. Ideal for beginners learning how REST APIs work with file-based storage.

🛠 Features:-

1.Add new patient records

2.Read patient records

3.Update existing patient records

4.Delete patient records

5.Data stored in patients.json

6.CLI or basic server (depending on main.py code)

📁 Project Structure:-
REST_API

├── myvenv/               # Virtual environment (Python packages installed here)


├── main.py               # Main script for handling the API logic


├── patients.json         # JSON file where all patient data is stored


├── pyvenv.cfg            # Configuration for virtual environment


└── README.md             # Project documentation (this file)

▶️ How to Run:- 1. Clone the Repository:

 i)git clone 
 
 ii)cd REST_API

2. Set up Virtual Environment:

i)python -m venv myvenv

source myvenv/Scripts/activate   # On Windows

source myvenv/bin/activate       # On macOS/Linux

3. Install Required Packages:

pip install -r requirements.txt

4. Run the Project::

uvicorn main:app --reload

Visit the API docs in your browser:

📄 Swagger UI: http://127.0.0.1:8000/docs

📄 ReDoc: http://127.0.0.1:8000/redoc

🧪 Sample Patient JSON
{
  "p001": {
    "name": "Ananya verma",
    "city": "Guwahati",
    "age": 28,
    "gender": "female",
    "height": 1.65,
    "weight": 90,
    "bmi": 33.06
  },
