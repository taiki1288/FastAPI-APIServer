from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLiteに接続(SQLiteでtest.dbファイルを開いている)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemyエンジンの作成。SQLiteでのみ必要。他のデータベースでは必要ない。
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_baseはクラスを返す関数。Baseを継承してDBモデルやクラスを作成する。
Base = declarative_base()

# get_db()関数を使用してDBへのアクセスを行う。
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()