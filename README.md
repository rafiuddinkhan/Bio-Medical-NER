# Bio-Medical-NER Project

This project is designed to extract biomedical entities such as symptoms, duration, diseases, medications, and medical tests from text inputs. It utilizes the Langchain library to interact with OpenAI's GPT-3.5 Turbo model to perform the extraction and build an API for biomedical entity extraction.

## Project Structure

The project consists of the following files:

1. `bio_medical_ner_parser.py`
2. `app.py`
3. `Dockerfile`

### `parser.py`

This file contains the core logic for extracting biomedical entities from text. Here's an overview of its components:

#### Initialization and Model Selection
- The `BioMedicalParser` class is initialized, which selects the appropriate OpenAI model based on the current date.
- It sets up the ChatOpenAI instance with the chosen model.

#### Output Schema Definition
- The parser defines output schemas for different biomedical entities such as symptoms, duration, diseases, medications, and medical tests.

#### Chat Prompt Template
- A chat prompt template is defined, instructing the GPT-3.5 Turbo model to extract specific biomedical information and format the output as JSON.

#### Entity Extraction
- The `extract_biomedical_entities` method takes an input text, formats it into chat messages, sends it to the GPT-3.5 Turbo model, and then parses the model's response to extract biomedical entities.

#### Message Formatting
- The `format_messages` method prepares input text for the chat by incorporating the chat prompt template.

### `app.py`

This file contains a Flask web application that exposes an API for interacting with the biomedical entity extraction functionality defined in `parser.py`. Here's an overview:

#### Health Check Endpoint
- The `/health` endpoint checks the status of the API.

#### Bio-Medical-NER Query Endpoint
- The `/bio-medical-ner/query` endpoint expects POST requests with an `input_text` parameter.
- It calls the `extract_biomedical_entities` method from `parser.py` to extract biomedical entities from the input text.
- The extracted entities are returned as JSON in the response.

#### Error Logging
- Errors are logged to a file named `bio_medical_ner.log`.

### `Dockerfile`

This Dockerfile is used to containerize the application. It sets up the necessary environment and dependencies for running the Flask web application.

## Usage

1. Build the Docker container using the provided Dockerfile.
2. Run the container to start the Flask web application.
3. Send POST requests to the `/bio-medical-ner/query` endpoint with the `input_text` parameter to extract biomedical entities from text.

Example API Request:
```bash
curl -X POST -F "input_text=Patient has a headache and fever" http://localhost:5000/bio-medical-ner/query
```

## Dependencies

- Python 3.8
- Flask
- Langchain
- OpenAI GPT-3.5 Turbo model
- dotenv

## Environment Configuration

- The environment variables can be configured in a `.env` file.

## Running the Application

To run the application, execute the following command:

```bash
docker build -t bio-medical-ner .
docker run -p 5000:5000 bio-medical-ner
```

The API will be accessible at `http://localhost:5000`.

## Logging

Error logs are written to the `bio_medical_ner.log` file within the container.

## Health Check

You can check the health of the API by sending a GET request to `http://localhost:5000/health`.

## Contributors

- Rafi

## Inspiration

This project is based on the knowledge acquired from this course:
https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/


