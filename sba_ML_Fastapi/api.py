from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import pandas as pd

app = FastAPI()

class Inputs(BaseModel):
    mois: int
    nb_employes: int
    emploi_crees: int
    franchise: int

    montant: float

    creation: str
    emplacement: str
    cred_renouvelable: str
    petit_pret: str
    
    secteur: int

@app.post("/predict")
async def predict(inputs: Inputs):
    model = joblib.load('sba_ML_Fastapi/models/GradientBoostingClassifier.pkl')

    mois = inputs.mois
    nb_employes = inputs.nb_employes
    emploi_crees = inputs.emploi_crees
    franchise = inputs.franchise

    montant = inputs.montant

    secure = 1 if mois >= 240 else 0

    creation = inputs.creation
    creation = 1 if creation == "Oui" else 0

    emplacement = inputs.emplacement
    if emplacement == "Ville":
        emplacement = 1
    elif emplacement == "Campagne":
        emplacement = 2
    else :
        emplacement = 0

    cred_renouvelable = inputs.cred_renouvelable
    cred_renouvelable = 1 if cred_renouvelable == "Oui" else 0
    
    petit_pret = inputs.petit_pret
    petit_pret = 1 if petit_pret == "Oui" else 0

    if nb_employes == 0:
        type_entreprise = 'AUTO'
    elif nb_employes < 10:
        type_entreprise = 'TPE'
    elif nb_employes < 250:
        type_entreprise = 'PME'
    elif nb_employes < 5000:
        type_entreprise = 'ETI'
    else:
        type_entreprise = 'GE'


    secteur = inputs.secteur


    variables = {
        "mois": mois,
        "nb_employes": nb_employes,
        "creation": creation,
        "emploi_crees": emploi_crees,
        "franchise": franchise,
        "emplacement": emplacement,
        "cred_renouvelable": cred_renouvelable,
        "petit_pret": petit_pret,
        "montant": montant,
        "secteur": secteur,
        "secure": secure,
        "type_entreprise": type_entreprise
    }

    df = pd.DataFrame(variables, index=[0])

    prediction = model.predict_proba(df)
    prediction = model.predict_proba(df)[0].tolist()

    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)