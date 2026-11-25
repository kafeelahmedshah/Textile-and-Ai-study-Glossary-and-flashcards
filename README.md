# Textile & AI Study Glossary & Flashcards

**Project ID:** 25TE091  
**Application:** Interactive glossary of key textile and AI terms with a search bar and quick flashcard quiz mode.

## Features

- Search textile and AI terms by name, definition, or example.
- Filter the glossary by Textile, AI, or All.
- Browse terms in alphabetical order.
- Review interactive flashcards with reveal, previous, next, and shuffle controls.
- Take a multiple-choice quiz with randomly selected questions.
- View score, percentage, and answer explanations.

## Project files

```text
textile_ai_glossary/
├── app.py
├── requirements.txt
└── README.md
```

## Run locally

### 1. Install Python
Use Python 3.9 or newer.

### 2. Open a terminal in the project folder

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will open the application in your web browser. If it does not open automatically, visit the local URL shown in the terminal (usually `http://localhost:8501`).

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `README.md` to the repository's root.
3. Sign in to Streamlit Community Cloud.
4. Select **New app**, connect your GitHub repository, and choose `app.py` as the main file.
5. Deploy the application.

## Customization

- Add more entries to the `TERMS` list in `app.py`.
- Add more multiple-choice questions to the `QUIZ` list.
- Each glossary entry uses `term`, `category`, `definition`, and `example` fields.
- Supported categories currently include `Textile` and `AI`.

## Notes

This is an educational starter application. Definitions are simplified for study purposes and should be checked against course notes or textbooks when preparing formal academic work.
