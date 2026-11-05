from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/monitors", response_model=schemas.MonitorOut)
def create_monitor(data: schemas.MonitorCreate, db: Session = Depends(get_db)):
    monitor = models.Monitor(**data.model_dump(mode="json"))
    db.add(monitor)
    db.commit()
    db.add(monitor)
    db.commit()
    db.refresh(monitor)
    return monitor

@app.get("/monitors", response_model=list[schemas.MonitorOut])
def read_monitors(db: Session = Depends(get_db)):
    monitors = db.query(models.Monitor).all()
    return monitors

@app.get("/monitors/{monitor_id}", response_model=schemas.MonitorOut)
def read_monitor(monitor_id: int, db: Session = Depends(get_db)):
    monitor = db.query(models.Monitor).filter(models.Monitor.id == monitor_id).first()
    if monitor is None:
        raise HTTPException(status_code=404, detail="Monitor not found")
    return monitor

@app.delete("/monitors/{monitor_id}", status_code=204)
def delete_monitor(monitor_id: int, db: Session = Depends(get_db)):
    monitor = db.query(models.Monitor).filter(models.Monitor.id == monitor_id).first()
    if monitor is None:
        raise HTTPException(status_code=404, detail="Monitor not found")
    db.delete(monitor)
    db.commit()