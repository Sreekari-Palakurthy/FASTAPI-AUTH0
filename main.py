from fastapi import FastAPI
from users import crud
import uvicorn

app = FastAPI()

app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


