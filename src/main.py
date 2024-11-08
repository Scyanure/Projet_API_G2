from fastapi import FastAPI
from src.database import Base, engine
from src.models.models import Departement, Commune, Client, Commande, Conditionnement, Objet, ObjetCond, Detail, DetailObjet, Enseigne, Poids, Vignette, Role, RoleUtilisateur

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return {"API démarrée"}

@app.get("/toto/")
def quelquechose():
    return {"bonjour": "toto"}