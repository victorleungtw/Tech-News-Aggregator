# Database Setup Skill

**Command:** `python -c "import sqlite3; sqlite3.connect('news.db').execute('CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, title TEXT, url TEXT UNIQUE, published_date TEXT)');"`

**Trigger:** Run this automatically when the agent detects a missing `news.db` file in the project root.
