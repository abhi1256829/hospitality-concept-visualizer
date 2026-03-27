# Project Overview

## Project Name

Hospitality Concept Visualizer

## Purpose

The project is a simple web application that demonstrates multimodal Generative AI for hospitality concept visualization. A user enters a prompt describing a hospitality concept, and the system produces:

- a short descriptive text
- a concept image

This makes it useful for early-stage ideation, concept pitching, and demonstration of text-plus-image generation in a single flow.

## Problem Statement

Hospitality concept ideation usually requires both narrative and visual material. This demo shows how Generative AI can reduce effort by automatically creating both outputs from one prompt.

## Main Features

- Accepts a text prompt from the user
- Generates descriptive text using Google Gemini
- Generates a concept image using Hugging Face Stable Diffusion
- Displays both outputs in one Streamlit interface
- Handles empty input and API errors

## Tech Used

- Frontend/UI: Streamlit
- Backend logic: Python
- Text generation: Google Gemini API using `google-genai`
- Image generation: Hugging Face Inference API
- HTTP requests: `requests`
- Runtime: Localhost deployment for demo

## Project Structure

```text
team_handoff_demo/
|-- app.py
|-- config.py
|-- gemini_service.py
|-- image_service.py
|-- utils.py
|-- requirements.txt
|-- .env.example
|-- README.md
|-- PROJECT_OVERVIEW.md
|-- HLD_REPORT_NOTES.md
```

## Functional Flow

1. User enters a hospitality prompt.
2. User clicks `Generate`.
3. The app sends the prompt to Gemini for text generation.
4. The app sends the same prompt to Hugging Face for image generation.
5. The app displays generated text and image side by side.

## Demo Scope

This is a lightweight proof-of-concept / HLD demo and not a production system.

Included:

- UI-based prompt submission
- API-based text generation
- API-based image generation
- Local demo deployment

Not included:

- Database
- User login
- Persistent storage
- Caching layer
- Admin panel
- Analytics
- Vector database
- Model fine-tuning
