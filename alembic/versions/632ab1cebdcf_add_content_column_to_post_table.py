"""add content column to post table

Revision ID: 632ab1cebdcf
Revises: 5e1890723631
Create Date: 2023-04-17 20:24:35.579655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '632ab1cebdcf'
down_revision = '5e1890723631'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts',"content")
    pass
