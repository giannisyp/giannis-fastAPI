"""add foreign-key to posts table

Revision ID: fcc57dd4eeb7
Revises: e98b6ad385d3
Create Date: 2023-04-18 19:27:17.103716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcc57dd4eeb7'
down_revision = 'e98b6ad385d3'
branch_labels = None
depends_on = None

# PostgreSQL implementation
# def upgrade():
#     op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
#     op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
#                           'owner_id'], remote_cols=['id'], ondelete="CASCADE")
#     pass


# def downgrade():
#     op.drop_constraint('post_users_fk', table_name="posts")
#     op.drop_column('posts', 'owner_id')
#     pass

# SQLite implementation

def upgrade():
    with op.batch_alter_table('posts') as batch_op:
        batch_op.add_column(sa.Column('owner_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('post_users_fk', referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    with op.batch_alter_table('posts') as batch_op:
        batch_op.drop_constraint('post_users_fk', type_='foreignkey')
        batch_op.drop_column('owner_id')
    pass