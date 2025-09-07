from fastapi import FastAPI, Form , Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_recipe(ingredients):
    url = "http://localhost:11434/api/generate"
    prompt = f"""
    You are a cooking assistant. Suggest a simple recipe using these ingredients: {ingredients}.
    Always include:
    - Recipe Name
    - Ingredients List
    - Step-by-step Instructions
    """
    payload = {"model": "recipe-bot", "prompt": prompt, "stream": False}

    try:
        res = requests.post(url, json=payload).json()
        return res.get("response", "No recipe generated.")
    except Exception as e:
        return f"Error: {e}"

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate_recipe(request: Request, ingredients: str = Form(...)):
    recipe = get_recipe(ingredients)
    return templates.TemplateResponse("result.html", {"request": request, "recipe": recipe})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)