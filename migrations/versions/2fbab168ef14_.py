"""empty message

Revision ID: 2fbab168ef14
Revises: dd891b0e2f1a
Create Date: 2022-03-02 21:39:03.593154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fbab168ef14'
down_revision = 'dd891b0e2f1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journey', sa.Column('start_date', sa.String(), nullable=True))
    op.add_column('journey', sa.Column('end_date', sa.String(), nullable=True))
    op.add_column('journey', sa.Column('start_time', sa.String(), nullable=False))
    op.add_column('journey', sa.Column('end_time', sa.String(), nullable=True))
    op.drop_column('journey', 'end_datetime')
    op.drop_column('journey', 'start_datetime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journey', sa.Column('start_datetime', sa.VARCHAR(), nullable=False))
    op.add_column('journey', sa.Column('end_datetime', sa.VARCHAR(), nullable=True))
    op.drop_column('journey', 'end_time')
    op.drop_column('journey', 'start_time')
    op.drop_column('journey', 'end_date')
    op.drop_column('journey', 'start_date')
    # ### end Alembic commands ###
