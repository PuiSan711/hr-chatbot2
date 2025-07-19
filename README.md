# Auto Global Parts Industries HR Policy Chatbot

A FastAPI chatbot that answers HR policy questions using GPT-4 and LangChain.

## How it works
- Upload HR documents (PDFs) into `docs/`
- Uses OpenAI + FAISS to provide instant policy answers
- Deployable on Render.com

## Project Structure
- main.py: FastAPI app
- requirements.txt: Dependencies
- start.sh: Startup script
- docs/: Place your HR PDFs here
