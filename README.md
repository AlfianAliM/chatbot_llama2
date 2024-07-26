# Personal BabyBot v1

## Overview
**Personal BabyBot v1** is an interactive chatbot built using Streamlit, designed to provide quick, accurate, and relevant answers to user queries. By integrating Google Search and leveraging the LLaMA2 AI model via the Replicate API, this bot can fetch up-to-date information and generate natural responses. It supports communication in both English and Indonesian, making it accessible to a wider audience.

## Key Features
- **User-Friendly Interface**: Built with Streamlit to ensure a clean and intuitive user experience.
- **Google Search Integration**: Incorporates Google Search capabilities to retrieve the most relevant and recent information.
- **Language Support**: Currently set to respond in English, with the capability to switch to Indonesian.
- **LLaMA2 AI Model**: Utilizes the advanced LLaMA2 model through the Replicate API for high-quality response generation.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Future Plans](#future-plans)

## Installation

### Prerequisites
- Python 3.7+
- Streamlit
- Replicate API
- Googlesearch-python

### Setup
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/AlfianAliM/chatbot_llama2.git
    cd chatbot_llama2
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Replicate API Token**:
    Obtain your Replicate API token from [Replicate](https://replicate.com/account/api-tokens) and set it in your environment:
    ```bash
    export REPLICATE_API_TOKEN="YOUR_REPLICATE_API_TOKEN"
    ```

## Usage
1. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the Chatbot**:
    - Open your browser and go to `http://localhost:8501`.
    - Ask your questions in the input field and receive real-time answers.

## File Structure
```
.
├── app.py                  # Main application file
├── requirements.txt        # List of dependencies
├── README.md               # This README file
└── ...                     # Additional files and directories
```

## How It Works
1. **User Input**: The user inputs a question into the application interface.
2. **Data Collection**: The bot collects additional data, including extra text from the user and Google search results.
3. **Response Generation**: The LLaMA2 API processes the collected data to formulate responses.
4. **Display Answer**: The bot displays the generated answer within the application interface.

### Google Search Function
Here’s a preview of the new Google Search function:

```python
# Function to perform Google search
def perform_google_search(query):
    results = []
    for j in search(query):  # Perform the search without num argument
        results.append(j)
        if len(results) >= 5:  # Limit results to the first 5
            break
    return results
```

## Contributing
We welcome contributions to improve Personal BabyBot v1. Here’s how you can contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## Future Plans
- **Enhance Response Generation**: Plan to further improve response quality by parsing search results more effectively.
- **Expand Language Support**: Add support for more languages to cater to a global audience.
- **Additional Features**: Integrate more functionalities such as voice input and output, and personalized user experiences.

For a detailed explanation of the project, including step-by-step instructions and technical details, please read the full article here:
https://medium.com/@alfian.ali/develop-personal-babybot-v1-an-interactive-chatbot-including-google-search-to-enhance-daily-c26aa7ce8ee5
