"""add user table

Revision ID: e98b6ad385d3
Revises: 632ab1cebdcf
Create Date: 2023-04-18 19:13:20.265807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e98b6ad385d3'
down_revision = '632ab1cebdcf'
branch_labels = None
depends_on = None

# PostgreSQL Implementation
# def upgrade():
#     op.create_table('users',
#                     sa.Column('id', sa.Integer(), nullable=False),
#                     sa.Column('email', sa.String(), nullable=False),
#                     sa.Column('password', sa.String(), nullable=False),
#                     sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
#                     sa.PrimaryKeyConstraint('id'),
#                     sa.UniqueConstraint('email')
#                     )
#     pass

# SQLite Implementation
def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass

def downgrade():
    op.drop_table('users')
    pass
