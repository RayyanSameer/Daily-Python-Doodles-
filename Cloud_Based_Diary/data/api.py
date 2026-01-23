from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import manager 

app = FastAPI()
#Input

class EntryRequest(BaseModel):
    filename :str
    content:str
    password: str

@app.get("/")
def home():
    return {"Status": "Online"}

@app.get("/list")
def list_files():
    return {"files " : manager.list_entries()}

@app.get("/read/{filename}")
def read_entry(filename: str):
    content = manager.read_entry(filename)
    if not content or "Error" in content:
        raise HTTPException(status_code=404, detail="File not found or bad key")
    return {"filename": filename, "content": content}

@app.post("/save")
def save(request: EntryRequest):

    if not manager.verify_password(request.password):
        raise HTTPException(status_code=401, detail="Invalid Password")
    
    success = manager.save_entry(request.filename, request.content)
    if success:
        return {"status": "Saved", "file": request.filename}
    else:
        raise HTTPException(status_code=500, detail="Save Failed")
