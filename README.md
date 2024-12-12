# Voice-Controlled Assistant using OpenAI's GPT

This project demonstrates the creation of an interactive, voice-controlled assistant that utilizes OpenAI's GPT model to process and respond to user queries in natural language. The assistant allows users to interact through speech, providing a seamless and intuitive user experience. The system captures audio commands, converts them to text using speech recognition, sends the text to OpenAI's GPT API, and responds with a spoken reply.

## Key Features

- **Speech Recognition**: Converts user voice commands into text.
- **OpenAI GPT Integration**: Uses GPT-3.5 to generate responses based on user queries.
- **Text-to-Speech**: Converts the generated text responses back into speech using pyttsx3 for voice output.
- **Voice-Controlled Interaction**: Users can ask questions or give commands, and the assistant responds accordingly.
## Setup

1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3.	Ensure you have an API key from OpenAI. Store your key in the apikey.py file.

#How to Use
	•	Run the script, and the assistant will greet you with “Hello, how are you?”.
	•	Speak to the assistant by giving voice commands such as “Open Google” or asking questions like “What’s the weather?”.
	•	The assistant will respond verbally to your queries and take actions like opening a website in the browser.

#Requirements
	•	Python 3.6 or higher
	•	speech_recognition for converting speech to text
	•	pyttsx3 for text-to-speech functionality
	•	OpenAI API key

