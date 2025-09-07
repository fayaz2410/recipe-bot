Recipe Generator Chatbot
This project is a web-based chatbot that suggests recipes based on user-input ingredients (e.g., "Egg, Onion"). It uses a locally hosted AI model (recipe-bot, based on llama3.2) via Ollama, customized with a recipe dataset embedded in the Modelfile. The backend is built with FastAPI, and the frontend is a web UI styled with Tailwind CSS. The API accepts ingredient inputs and returns responses displayed conversationally in the UI.
Project Structure
recipe-bot/
├── main.py
├── Modelfile
├── templates/
│   ├── form.html
│   ├── result.html
├── requirements.txt
├── README.md

Prerequisites

Python: 3.8 or higher
Operating System: Windows or Linux
Hardware: Standard laptop with at least 8GB RAM (for running Ollama)
Internet Connection: Required for initial setup (to download Ollama and llama3.2)

Setup Instructions
1. Clone the Repository
Clone the repository from GitHub and navigate to the project directory.
git clone https://github.com/fayaz2410/recipe-bot
cd recipe-bot

2. Create and Activate a Virtual Environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux
source venv/bin/activate

3. Install Python Dependencies
Install the required Python packages listed in requirements.txt.
pip install -r requirements.txt

The requirements.txt includes:
fastapi==0.115.0
uvicorn==0.30.6
requests==2.32.3
jinja2==3.1.4

4. Install and Configure Ollama
Ollama is used to run the recipe-bot model locally.

Install Ollama:
Windows: Download and install from https://ollama.ai/download
Linux: Run the following command:curl https://ollama.ai/install.sh | sh




Pull the Base Model:The recipe-bot model is based on llama3.2. Pull it:ollama pull llama3.2


Create the recipe-bot Model:The Modelfile defines the recipe-bot model, which is based on llama3.2 and includes a system prompt with 35 example recipes. Create the model:ollama create recipe-bot -f Modelfile


Run the Ollama Server:In a terminal, start the Ollama server:ollama serve


Run the recipe-bot Model:In another terminal, ensure the model is active:ollama run recipe-bot



5. Run the Application

Ensure the Ollama server is running (ollama serve) and the recipe-bot model is active (ollama run recipe-bot).
In another terminal, activate the virtual environment and start the FastAPI server:python main.py


Open a browser and navigate to http://localhost:8080.

6. Test the API (Optional)
The application includes a POST endpoint at /generate that returns recipe responses. Test it using curl or Postman:
curl -X POST http://localhost:8080/generate -d "ingredients=Egg, Onion"

How to Run the Project

Start the Ollama server in one terminal:ollama serve


Ensure the recipe-bot model is created and running:ollama create recipe-bot -f Modelfile
ollama run recipe-bot


Activate the virtual environment and run the FastAPI server:python main.py


Access the web UI at http://localhost:8080 or use the API endpoint.

Sample Input and Expected Output
Web UI

Input: Enter Egg, Onion in the input field on http://localhost:8080.
Expected Output (displayed on the result page):Recipe Name: Classic Onion Omelette

Ingredients:
- 2 eggs
- 1 medium onion (finely chopped)
- Salt (to taste)
- Black pepper (to taste)
- 1 tbsp butter or oil
- Optional: 1 tbsp chopped parsley

Step-by-step Instructions:
1. Crack eggs into a bowl, add salt and pepper, and whisk until smooth.
2. Heat butter or oil in a non-stick skillet over medium heat.
3. Add onions and sauté until golden, about 5 minutes.
4. Pour eggs into the skillet, spreading evenly.
5. Cook for 2-3 minutes until edges set, then flip or fold the omelette.
6. Cook for 1-2 minutes until set. Garnish with parsley (optional) and serve.

Tips: Add cheese or herbs for extra flavor. Serve with toast.



API

Input (via curl):curl -X POST http://localhost:8080/generate -d "ingredients=Egg, Onion"


Expected Output (response):Recipe Name: Classic Onion Omelette

Ingredients:
- 2 eggs
- 1 medium onion (finely chopped)
- Salt (to taste)
- Black pepper (to taste)
- 1 tbsp butter or oil
- Optional: 1 tbsp chopped parsley

Step-by-step Instructions:
1. Crack eggs into a bowl, add salt and pepper, and whisk until smooth.
2. Heat butter or oil in a non-stick skillet over medium heat.
3. Add onions and sauté until golden, about 5 minutes.
4. Pour eggs into the skillet, spreading evenly.
5. Cook for 2-3 minutes until edges set, then flip or fold the omelette.
6. Cook for 1-2 minutes until set. Garnish with parsley (optional) and serve.

Tips: Add cheese or herbs for extra flavor. Serve with toast.



Notes

The web UI uses a cooking-themed background image (Unsplash) for a user-friendly experience.
The Modelfile embeds a dataset of 35 recipes to customize llama3.2 for recipe generation.
If you encounter port conflicts on 8080, modify main.py to use another port (e.g., port=8000).
Ensure the Ollama server and recipe-bot model are running before starting the FastAPI server.
The project is designed to be fully runnable on a standard Windows/Linux laptop with the documented steps.

Troubleshooting

Ollama Server Not Running: Verify with ollama serve and check http://localhost:11434 in a browser (should return a 200 OK response).
Model Not Found: Ensure ollama pull llama3.2 and ollama create recipe-bot -f Modelfile are executed.
Port Conflict: Change the port in main.py and restart the server.
Template Errors: Confirm templates/form.html and templates/result.html are in the templates/ directory.
