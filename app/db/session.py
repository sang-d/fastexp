from app.db.database import SessionLocal


# DependencyO
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
