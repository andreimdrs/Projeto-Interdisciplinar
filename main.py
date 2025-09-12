from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routers import router as api_router
from database import create_db_and_tables


app = FastAPI(
    title="Sistema de Recomendação de Livros e Filmes",
    description="Backend com FastAPI para cadastro, avaliação, recomendação de livros e filmes",
    version="0.1.0"
)


# CORS
origins = ["http://localhost", "http://localhost:3000"] # restringir em produção


app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


# incluir rotas
app.include_router(api_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def root():
    return {"message": "Bem-vindo ao Sistema de Recomendação de Livros e Filmes"}