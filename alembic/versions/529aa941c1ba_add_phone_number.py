"""add phone number

Revision ID: 529aa941c1ba
Revises: 65eeaf2b7781
Create Date: 2023-04-18 20:15:09.144980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '529aa941c1ba'
down_revision = '65eeaf2b7781'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###