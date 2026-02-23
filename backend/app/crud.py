from sqlalchemy.orm import Session
from . import models
import datetime

def create_issue(db: Session, payload):
    # generate simple tracking id
    dt = datetime.datetime.utcnow().strftime('%Y%m%d')
    count = db.query(models.Issue).count() + 1
    tracking = f"CS-{dt}-{count:04d}"
    db_issue = models.Issue(
        tracking_id=tracking,
        title=payload['title'],
        description=payload.get('description'),
        category=payload.get('category'),
        lat=payload.get('lat'),
        lon=payload.get('lon'),
        image_url=payload.get('image_url')
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue
