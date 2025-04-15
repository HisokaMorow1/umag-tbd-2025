"""Init db

Revision ID: 81e33c78f099
Revises: 
Create Date: 2025-04-15 15:06:33.165193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81e33c78f099'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grupos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_usuario', sa.String(length=32), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('apodo', sa.String(), nullable=True),
    sa.Column('ultimo_loggin', sa.DateTime(), nullable=True),
    sa.Column('creado_en', sa.DateTime(), nullable=False),
    sa.Column('habilitado', sa.Boolean(), server_default='1', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuarios_nombre_usuario'), 'usuarios', ['nombre_usuario'], unique=True)
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios_grupos',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('grupo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['grupo_id'], ['grupos.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('usuario_id', 'grupo_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios_grupos')
    op.drop_table('emails')
    op.drop_index(op.f('ix_usuarios_nombre_usuario'), table_name='usuarios')
    op.drop_table('usuarios')
    op.drop_table('grupos')
    # ### end Alembic commands ###
