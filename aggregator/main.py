import sqlite3
import feedparser
from aggregator.parser import sanitize_url

def init_db(conn):
    """Ensure the database schema exists."""
    conn.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            title TEXT,
            url TEXT UNIQUE,
            published_date TEXT
        )
    ''')
    conn.commit()

def fetch_news():
    """Fetch RSS feed, sanitize URLs, and insert into SQLite."""
    feed_url = "https://news.ycombinator.com/rss"
    print(f"Fetching news from {feed_url}...")
    feed = feedparser.parse(feed_url)

    conn = sqlite3.connect('news.db')
    init_db(conn)

    inserted_count = 0
    for entry in feed.entries:
        try:
            # Reusing the tested sanitization logic from Lesson 4
            clean_url = sanitize_url(entry.link)

            # INSERT OR IGNORE prevents duplicates based on the UNIQUE url constraint
            cursor = conn.execute(
                "INSERT OR IGNORE INTO articles (title, url, published_date) VALUES (?, ?, ?)",
                (entry.title, clean_url, entry.get('published', ''))
            )
            if cursor.rowcount > 0:
                inserted_count += 1

        except ValueError as e:
            print(f"Skipping invalid URL {entry.link}: {e}")

    conn.commit()
    conn.close()
    print(f"Successfully fetched and stored {inserted_count} new articles.")

if __name__ == "__main__":
    fetch_news()
