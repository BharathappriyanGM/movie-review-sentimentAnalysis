# movie-review-sentimentAnalysis

1. Project Overview:

Movie Review Analyzer is a web application that uses an ensemble of machine learning models (Logistic Regression, LSTM, and Transformer) to analyze movie reviews for sentiment and thematic content. The system provides sentiment predictions with confidence scores and identifies movie genres/themes from review text.

2. Tech Stack:

Mention the technologies used for backend, frontend, and database:

Backend: FastAPI, MongoDB, Logistic Regression, LSTM, Hugging Face.
Frontend: React, Axios.
Database: MongoDB Atlas.

3. Folder Structure:
MovieReviewProject/
│
├── backend/               # Backend folder
├── frontend/              # Frontend folder
├── nltk_data/             # NLTK language data
├── logs/                  # Logs folder (created at runtime)
├── tests/                 # Test cases for backend and frontend
├── .gitignore             # Git ignored files
├── docker-compose.yml     # Docker setup for full-stack deployment
├── README.md              # Project documentation
└── LICENSE                # License for the project

4. Getting Started:
Instructions for cloning the repository and navigating to the project folder:

git clone <repo-link>
cd MovieReviewProject

5. Setting Up Backend:

Refer to the README.md in the backend folder for detailed instructions.

6. Setting Up Frontend:

Refer to the README.md in the frontend folder for detailed instructions.

7. Running the project:

Backend:
cd backend
uvicorn main:app --reload

Frontend:
cd frontend
npm start

8. Testing:
Backend tests:
pytest tests/test_backend.py

Frontend tests:
cd frontend
npm test