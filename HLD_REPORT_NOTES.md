# HLD Report Notes

These notes are organized to match the High Level Design table of contents and can be used directly by teammates while preparing the report.

## 1. Introduction

### 1.1 Scope of the document

This document describes the high-level design of a Streamlit-based multimodal Generative AI demo for hospitality concept visualization. The system accepts a user prompt and generates both descriptive text and a concept image using external AI APIs.

### 1.2 Intended Audience

- Faculty or evaluators reviewing the architecture
- Project team members preparing presentation or report material
- Developers who want to understand the implementation
- Stakeholders interested in the solution approach

### 1.3 System overview

The system is a lightweight web application that runs locally on Streamlit. It integrates:

- Google Gemini API for text generation
- Hugging Face Stable Diffusion inference API for image generation

The application is designed as a demo-oriented proof of concept focused on simple user interaction and clear multimodal output.

## 2. System Design

### 2.1 Application Design

The application uses a simple single-tier app structure:

- Presentation layer: Streamlit UI in `app.py`
- Service layer: Gemini and Hugging Face API integrations in dedicated service files
- Shared configuration and validation utilities in helper modules
- External services: Gemini API and Hugging Face model inference endpoint

This design was chosen to keep the demo minimal, understandable, and easy to present.

### 2.2 Process Flow

1. User opens Streamlit app in browser.
2. User enters a hospitality concept prompt.
3. User clicks `Generate`.
4. Application validates the prompt.
5. Application sends prompt to Gemini API.
6. Gemini returns descriptive text.
7. Application sends same prompt to Hugging Face image API.
8. Hugging Face returns image bytes.
9. Application renders text and image in the UI.
10. If any issue occurs, the app displays an error message.

### 2.3 Information Flow

- Input source: User prompt entered in Streamlit UI
- Outbound API call 1: Prompt to Gemini text model
- Outbound API call 2: Prompt to Hugging Face Stable Diffusion model
- Inbound response 1: Generated descriptive text
- Inbound response 2: Generated image content
- Output destination: Browser UI rendered by Streamlit

### 2.4 Components Design

#### Component 1: Streamlit UI

- Collects prompt input
- Displays generate button
- Shows spinner during processing
- Displays text output
- Displays image output
- Displays error messages

#### Component 2: Gemini Text Generation

- Reads `GEMINI_API_KEY` from environment
- Creates Gemini client using `from google import genai`
- Calls `client.models.generate_content(...)`
- Returns generated text as string

#### Component 3: Hugging Face Image Generation

- Reads `HUGGINGFACE_API_KEY` from environment
- Sends HTTP POST request using `requests`
- Uses Stable Diffusion model endpoint
- Returns image bytes for display

#### Component 4: Configuration and Utilities

- Stores model names and endpoint constants
- Validates user input before making API calls

#### Component 5: External API Services

- Gemini handles text generation
- Hugging Face handles image generation

### 2.5 Key Design Considerations

- Simplicity: small modular project for quick understanding
- Demonstrability: focused on visible text and image output
- Minimal modularity: UI, service logic, config, and validation are separated
- Maintainability: short and readable code
- API-based integration: no local model hosting required
- Local deployment: suitable for classroom or presentation demo

### 2.6 API Catalogue

#### Google Gemini API

- Purpose: Generate hospitality concept description
- SDK: `google-genai`
- Method used: `client.models.generate_content`
- Model: `gemini-2.5-flash`
- Authentication: `GEMINI_API_KEY`

#### Hugging Face Inference API

- Purpose: Generate hospitality concept image
- Access method: HTTPS POST request
- Endpoint style: Hugging Face router inference endpoint
- Model: `stabilityai/stable-diffusion-xl-base-1.0`
- Authentication: `HUGGINGFACE_API_KEY`

## 3. Data Design

### 3.1 Data Model

This demo does not use a persistent database. The main data objects are transient runtime values:

- `prompt`: input text from user
- `text_result`: generated text response
- `image_result`: generated image bytes

### 3.2 Data Access Mechanism

- Prompt is collected from Streamlit input widget
- External AI services are accessed through SDK/HTTP APIs
- Returned data is used in memory only during request processing

### 3.3 Data Retention Policies

- No local persistence of prompts or outputs by default
- Data remains in process memory only for the active request/session
- Logs may exist only if manually enabled during local execution

### 3.4 Data Migration

No data migration is required because the application has no structured persistent storage.

## 4. Interfaces

The system exposes a browser-based user interface through Streamlit.

User interface elements:

- Title banner
- Prompt input box
- Generate button
- Generated text section
- Generated image section
- Error message display

External interfaces:

- Gemini API interface
- Hugging Face inference interface

## 5. State and Session Management

- Streamlit manages per-session UI state during the browser session
- The app does not maintain custom long-term session state
- Each generation request is processed independently

## 6. Caching

- No explicit caching is implemented in the current demo
- This keeps behavior simple and transparent for presentation
- Future enhancement could cache repeated prompts or generated results

## 7. Non-Functional Requirements

### 7.1 Security Aspects

- API keys are stored in environment variables, not hardcoded in code for normal use
- Sensitive credentials should not be committed to version control
- HTTPS is used for communication with external APIs
- The demo should be used only with controlled access in local development or classroom presentation setup

Recommended improvements for production:

- Secret management tool or `.env` file with secure handling
- Role-based access control
- Request logging and monitoring
- API usage throttling

### 7.2 Performance Aspects

- Application performance depends mainly on external API latency
- Gemini text generation is typically faster than image generation
- Hugging Face image generation may take longer depending on model availability and queue time
- The UI includes a spinner to indicate active processing

Potential future improvements:

- Parallel API invocation
- Response caching
- Retry logic with backoff
- Async processing for better responsiveness

## 8. References

- Streamlit documentation
- Google Gemini API Python SDK documentation
- Hugging Face Inference API documentation
- Python `requests` documentation

## Additional Notes For Report Team

- This project is best described as a proof-of-concept or demo prototype.
- Architecture is intentionally minimal to keep the implementation easy to explain.
- There is no database, no authentication layer, and no persistent storage in the current scope.
- The strongest demo value is the end-to-end multimodal flow from one prompt to two generated outputs.
