import streamlit as st
import speech_recognition as sr
import requests
import json

class OllamaInterviewAssistant:
    def __init__(self, ollama_url="http://localhost:11434/api/chat"):
        """
        Initialize the Ollama Interview Assistant
        
        :param ollama_url: URL for Ollama API chat endpoint
        """
        self.ollama_url = ollama_url
        self.recognizer = sr.Recognizer()
        
        # Initialize session state for conversation history
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []

    def recognize_speech(self):
        """
        Recognize speech with improved robustness and error handling
        
        :return: Transcribed text or None
        """
        try:
            with sr.Microphone() as source:
                st.write("🎤 Listening... Please speak your question.")
                
                # More aggressive noise adjustment
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Increase timeout and phrase time limit
                try:
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=20)
                    
                    try:
                        # Use Google Speech Recognition with multiple language options
                        text = self.recognizer.recognize_google(audio, language='en-US')
                        
                        # Validate transcription length
                        if len(text.strip()) < 2:
                            st.warning("🤔 Very short transcription. Could you speak more clearly?")
                            return None
                        
                        # Check for incomplete sentences and prompt continuation
                        if text[-1] not in '.!?':
                            st.warning("🔍 It seems like the sentence is incomplete. Please continue speaking.")
                            return text + "..."
                        
                        return text
                    
                    except sr.UnknownValueError:
                        st.error("🤷 Could not understand the audio. Please try again.")
                        return None
                    
                    except sr.RequestError as e:
                        st.error(f"🚨 Speech recognition service error: {e}")
                        return None
                
                except sr.WaitTimeoutError:
                    st.warning("⏰ No speech detected. Make sure your microphone is working.")
                    return None
        
        except Exception as e:
            st.error(f"🚨 Speech recognition setup error: {e}")
            return None

    def get_ollama_response(self, user_message):
        """
        Get response from Ollama API
        
        :param user_message: User's input message
        :return: AI-generated response
        """
        try:
            # Prepare the request payload
            payload = {
                "model": "llama3.2",  # You can change this to your preferred model
                "messages": [
                    {"role": "system", "content": "You are an helpful interview assistant. Provide clear, concise, and professional answers."},
                    *st.session_state.conversation_history,
                    {"role": "user", "content": user_message}
                ],
                "stream": False
            }
            
            # Send request to Ollama
            response = requests.post(
                self.ollama_url, 
                data=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )
            
            # Check response
            if response.status_code == 200:
                result = response.json()
                return result['message']['content']
            else:
                st.error(f"🚨 Ollama API Error: {response.text}")
                return "Sorry, I couldn't generate a response."
        
        except Exception as e:
            st.error(f"🚨 Error communicating with Ollama: {e}")
            return "An error occurred while processing your request."

    def run(self):
        """
        Run the Ollama Interview Assistant
        """
        # Streamlit UI
        st.title("🤖 AI Interview Assistant")
        st.write("Ask me anything! I'll listen and respond live for the interview.")

        # Continuous interaction
        while True:
            # Recognize speech
            user_question = self.recognize_speech()
            
            if user_question:
                # Display the recognized question
                st.write(f"📝 Your Question: {user_question}")
                
                # Get AI response
                ai_response = self.get_ollama_response(user_question)
                
                # Update conversation history
                st.session_state.conversation_history.append(
                    {"role": "user", "content": user_question}
                )
                st.session_state.conversation_history.append(
                    {"role": "assistant", "content": ai_response}
                )
                
                # Display AI response
                st.write("🤖 AI Response:")
                st.write(ai_response)
            
            # Small delay and clear to prevent overwhelming
            st.empty()

def main():
    assistant = OllamaInterviewAssistant()
    assistant.run()

if __name__ == "__main__":
    main()
