from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel

app = FastAPI(title="Harpia SPHY API Core")

class QuantumParams(BaseModel):
    H: float
    S: float
    C: float
    I: float
    T: int

@app.get("/")
def home():
    return {"status": "Harpia SPHY Online", "version": "1.1.2"}

@app.post("/resolver_fopt")
def resolver_fopt(params: QuantumParams):
    # Implementação fiel do seu módulo STDJ
    try:
        f_opt = (params.H * 0.2) + (params.S * 0.4) + (params.C * 0.3) + \
                (params.I * 0.5) + np.exp(-params.T / 12)
        
        return {"f_opt": float(f_opt)}
    except Exception as e:
        return {"error": str(e)}