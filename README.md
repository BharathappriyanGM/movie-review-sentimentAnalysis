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
```
movie-review-sentimentAnalysis
├─ backend
│  ├─ create_tokenizer.py
│  ├─ database
│  │  ├─ mongodb.py
│  │  └─ schemas.py
│  ├─ main.py
│  ├─ README.md
│  ├─ requirements.txt
│  └─ utils
│     ├─ ensemble.py
│     └─ preprocess.py
├─ data
├─ docker-compose.yml
├─ frontend
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ index.html
│  │  └─ manifest.json
│  ├─ README.md
│  └─ src
│     ├─ App.css
│     ├─ App.js
│     ├─ components
│     │  ├─ AdminPanel.js
│     │  ├─ Analyzer.css
│     │  ├─ Analyzer.js
│     │  ├─ Dashboard.js
│     │  ├─ Home.css
│     │  ├─ Home.js
│     │  ├─ Navbar.css
│     │  └─ Navbar.js
│     ├─ index.js
│     └─ services
│        └─ api.js
├─ LICENSE
├─ nltk_data
│  ├─ corpora
│  │  ├─ stopwords
│  │  │  ├─ albanian
│  │  │  ├─ arabic
│  │  │  ├─ azerbaijani
│  │  │  ├─ basque
│  │  │  ├─ belarusian
│  │  │  ├─ bengali
│  │  │  ├─ catalan
│  │  │  ├─ chinese
│  │  │  ├─ danish
│  │  │  ├─ dutch
│  │  │  ├─ english
│  │  │  ├─ finnish
│  │  │  ├─ french
│  │  │  ├─ german
│  │  │  ├─ greek
│  │  │  ├─ hebrew
│  │  │  ├─ hinglish
│  │  │  ├─ hungarian
│  │  │  ├─ indonesian
│  │  │  ├─ italian
│  │  │  ├─ kazakh
│  │  │  ├─ nepali
│  │  │  ├─ norwegian
│  │  │  ├─ portuguese
│  │  │  ├─ README
│  │  │  ├─ romanian
│  │  │  ├─ russian
│  │  │  ├─ slovene
│  │  │  ├─ spanish
│  │  │  ├─ swedish
│  │  │  ├─ tajik
│  │  │  ├─ tamil
│  │  │  └─ turkish
│  │  ├─ stopwords.zip
│  │  └─ wordnet.zip
│  └─ tokenizers
│     ├─ punkt
│     │  ├─ czech.pickle
│     │  ├─ danish.pickle
│     │  ├─ dutch.pickle
│     │  ├─ english.pickle
│     │  ├─ estonian.pickle
│     │  ├─ finnish.pickle
│     │  ├─ french.pickle
│     │  ├─ german.pickle
│     │  ├─ greek.pickle
│     │  ├─ italian.pickle
│     │  ├─ malayalam.pickle
│     │  ├─ norwegian.pickle
│     │  ├─ polish.pickle
│     │  ├─ portuguese.pickle
│     │  ├─ PY3
│     │  │  ├─ czech.pickle
│     │  │  ├─ danish.pickle
│     │  │  ├─ dutch.pickle
│     │  │  ├─ english.pickle
│     │  │  ├─ estonian.pickle
│     │  │  ├─ finnish.pickle
│     │  │  ├─ french.pickle
│     │  │  ├─ german.pickle
│     │  │  ├─ greek.pickle
│     │  │  ├─ italian.pickle
│     │  │  ├─ malayalam.pickle
│     │  │  ├─ norwegian.pickle
│     │  │  ├─ polish.pickle
│     │  │  ├─ portuguese.pickle
│     │  │  ├─ README
│     │  │  ├─ russian.pickle
│     │  │  ├─ slovene.pickle
│     │  │  ├─ spanish.pickle
│     │  │  ├─ swedish.pickle
│     │  │  └─ turkish.pickle
│     │  ├─ README
│     │  ├─ russian.pickle
│     │  ├─ slovene.pickle
│     │  ├─ spanish.pickle
│     │  ├─ swedish.pickle
│     │  └─ turkish.pickle
│     ├─ punkt.zip
│     ├─ punkt_tab
│     │  ├─ czech
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ danish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ dutch
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ english
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ estonian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ finnish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ french
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ german
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ greek
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ italian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ malayalam
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ norwegian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ polish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ portuguese
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ README
│     │  ├─ russian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ slovene
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ spanish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ swedish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  └─ turkish
│     │     ├─ abbrev_types.txt
│     │     ├─ collocations.tab
│     │     ├─ ortho_context.tab
│     │     └─ sent_starters.txt
│     └─ punkt_tab.zip
├─ README.md
├─ s_a.py
└─ tests
   ├─ test_backend.py
   └─ test_frontend.js

```
```
movie-review-sentimentAnalysis
├─ backend
│  ├─ create_tokenizer.py
│  ├─ database
│  │  ├─ mongodb.py
│  │  └─ schemas.py
│  ├─ fix_tokenizer.py
│  ├─ main.py
│  ├─ README.md
│  ├─ requirements.txt
│  └─ utils
│     ├─ ensemble.py
│     └─ preprocess.py
├─ data
├─ docker-compose.yml
├─ frontend
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ index.html
│  │  └─ manifest.json
│  ├─ README.md
│  └─ src
│     ├─ App.css
│     ├─ App.js
│     ├─ components
│     │  ├─ AdminPanel.js
│     │  ├─ Analyzer.css
│     │  ├─ Analyzer.js
│     │  ├─ Dashboard.js
│     │  ├─ Home.css
│     │  ├─ Home.js
│     │  ├─ Navbar.css
│     │  └─ Navbar.js
│     ├─ index.js
│     └─ services
│        └─ api.js
├─ LICENSE
├─ nltk_data
│  ├─ corpora
│  │  ├─ stopwords
│  │  │  ├─ albanian
│  │  │  ├─ arabic
│  │  │  ├─ azerbaijani
│  │  │  ├─ basque
│  │  │  ├─ belarusian
│  │  │  ├─ bengali
│  │  │  ├─ catalan
│  │  │  ├─ chinese
│  │  │  ├─ danish
│  │  │  ├─ dutch
│  │  │  ├─ english
│  │  │  ├─ finnish
│  │  │  ├─ french
│  │  │  ├─ german
│  │  │  ├─ greek
│  │  │  ├─ hebrew
│  │  │  ├─ hinglish
│  │  │  ├─ hungarian
│  │  │  ├─ indonesian
│  │  │  ├─ italian
│  │  │  ├─ kazakh
│  │  │  ├─ nepali
│  │  │  ├─ norwegian
│  │  │  ├─ portuguese
│  │  │  ├─ README
│  │  │  ├─ romanian
│  │  │  ├─ russian
│  │  │  ├─ slovene
│  │  │  ├─ spanish
│  │  │  ├─ swedish
│  │  │  ├─ tajik
│  │  │  ├─ tamil
│  │  │  └─ turkish
│  │  ├─ stopwords.zip
│  │  └─ wordnet.zip
│  └─ tokenizers
│     ├─ punkt
│     │  ├─ czech.pickle
│     │  ├─ danish.pickle
│     │  ├─ dutch.pickle
│     │  ├─ english.pickle
│     │  ├─ estonian.pickle
│     │  ├─ finnish.pickle
│     │  ├─ french.pickle
│     │  ├─ german.pickle
│     │  ├─ greek.pickle
│     │  ├─ italian.pickle
│     │  ├─ malayalam.pickle
│     │  ├─ norwegian.pickle
│     │  ├─ polish.pickle
│     │  ├─ portuguese.pickle
│     │  ├─ PY3
│     │  │  ├─ czech.pickle
│     │  │  ├─ danish.pickle
│     │  │  ├─ dutch.pickle
│     │  │  ├─ english.pickle
│     │  │  ├─ estonian.pickle
│     │  │  ├─ finnish.pickle
│     │  │  ├─ french.pickle
│     │  │  ├─ german.pickle
│     │  │  ├─ greek.pickle
│     │  │  ├─ italian.pickle
│     │  │  ├─ malayalam.pickle
│     │  │  ├─ norwegian.pickle
│     │  │  ├─ polish.pickle
│     │  │  ├─ portuguese.pickle
│     │  │  ├─ README
│     │  │  ├─ russian.pickle
│     │  │  ├─ slovene.pickle
│     │  │  ├─ spanish.pickle
│     │  │  ├─ swedish.pickle
│     │  │  └─ turkish.pickle
│     │  ├─ README
│     │  ├─ russian.pickle
│     │  ├─ slovene.pickle
│     │  ├─ spanish.pickle
│     │  ├─ swedish.pickle
│     │  └─ turkish.pickle
│     ├─ punkt.zip
│     ├─ punkt_tab
│     │  ├─ czech
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ danish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ dutch
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ english
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ estonian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ finnish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ french
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ german
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ greek
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ italian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ malayalam
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ norwegian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ polish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ portuguese
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ README
│     │  ├─ russian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ slovene
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ spanish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ swedish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  └─ turkish
│     │     ├─ abbrev_types.txt
│     │     ├─ collocations.tab
│     │     ├─ ortho_context.tab
│     │     └─ sent_starters.txt
│     └─ punkt_tab.zip
├─ README.md
├─ s_a.py
└─ tests
   ├─ test_backend.py
   └─ test_frontend.js

```
```
movie-review-sentimentAnalysis
├─ backend
│  ├─ create_tokenizer.py
│  ├─ database
│  │  ├─ mongodb.py
│  │  └─ schemas.py
│  ├─ fix_tokenizer.py
│  ├─ main.py
│  ├─ README.md
│  ├─ requirements.txt
│  └─ utils
│     ├─ ensemble.py
│     └─ preprocess.py
├─ data
├─ docker-compose.yml
├─ frontend
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ index.html
│  │  └─ manifest.json
│  ├─ README.md
│  └─ src
│     ├─ App.css
│     ├─ App.js
│     ├─ components
│     │  ├─ AdminPanel.js
│     │  ├─ Analyzer.css
│     │  ├─ Analyzer.js
│     │  ├─ Dashboard.js
│     │  ├─ Home.css
│     │  ├─ Home.js
│     │  ├─ Navbar.css
│     │  └─ Navbar.js
│     ├─ index.js
│     └─ services
│        └─ api.js
├─ LICENSE
├─ nltk_data
│  ├─ corpora
│  │  ├─ stopwords
│  │  │  ├─ albanian
│  │  │  ├─ arabic
│  │  │  ├─ azerbaijani
│  │  │  ├─ basque
│  │  │  ├─ belarusian
│  │  │  ├─ bengali
│  │  │  ├─ catalan
│  │  │  ├─ chinese
│  │  │  ├─ danish
│  │  │  ├─ dutch
│  │  │  ├─ english
│  │  │  ├─ finnish
│  │  │  ├─ french
│  │  │  ├─ german
│  │  │  ├─ greek
│  │  │  ├─ hebrew
│  │  │  ├─ hinglish
│  │  │  ├─ hungarian
│  │  │  ├─ indonesian
│  │  │  ├─ italian
│  │  │  ├─ kazakh
│  │  │  ├─ nepali
│  │  │  ├─ norwegian
│  │  │  ├─ portuguese
│  │  │  ├─ README
│  │  │  ├─ romanian
│  │  │  ├─ russian
│  │  │  ├─ slovene
│  │  │  ├─ spanish
│  │  │  ├─ swedish
│  │  │  ├─ tajik
│  │  │  ├─ tamil
│  │  │  └─ turkish
│  │  ├─ stopwords.zip
│  │  └─ wordnet.zip
│  └─ tokenizers
│     ├─ punkt
│     │  ├─ czech.pickle
│     │  ├─ danish.pickle
│     │  ├─ dutch.pickle
│     │  ├─ english.pickle
│     │  ├─ estonian.pickle
│     │  ├─ finnish.pickle
│     │  ├─ french.pickle
│     │  ├─ german.pickle
│     │  ├─ greek.pickle
│     │  ├─ italian.pickle
│     │  ├─ malayalam.pickle
│     │  ├─ norwegian.pickle
│     │  ├─ polish.pickle
│     │  ├─ portuguese.pickle
│     │  ├─ PY3
│     │  │  ├─ czech.pickle
│     │  │  ├─ danish.pickle
│     │  │  ├─ dutch.pickle
│     │  │  ├─ english.pickle
│     │  │  ├─ estonian.pickle
│     │  │  ├─ finnish.pickle
│     │  │  ├─ french.pickle
│     │  │  ├─ german.pickle
│     │  │  ├─ greek.pickle
│     │  │  ├─ italian.pickle
│     │  │  ├─ malayalam.pickle
│     │  │  ├─ norwegian.pickle
│     │  │  ├─ polish.pickle
│     │  │  ├─ portuguese.pickle
│     │  │  ├─ README
│     │  │  ├─ russian.pickle
│     │  │  ├─ slovene.pickle
│     │  │  ├─ spanish.pickle
│     │  │  ├─ swedish.pickle
│     │  │  └─ turkish.pickle
│     │  ├─ README
│     │  ├─ russian.pickle
│     │  ├─ slovene.pickle
│     │  ├─ spanish.pickle
│     │  ├─ swedish.pickle
│     │  └─ turkish.pickle
│     ├─ punkt.zip
│     ├─ punkt_tab
│     │  ├─ czech
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ danish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ dutch
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ english
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ estonian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ finnish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ french
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ german
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ greek
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ italian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ malayalam
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ norwegian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ polish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ portuguese
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ README
│     │  ├─ russian
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ slovene
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ spanish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  ├─ swedish
│     │  │  ├─ abbrev_types.txt
│     │  │  ├─ collocations.tab
│     │  │  ├─ ortho_context.tab
│     │  │  └─ sent_starters.txt
│     │  └─ turkish
│     │     ├─ abbrev_types.txt
│     │     ├─ collocations.tab
│     │     ├─ ortho_context.tab
│     │     └─ sent_starters.txt
│     └─ punkt_tab.zip
├─ README.md
├─ s_a.py
└─ tests
   ├─ test_backend.py
   └─ test_frontend.js

```