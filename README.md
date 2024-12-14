# AI Interview Assistant

The AI Interview Assistant is an interactive application that uses speech recognition and AI responses to facilitate dynamic, real-time interview interactions. Built with Streamlit, this tool leverages the Google Speech Recognition API and an AI model hosted on Ollama to provide professional and concise answers to user queries.

## Features

- **Speech-to-Text Conversion**: Transcribes spoken questions into text using Google Speech Recognition.
- **AI-Powered Responses**: Generates clear, professional answers using the Ollama API.
- **Interactive UI**: Provides a user-friendly interface for continuous interaction.
- **Session History**: Maintains conversation history for context-aware responses.

## Prerequisites

- Python 3.8 or higher
- Internet connection for API requests

### Required Libraries

Install the necessary dependencies using:

```bash
pip install streamlit speechrecognition requests
```

## Getting Started

1. Clone this repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Ensure the Ollama API is running locally on `http://localhost:11434/api/chat` or update the URL in the script.

3. Run the application:

    ```bash
    streamlit run speech_to_text_ollama.py
    ```

4. Use a microphone to ask questions, and the assistant will provide AI-generated responses.

## Usage

### Key Functions

- **`recognize_speech()`**: Handles speech input and converts it into text with enhanced noise adjustment and error handling.
- **`get_ollama_response(user_message)`**: Sends user input to the Ollama API and retrieves AI responses.
- **`run()`**: Integrates the Streamlit UI, continuously listens for questions, and provides answers.

## Customization

- **Ollama Model**: Modify the model used in the `get_ollama_response()` function by changing the `"model"` parameter in the payload.
- **Speech Recognition Settings**: Adjust the `timeout` and `phrase_time_limit` in `recognize_speech()` to suit different environments.

## Troubleshooting

- **No Speech Detected**: Ensure the microphone is properly connected and functional.
- **API Errors**: Verify the Ollama API is running and accessible at the specified URL.
- **Dependencies Missing**: Reinstall libraries using the `pip install` command above.

## Future Improvements

- Multi-language support for speech recognition and responses.
- Deployment options for cloud platforms.
- Enhanced error handling and debugging features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the user interface.
- [Google Speech Recognition API](https://cloud.google.com/speech-to-text/) for speech-to-text functionality.
- [Ollama](https://ollama.ai/) for providing the AI response backend.

---

Enjoy using the Ollama AI Interview Assistant!
