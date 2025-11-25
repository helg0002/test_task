import uvicorn
from fastapi import FastAPI

from api import operator_router, source_router, contact_router
from cfg import config
app = FastAPI()

app.include_router(operator_router)
app.include_router(source_router)
app.include_router(contact_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.api.host, port=config.api.port, reload=True)
