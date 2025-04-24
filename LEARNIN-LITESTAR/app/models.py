from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class TodoItem(Base):
    __tablename__ = "todo_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    done: Mapped[bool]
