
# Translation App

A Python-based translation tool built to help immigrant families navigate language barriers.

## Why I Built This

I grew up between Togo, Canada, and Atlanta — three cultures, three languages, and countless moments where words failed to bridge the gap. I watched my mother struggle with English documents, forms, and conversations that should have been simple. This app exists because I believe language should never be a barrier to access, safety, or dignity.

## What It Does

- Accepts text input and translates it to a target language
- Sanitizes input text to handle special characters, formatting issues, and edge cases
- Returns clean, readable translations through a simple API

## Tech Stack

- Python
- Flask (REST API framework)
- Custom text sanitization pipeline

## Project Structure
translation-app/
├── src/
│   ├── api/
│   │   ├── routes.py      # API endpoints
│   │   └── sanitize.py    # Text cleaning logic
│   └── backend/
│       └── translator.py  # Translation engine
├── tests/
│   └── test_sanitize.py   # Unit tests
├── requirements.txt       # Dependencies
└── README.md



What I Learned
Building this app taught me that translation is not just about converting words — it's about preserving intent across contexts. I had to design a sanitization pipeline that handles real-world messy input: mixed scripts, special characters, inconsistent formatting. That systems-thinking approach is what I bring to every project.
Future Plans
[ ] Add support for Ewe and French (my family's languages)
[ ] Deploy to a cloud platform for public access
[ ] Add voice input for non-text users
[ ] Build a mobile interface

About Me
I'm Ryan Agbobli, a rising senior at North Atlanta High School in the IB Diploma Programme. 
I plan to study Computer Science with a focus on cybersecurity at Georgia Tech. This app is one step toward my larger mission: using technology to protect and empower underserved communities.
Built with purpose. Open to collaboration.
plain

