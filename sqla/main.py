from faker import Faker
from sqlalchemy.sql.functions import user
from src.models import Usuario
from src.db import Session
from src.db_ops import add_email_to_user, crear_grupo, delete_user, disable_user, get_group, get_user_emails, turn_enable_users, get_user, query_users, create_database
fake = Faker(["es_CL","en_US"])
def main(): 
    create_database()
    #add_users()
    #query_users()
    # usuario = get_user(username="arilopez")
    # print(usuario)

    # disable_user(username="arilopez")
    # turn_enable_users(username=["jperez","ckent"],enabled=True)
    # for user in query_users(filter=False):
    #     print(f"{user.nombre_usuario=},{user.habilitado=}")

    #delete_user(username="arilopez")
    # add_email_to_user(username="ckent",email="ckent2@umag.cl")

    # with Session() as session:
    #     usuario = get_user(username="ckent", session=session)
    #     if usuario is not None:
    #         print(usuario.emails)
        
    # grupo_admins = get_group(name="admins")
    # print(grupo_admins)
    
    # with Session() as session:
    #     usuario = get_user(username="ckent", session=session)
    #     if usuario is not None:
    #         print(usuario.emails)

    #         usuario.grupos = [grupo_admins]
    #         session.commit()
    #         print(usuario.grupos)

    with Session() as session:
        for i in range(20):
            usuario = Usuario(nombre_usuario=fake.user_name(),nombre=fake.name())
            session.add(usuario)
        session.commit()
if __name__ == "__main__":
    main()