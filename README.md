# Hugging Face API Proxy

This repository contains a simple example of a web application that uses a Flask server as a proxy for making API calls to Hugging Face. The user interface consists of a single `index.html` page that allows users to input text and receive generated text from Hugging Face's GPT-3 model.

## Features

- Securely store and use the Hugging Face API key
- Simple UI with a user input field, a submit button, and an output container
- Flask server as a proxy to make API calls to Hugging Face

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/huggingface-api-proxy.git
```

2. Install the required Python packages:

```bash
pip install Flask waitress
```

3. Set the Hugging Face API key as an environment variable:

```bash
export HUGGINGFACE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Hugging Face API key.

4. Run the Flask server:

```bash
python app.py
```

5. Visit `http://localhost:8080` in your web browser to use the application.

## Deployment

For deployment, make sure to securely set the `HUGGINGFACE_API_KEY` environment variable in your production environment. Check the documentation of your hosting platform for instructions on how to set environment variables.

## License

MIT License