from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def get_root():
  """Get Root response"""
  return {"status": 200, "message": "OK"}