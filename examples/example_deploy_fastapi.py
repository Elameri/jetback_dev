from fastapi import FastAPI
from jetback import jetback_deploy_fastapi

# Create your FastAPI app
app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello from FastAPI on JetBack.Dev :D !"}


# Deploy the FastAPI app
jetback_deploy_fastapi(app)



