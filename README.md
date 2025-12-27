# QuickNoteAI
AI-powered note-taking web application built with Flask and deployed on Azure using GitHub Actions CI/CD. Single-user, Public and with No authentication as it's only for demo.

## Features
- Create & manage notes
- AI-generated summaries using OpenAI API
- Clean, responsive UI
- Secure environment variables
- Automated CI/CD pipeline

## Tech Stack
- Flask (Python)
- OpenAI API
- SQLite
- Azure App Service
- GitHub Actions (CI/CD)

## Architecture
- Flask MVC pattern
- Environment variables for secrets
- Gunicorn production server

## CI/CD Pipeline
- Triggered on push to main
- Builds and deploys automatically to Azure Web App

## Screenshots
### Home Page
![Home Page](images/HomePage.png)

### View Page
![View Page](images/ViewPage.png)

### Create Note Page
![Create note](images/CreateNotePage.png)

## How to Run Locally
- Get GitHub code 
- You need to have OPENAI_API_KEY for your local environment. Set local environment 'setx OPENAI_API_KEY "openai api key"'.
- Run app.py 

## Live Demo
https://quicknoteai-webapp-dcc9hrdmgzf7bqdp.centralindia-01.azurewebsites.net/

## How it different from Copilot, Chatgpt and Gemini ai.
ChatGPT/Copilot/Gemini etc. are general-purpose AI tools. QuickNoteAI is a context-aware personal knowledge tool.
Example-
1. Student writes: Daily lecture notes and clicks “Weekly Summary”.
   AI generates: Key concepts, Important formulas, Exam-focused highlights
2. Developer stores: Meeting notes
   AI generates: Action items, Follow-ups, Technical summaries
ChatGPT/Copilot/Gemini etc. doesn’t remember this for them.