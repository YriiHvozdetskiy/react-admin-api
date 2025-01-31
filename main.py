from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from authx import AuthX, AuthXConfig, RequestToken
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", 'https://react-admin-hazel-gamma.vercel.app'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = AuthXConfig(
    JWT_ALGORITHM = "HS256",
    JWT_SECRET_KEY = "SECRET_KEY",
    JWT_TOKEN_LOCATION = ["headers"],
)

auth = AuthX(config=config)
auth.handle_errors(app)


class LoginRequest(BaseModel):
    username: str
    password: str

@app.post('/login')
def login(request: LoginRequest):
    if request.username == "user" and request.password == "user":
        token = auth.create_access_token(uid=request.username)
        return {"token": token}
    raise HTTPException(401, detail={"message": "Invalid credentials"})
