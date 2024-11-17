"""empty message

Revision ID: 1c87cd1748dd
Revises: c82c1438843c
Create Date: 2024-11-17 01:15:56.082191

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1c87cd1748dd'
down_revision = 'c82c1438843c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('party', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=mysql.DATETIME(),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('join_date',
               existing_type=mysql.DATETIME(),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('party', schema=None) as batch_op:
        batch_op.alter_column('join_date',
               existing_type=sa.String(length=255),
               type_=mysql.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('birthday',
               existing_type=sa.String(length=255),
               type_=mysql.DATETIME(),
               existing_nullable=False)

    # ### end Alembic commands ###