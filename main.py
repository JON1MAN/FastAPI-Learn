from fastapi import FastAPI
from controller.user.UserController import user_router
from dao.model.user import User
from resources.db_configuration import SessionLocal, engine

User.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)