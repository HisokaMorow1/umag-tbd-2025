from datetime import datetime
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine,String, not_, select

engine = create_engine("postgresql+psycopg:///test_db_2025")
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_usuario: Mapped[str] = mapped_column(String(32),unique=True,index=True)
    nombre: Mapped[str]
    apodo: Mapped[Optional[str]]
    ultimo_loggin: Mapped[Optional[datetime]]
    creado_en: Mapped[datetime] = mapped_column(default=datetime.now)
    habilitado: Mapped[bool] = mapped_column(default=True,server_default="1")

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, nombre_usuario={self.nombre_usuario},apodo={self.apodo})"
    

def get_user(username: str) -> Usuario | None:
    with Session() as session:
        stmt = select(Usuario).where(Usuario.nombre_usuario == username)
        return session.execute(stmt).scalar_one_or_none()

def main(): 
    Base.metadata.create_all(engine)
    #add_users()
    #query_users()
    usuario = get_user("hola")
    print(usuario)

def query_users():
    with Session() as session:
        stmt =select(Usuario).where(not_( Usuario.apodo.is_(None)))
        result = session.execute(stmt).scalars()
        for row in result:
            print(row)

def add_users():
    u1 = Usuario(nombre_usuario="jperez", nombre="Juan Pérez")
    u2 = Usuario(nombre_usuario="ckent", nombre="Clark Kent", apodo="Superman")
    u3 = Usuario(nombre_usuario="arilopez", nombre="Ariel López")

    with Session() as session:
        session.add_all([u1, u2, u3])

        print(u1.id)
        session.commit()
        print(u1.id)


if __name__ == "__main__":
    main()
