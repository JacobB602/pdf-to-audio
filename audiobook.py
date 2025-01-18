import PyPDF2
import pyttsx3
import os

def pdf_to_text(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def text_to_audio(text, output_audio_path):
    """Convert text to audio and save it as an audio file."""
    try:
        engine = pyttsx3.init()

        # List available voices
        voices = engine.getProperty('voices')

        # Set the voice to an English voice
        for voice in voices:
            if "english" in voice.name.lower():  # Look for English in the voice name
                engine.setProperty('voice', voice.id)
                break

        engine.setProperty('rate', 150)  # Adjust the speech rate (slower than default)
        engine.save_to_file(text, output_audio_path)
        engine.runAndWait()
        print(f"Audiobook saved to: {os.path.abspath(output_audio_path)}")  # Print absolute path
    except Exception as e:
        print(f"Error converting text to audio: {e}")

def main():
    # Input and output paths
    pdf_path = input("Enter the path to the PDF file: ").strip()
    output_audio_path = input("Enter the name of the output audio file (e.g., output.mp3): ").strip()
    # Extract text from the PDF
    print("Extracting text from PDF...")
    text = pdf_to_text(pdf_path)

    if text:
        # Convert text to audio
        print("Converting text to audio...")
        text_to_audio(text, output_audio_path)
    else:
        print("Failed to extract text from the PDF.")
    
if __name__ == "__main__":
    main()