from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import schemas
import models
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ramosDATA", description="Sistema de Gestão Logística - Ramos Transportes")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/motoristas/", response_model=schemas.MotoristaResponse)
def criar_motorista(motorista: schemas.MotoristaCreate, db: Session = Depends (get_db)):
    return crud.create_motorista(db=db, motorista=motorista)

@app.get("/motoristas/", response_model=List[schemas.MotoristaResponse])
def listar_motoristas(skip: int=0, limit: int=100, db: Session = Depends (get_db)):
    return crud.get_motoristas(db=db, skip=skip,limit=limit)

@app.get("/motoristas/{motorista_id}", response_model=schemas.MotoristaResponse)
def listar_motorista_id(motorista_id: int, db: Session = Depends (get_db)):
    db_motorista = crud.get_motorista_by_id(db=db, motorista_id=motorista_id)

    if db_motorista is None:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return db_motorista

