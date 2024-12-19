from fastapi import FastAPI

from routers.hero_routes import router as Hero_router

app = FastAPI()

@app.get("/health")
def health():
    return "ok"


app.include_router(Hero_router)


#hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")