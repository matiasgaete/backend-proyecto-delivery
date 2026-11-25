from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from userSession import UserSession
from bd import config


def create_update_sesion(user_id: int, device_id: str, refresh_token: str, expires_at):
    with config() as session:
        stmt = insert(UserSession).values(
            user_id=user_id,
            device_id=device_id,
            refresh_token=refresh_token,
            expires_at=expires_at
        ).on_conflict_do_update(
            index_elements=["user_id", "device_id"],
            set_={
                "refresh_token": refresh_token,
                "expires_at": expires_at
            }
        )

        session.execute(stmt)
        session.commit()
    return


def get_sesion_dispositivo_token(device_id: str, refresh_token: str):
    with config() as session:
        stmt = select(UserSession).where(
            UserSession.device_id == device_id,
            UserSession.refresh_token == refresh_token
        )
        return session.scalars(stmt).first()


# 5. Eliminar sesión en el LOGOUT
def eliminar_sesion_repo(user_id: int, device_id: str):
    with config() as session:
        stmt = select(UserSession).where(
            UserSession.user_id == user_id,
            UserSession.device_id == device_id
        )
        sesion = session.scalars(stmt).first()

        if sesion:
            session.delete(sesion)
            session.commit()
    return