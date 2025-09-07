# Recipe Generator Chatbot

A web-based chatbot that suggests recipes based on user-input ingredients (e.g., "Egg, Onion"). The chatbot uses a locally hosted AI model (`recipe-bot`, based on `llama3.2`) via Ollama, customized with a dataset of 35 example recipes.

---

## Project Structure

```
recipe-bot/
├── main.py
├── Modelfile
├── templates/
│   ├── form.html
│   ├── result.html
├── requirements.txt
├── README.md
```

---

## Prerequisites

- **Python:** 3.8 or higher
- **Operating System:** Windows or Linux
- **Hardware:** Standard laptop with at least 8GB RAM (for running Ollama)
- **Internet Connection:** Required for initial setup (to download Ollama and llama3.2)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/fayaz2410/recipe-bot
cd recipe-bot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux
source venv/bin/activate
```

### 3. Install Python Dependencies

Install required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```
**Requirements:**
- fastapi
- uvicorn
- requests
- jinja2

### 4. Install and Configure Ollama

Ollama is used to run the recipe-bot model locally.

- **Windows:** Download and install from [Ollama Download](https://ollama.ai/download)
- **Linux:** Run:
  ```bash
  curl https://ollama.ai/install.sh | sh
  ```

#### Pull the Base Model

```bash
ollama pull llama3.2
```

#### Create the recipe-bot Model

The `Modelfile` defines the recipe-bot model, based on llama3.2 and includes a system prompt with 35 example recipes.

```bash
ollama create recipe-bot -f Modelfile
```

#### Run the Ollama Server

```bash
ollama serve
```

#### Run the recipe-bot Model

```bash
ollama run recipe-bot
```

### 5. Run the Application

Ensure Ollama server is running (`ollama serve`) and `recipe-bot` model is active (`ollama run recipe-bot`).

Activate the virtual environment and start the FastAPI server:

```bash
python main.py
```

Open a browser and navigate to [http://localhost:8080](http://localhost:8080).

---

## How to Use

### Web UI

1. Enter ingredients (e.g., "Egg, Onion") in the input field at [http://localhost:8080](http://localhost:8080).
2. View the suggested recipe on the results page.

#### Sample Output

**Recipe Name:** Classic Onion Omelette

**Ingredients:**
- 2 eggs
- 1 medium onion (finely chopped)
- Salt (to taste)
- Black pepper (to taste)
- 1 tbsp butter or oil
- Optional: 1 tbsp chopped parsley

**Step-by-step Instructions:**
1. Crack eggs into a bowl, add salt and pepper, and whisk until smooth.
2. Heat butter or oil in a non-stick skillet over medium heat.
3. Add onions and sauté until golden, about 5 minutes.
4. Pour eggs into the skillet, spreading evenly.
5. Cook for 2-3 minutes until edges set, then flip or fold the omelette.
6. Cook for 1-2 minutes until set. Garnish with parsley (optional) and serve.

**Tips:** Add cheese or herbs for extra flavor. Serve with toast.

---

### API

POST endpoint at `/generate` returns recipe responses.

**Example Request:**
```bash
curl -X POST http://localhost:8080/generate -d "ingredients=Egg, Onion"
```

**Response:**

```
Recipe Name: Classic Onion Omelette

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
```

---

## Notes

- The web UI uses a cooking-themed background image (Unsplash) for a user-friendly experience.
- The `Modelfile` embeds a dataset of 35 recipes to customize `llama3.2` for recipe generation.
- If you encounter port conflicts on 8080, modify `main.py` to use another port (e.g., port=8000).
- Ensure the Ollama server and `recipe-bot` model are running before starting the FastAPI server.
- The project is designed to be fully runnable on a standard Windows/Linux laptop with the documented steps.

---

## Troubleshooting

- **Ollama Server Not Running:** Verify with `ollama serve` and check [http://localhost:11434](http://localhost:11434) (should return a 200 OK response).
- **Model Not Found:** Ensure you have run `ollama pull llama3.2` and `ollama create recipe-bot -f Modelfile`.
- **Port Conflict:** Change the port in `main.py` and restart the server.
- **Template Errors:** Confirm `templates/form.html` and `templates/result.html` are in the `templates/` directory.

---
