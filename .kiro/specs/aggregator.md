# Tech News Aggregator Spec

## Overview
A lightweight Python service that fetches RSS feeds from tech sources (Hacker News, TechCrunch), sanitizes the URLs, and stores them in a local SQLite database for querying.

## Core Requirements
- Python 3.12+
- Use `feedparser` for RSS parsing.
- Use `sqlite3` for local storage.
- Must include strict URL sanitization.
