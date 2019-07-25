"""empty message

Revision ID: 34615c9297c8
Revises: c332d2b45452
Create Date: 2019-07-24 19:35:09.966591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34615c9297c8'
down_revision = 'c332d2b45452'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('createTime', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'createTime')
    # ### end Alembic commands ###