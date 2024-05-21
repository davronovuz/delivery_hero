from fastapi import FastAPI
from auth_routes import auth_router


app=FastAPI()
app.include_router(auth_router)



@app.get("/")
async def root():
    return {"message":"Bosh sahifa"}