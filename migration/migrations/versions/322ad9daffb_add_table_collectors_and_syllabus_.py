"""add table collectors and syllabus_collection

Revision ID: 322ad9daffb
Revises: 127e6a09b59
Create Date: 2016-09-16 22:29:54.744351

"""

# revision identifiers, used by Alembic.
revision = '322ad9daffb'
down_revision = '127e6a09b59'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('syllabus_collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collection_id', sa.VARCHAR(length=6), nullable=False),
    sa.Column('syllabus', sa.TEXT(), nullable=False),
    sa.Column('account', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collectors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collection_id', sa.VARCHAR(length=6), nullable=True),
    sa.Column('start_year', sa.SMALLINT(), nullable=False),
    sa.Column('season', sa.SMALLINT(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('collection_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collectors')
    op.drop_table('syllabus_collection')
    ### end Alembic commands ###