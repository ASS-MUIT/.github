import os
import sys
import time
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini."""
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def wait_for_files_active(files):
  """Waits for the given files to be active."""
  print("Waiting for file processing...")
  for name in (file.name for file in files):
    file = genai.get_file(name)
    while file.state.name == "PROCESSING":
      print(".", end="", flush=True)
      time.sleep(10)
      file = genai.get_file(name)
    if file.state.name != "ACTIVE":
      raise Exception(f"File {file.name} failed to process")
  print("...all files ready")
  print()
# Create the model
generation_config = {
  "temperature": 0.5, # Ajustado para una traducción más literal
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Eres un experto en traducciones técnicas al inglés y otros idiomas.",
)


def translate_file(input_file, output_file):
    """Traduce un archivo usando la API de Gemini."""

    try:
        files = [upload_to_gemini(input_file, mime_type="text/plain")]
        wait_for_files_active(files)


        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        files[0],
                        f"Traduce este fichero a inglés.  El fichero original es un archivo Markdown.", # Instrucción más específica
                    ],
                },
          ]
        )
        response = chat_session.send_message("procede") #mensaje para que la api responda

        with open(output_file, "w") as f:
            f.write(response.text)

        print(f"Traducción guardada en: {output_file}")

    except Exception as e:
        print(f"Error durante la traducción: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python translate.py <fichero_entrada> <fichero_salida>")
        sys.exit(1)  # Salir con código de error

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.exists(input_filename):
        print(f"Error: El fichero '{input_filename}' no existe.")
        sys.exit(1)

    translate_file(input_filename, output_filename)