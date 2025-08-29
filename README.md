# HFL Reporter Web App

This is a Streamlit-based web app for generating HFL reports from KMZ files.

## Features
- Upload KMZ boundary file
- Auto-fill introduction, Table-1, Table-2, Table-3 into a DOCX master template
- Download ready-made HFL report
- Incremental ML learning: correct HFL values via feedback, model improves over time
- Stores reports metadata in SQLite DB

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Cloud / Hugging Face Spaces / Render)
- Upload all files to a GitHub repository
- Connect repository to hosting platform
- For Render, use start command:
  streamlit run app.py --server.port $PORT
