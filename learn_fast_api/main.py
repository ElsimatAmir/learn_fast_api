from fastapi import FastAPI
from models import user_model
app = FastAPI()


@app.get('/')
async def root():
    user = user_model()
    user.setName('ahmad')
    return {"userName": user}
