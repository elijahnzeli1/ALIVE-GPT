# NEN-AI: Next-Generation Generative AI Project

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Project Structure](#project-structure)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

## Introduction

NEN-AI is a cutting-edge Generative AI project that leverages modern APIs and machine learning techniques to create a powerful text generation system. This project aims to provide a flexible and extensible framework for various generative AI tasks.

## Features

- Text generation using state-of-the-art language models
- RESTful API for easy integration with other applications
- Web interface for interactive text generation
- Extensible architecture for adding new AI models and capabilities
- Comprehensive logging and error handling
- Containerized application for easy deployment

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher
- pip (Python package manager)
- Git
- Docker (for containerized deployment)

## Installation

1. Clone the repository:

   git clone <https://github.com/elijahnzeli1/NEN-AI.git>
   cd NEN-AI

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:

   pip install -r requirements.txt

## Configuration

1. Copy the example environment file and edit it with your settings:

   cp .env.example .env

2. Open `.env` in a text editor and set the following variables:
   - `SECRET_KEY`: A secret key for Flask sessions
   - `DATABASE_URL`: The URL for your database
   - `AI_MODEL_PATH`: Path to your pre-trained AI model (if applicable)

## Running the Application

1. Initialize the database:

   - flask db init
   - flask db migrate
   - flask db upgrade

    ('windows powershell')

   - $env:FLASK_APP = "api"
   - flask db init
   - flask db migrate
   - flask db upgrade
   or
   flask --app api db init
   flask --app api db migrate
   flask --app api db upgrade

2. Run the development server:

   python scripts/run_server.py

3. Open a web browser and navigate to `http://localhost:5000` to use the application.

## Preparing Advanced Data

To prepare advanced data for training, including data for reinforcement learning:

1. Place your raw text files in the `data/raw` directory.

2. Run the advanced data preparation script:

   - python scripts/prepare_advanced_data.py

This will create the following files in the `data/processed` directory:

- `advanced_train.txt`: Advanced training data with metadata
- `advanced_valid.txt`: Advanced validation data with metadata
- `rl_data.txt`: Data prepared for reinforcement learning

1. You can now use these files for advanced training and reinforcement learning tasks.

- By placing the code in [scripts/prepare_advanced_data.py], you're keeping it separate from the basic preprocessing script while still making it easily accessible within your project structure. This allows you to run advanced data preparation when needed without interfering with the basic functionality of your project.

- Remember to adapt the [ai_engine/training.py] and other relevant files to make use of this new advanced data when you're ready to implement more sophisticated training techniques.

## Fine-tuning the Model

To fine-tune the model on your own data:

1. Prepare your data:
   - Place your raw text files in the `data/raw` directory.
   - Run the preprocessing script:

     python scripts/preprocess_data.py

   This will create `train.txt` and `valid.txt` in the `data/processed` directory.

2. Run the fine-tuning script:
   - python scripts/fine_tuning.py

3. The fine-tuned model will be saved in the `./fine_tuned_model` directory.

4. Restart the application to use the fine-tuned model for generation.

## Testing

Run the test suite using the following command:

python -m unittest discover tests

## Deployment

### Docker Deployment

1. Build the Docker image:

   docker build -t nen-ai .

2. Run the container:

   docker run -p 5000:5000 -e DATABASE_URL=your_database_url -e SECRET_KEY=your_secret_key nen-ai

### Cloud Deployment (e.g., Heroku)

1. Install the Heroku CLI and log in.

2. Create a new Heroku app:

   heroku create your-app-name

3. Set the necessary environment variables:

   heroku config:set SECRET_KEY=your_secret_key
   heroku config:set DATABASE_URL=your_database_url

4. Deploy the application:

   git push heroku main

5. Open the deployed application:

   heroku open

## Project Structure

NEN-AI/
├── .vscode/
├── api/                 # Flask API code
├── ai_engine/           # AI model and inference code
├── data/                # Raw and processed data
├── config/              # Configuration files
├── tests/               # Unit tests
├── scripts/             # Utility scripts
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── .gitignore
├── .env
├── README.md
├── requirements.txt
└── Dockerfile

## Contributing

We welcome contributions to the NEN-AI project. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/elijahnzeli1`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/elijahnzeli1`)
6. Create a new Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please open an issue on GitHub or contact the maintainer at <ilianacruse@gmail.com>.

Happy generating with NEN-AI!

This README.md file provides a comprehensive guide for users and potential contributors. It covers:

1. An introduction to the project and its features
2. Prerequisites for running the project
3. Detailed installation instructions
4. Configuration steps
5. How to run the application locally
6. Testing procedures
7. Deployment instructions for both Docker and cloud platforms like Heroku
8. An overview of the project structure
9. Guidelines for contributing to the project
10. License information
11. Contact details for further inquiries.

## This README should give users and developers all the information they need to get started with the NEN-AI project, run it locally, and potentially deploy it to a production environment

## NOTE

1. These changes will add a "Speak" button that appears after text is  generated. When clicked, it will send a request to the server to convert the generated text to speech. The resulting audio will be played using an HTML audio element.
2. Remember to handle potential errors, such as when the text is too long for the TTS service or when the user's browser doesn't support the audio format.
3. Also, be aware that generating audio files on the server for each request might not be the most scalable solution for a production environment. For a more scalable approach, you might want to consider using client-side TTS APIs (like the Web Speech API) or a cloud-based TTS service.
