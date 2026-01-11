from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://neondb_owner:npg_WiOIup25hzwe@ep-royal-bird-a18kewtm-pooler.ap-southeast-1.aws.neon.tech/notes_db?sslmode=require&channel_binding=require"

engine = create_engine(
    DATABASE_URL,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

print("DATABASE URL:", DATABASE_URL)
