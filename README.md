# Random 20-Word Sentence Generator

A full-stack application that generates random 20-word sentences. Built with Next.js and FastAPI.

## Features

- Generates random 20-word sentences
- Modern, responsive UI
- Dockerized application
- Full test coverage

## Prerequisites

- Docker and Docker Compose
- Node.js (for local development)
- Python 3.11+ (for local development)

## Running the Application

### Using Docker (Recommended)

1. Clone the repository
2. Run the following command in the root directory:
   ```bash
   docker-compose up --build
   ```
3. Open your browser and navigate to `http://localhost:3000`

### Local Development

#### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## Running Tests

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## API Endpoints

- `GET /api/sentence`: Returns a random 20-word sentence 