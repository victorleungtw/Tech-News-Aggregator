# Tech News Aggregator

A lightweight, autonomous tech news aggregator built as a final exam submission for the **Kiro University Challenge 2026**.

This project fetches RSS feeds from various tech sources (like Hacker News), sanitizes the URLs using property-based testing principles, and stores the curated articles in a local SQLite database. It heavily leverages the Kiro platform's autonomous capabilities, including Model Context Protocol (MCP) servers and specialized agents.

## 🎓 Kiro Challenge Lessons Implemented

This repository satisfies the 7 core lessons of the challenge:

1. **Spec-Driven Development:** Defined in `.kiro/specs/aggregator.md`.

2. **Steering Documents:** Python coding standards enforced via `.kiro/steering/python-style.md`.

3. **Automated Hooks:** Auto-linting (Ruff) and auto-testing (Pytest) on file save via `.kiro/hooks/hooks.json`.

4. **Property-Based Testing:** Rigorous URL sanitization edge-case testing using `hypothesis` in the `tests/` directory.

5. **Modular Powers:** Automated database initialization via `.kiro/powers/plugin.json` and associated skills.

6. **Model Context Protocol (MCP):** Integration with `mcp-server-sqlite` and `mcp-server-fetch` in `mcp.json`.

7. **Custom Agents:** The `news-curator` agent configured in `.kiro/agents/news-curator.json` for autonomous pipeline execution.

## ⚙️ Prerequisites

* Python 3.12+

* `uvx` (for running MCP servers)

* Kiro CLI / IDE

## 🚀 Getting Started

1. **Clone the repository:**

   ```
   git clone
   cd Tech-News-Aggregator

   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt

   ```

3. **Initialize the Database:**
   Use the custom Kiro power to generate the SQLite schema.

   ```
   kiro run power db-setup

   ```

## 🧪 Testing

Run the property-based test suite to validate the URL sanitization logic:

```
python -m pytest tests/ -v

```

*(Note: If you are using the Kiro IDE, saving any `.py` file will automatically trigger these tests and the `ruff` linter via our custom hooks).*

## 🤖 Fetching Data & Running the Agent

To fetch the latest tech news, sanitize the links, and insert them into your local database, you can run the core Python module:

```
python -m aggregator.main

```

Alternatively, command the custom Kiro agent to execute the pipeline autonomously:

```
kiro run agent news-curator

```

You can verify the successfully curated database entries using:

```
sqlite3 news.db "SELECT title, url FROM articles LIMIT 5;"

```
