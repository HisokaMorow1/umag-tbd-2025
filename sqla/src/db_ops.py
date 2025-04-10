
from sqlalchemy import select, update
from src.db import Session, engine


from src.models import Base, Email, Grupo, Usuario


def get_user(username: str, session) -> Usuario | None:

    stmt = select(Usuario).where(Usuario.nombre_usuario == username)

    user = session.execute(stmt).scalar_one_or_none()
    return user

def query_users(filter: bool = False) -> list[Usuario]:
    with Session() as session:
        stmt =select(Usuario).order_by(Usuario.nombre_usuario.desc())
        if filter:
            stmt = stmt.where(Usuario.apodo.is_(None))

        users = session.execute(stmt).scalars().fetchall()
    return users


def add_users():
    u1 = Usuario(nombre_usuario="jperez", nombre="Juan Pérez")
    u2 = Usuario(nombre_usuario="ckent", nombre="Clark Kent", apodo="Superman")
    u3 = Usuario(nombre_usuario="arilopez", nombre="Ariel López")

    with Session() as session:
        session.add_all([u1, u2, u3])
        session.commit()

def disable_user(username: str) -> None:

    with Session() as session:
        with session.begin():
            try:
                user = session.execute(
                    select(Usuario).where(Usuario.nombre_usuario == username)
                    ).scalar_one()
                user.habilitado = False
            except Exception as e:
                print(f"Error:El usuario {username} no existe")
                return
                
            
def turn_enable_users(username: list[str], enabled: bool) -> None:
    with Session() as session:
        with session.begin():
            stmt = (
                update(Usuario).where(Usuario.nombre_usuario
                .in_(username))
                .values(habilitado=enabled))
            session.execute(stmt)
            
def delete_user(username: str) -> None:
    with Session() as session:
        with session.begin():
            user = session.execute(
                    select(Usuario).where(Usuario.nombre_usuario == username)
                    ).scalar_one()
            
            session.delete(user)

def add_email_to_user(username: int, email: str) -> None:
    with Session() as session:
        with session.begin():
            user = session.execute(
                    select(Usuario).where(Usuario.nombre_usuario == username)
                    ).scalar_one()
            user.emails.append(Email(email=email))


def get_user_emails(username: str) -> list[Email]:
    with Session() as session:
            user = session.execute(
                    select(Usuario).where(Usuario.nombre_usuario == username)
                    ).scalar_one()
            stmt = (
                select(Email).where(Email.usuario_id == user.id)
                .order_by(Email.email)
            )
            return session.execute(stmt).scalars().fetchall()

def crear_grupo(name: str) -> Grupo:
    with Session() as session:
        with session.begin():
            grupo = Grupo(nombre=name)
            session.add(grupo)

            return grupo

def get_group(name: str) -> Grupo | None:
    with Session() as session:
        group = session.execute(select(Grupo).where(Grupo.nombre == name)).scalar_one()

        return group



            
def create_database():
    Base.metadata.create_all(engine)

