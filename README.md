# Agents for Good - EduAgent

Problem Statement

Students often struggle to get personalized learning guidance, study plans, quizzes, and career advice in one place.

EduAgent solves this problem by providing an AI-powered educational assistant using multiple specialized agents.

---

Features

- Personalized study plans
- Quiz generation
- AI tutoring and doubt solving
- Career guidance
- Multi-agent coordination
- FastAPI REST API
- Secure API key management using .env

---

Multi-Agent Architecture

Tutor Agent

Explains concepts and answers questions.

Quiz Agent

Generates quizzes and practice questions.

Planner Agent

Creates study schedules and learning roadmaps.

Career Agent

Provides career advice and resume guidance.

---

MCP Integration

EduAgent uses MCP (Model Context Protocol) server to enable communication between agents and external resources.

---

Tech Stack

- Python
- FastAPI
- Google Gemini API
- Google ADK
- MCP
- Git & GitHub

---

Project Structure

EduAgent/

├── main.py

├── app.py

├── tutor_agent.py

├── quiz_agent.py

├── planner_agent.py

├── career_agent.py

├── mcp/

│   └── server.py

├── requirements.txt

└── README.md

---

Installation

1. Clone repository

git clone YOUR_REPOSITORY_LINK

2. Install dependencies

pip install -r requirements.txt

3. Create .env file

Add your Gemini API key:

GEMINI_API_KEY=your_api_key

4. Run application

uvicorn main:app --reload

---

API Documentation

Open:

http://127.0.0.1:8000/docs

---

Future Enhancements

- Voice interaction
- PDF learning support
- Student progress tracking
- Streamlit frontend
- Vector database integration

---

Author

Jejji Shankar Rao

B.Tech CSE (AI & ML)

Malla Reddy Institute of Technology and Science

## Multi-Agent Architecture

User
  │
FastAPI Server
  │
Coordinator Agent
 ├── Tutor Agent
 ├── Career Agent
 ├── Planner Agent
 └── Quiz Agent
        │
    MCP Server
        │
Google Gemini API

