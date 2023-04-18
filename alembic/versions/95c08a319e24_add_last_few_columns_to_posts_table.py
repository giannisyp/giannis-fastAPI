"""add last few columns to posts table

Revision ID: 95c08a319e24
Revises: fcc57dd4eeb7
Create Date: 2023-04-18 19:34:00.095877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95c08a319e24'
down_revision = 'fcc57dd4eeb7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),nullable=False,server_default='True'),)
    op.add_column('posts', sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,
                                     server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
