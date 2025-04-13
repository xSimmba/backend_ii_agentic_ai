from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL = "sqlite:///./test.db"  # For development (use PostgreSQL in prod)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Removed duplicate import statement

# Added async engine for async operations

engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")
SessionLocal = sessionmaker(engine, class_=AsyncSession)