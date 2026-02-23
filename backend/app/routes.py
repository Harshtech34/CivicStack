from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud, models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/api/v1/issues')
def create_issue(payload: dict, db: Session = Depends(get_db)):
    if not payload.get('title'):
        raise HTTPException(status_code=400, detail='title required')
    issue = crud.create_issue(db, payload)
    return {'tracking_id': issue.tracking_id, 'status': 'created'}

@router.get('/api/v1/issues')
def list_issues(db: Session = Depends(get_db)):
    issues = db.query(models.Issue).order_by(models.Issue.created_at.desc()).all()
    out = []
    for i in issues:
        out.append({
            'id': i.id,
            'tracking_id': i.tracking_id,
            'title': i.title,
            'category': i.category,
            'status': i.status,
            'lat': float(i.lat) if i.lat else None,
            'lon': float(i.lon) if i.lon else None,
            'created_at': i.created_at.isoformat()
        })
    return out
