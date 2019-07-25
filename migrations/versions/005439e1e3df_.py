"""empty message

Revision ID: 005439e1e3df
Revises: 
Create Date: 2019-07-24 15:14:56.933691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '005439e1e3df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('telphone', sa.String(length=11), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('createTime', sa.DateTime(), nullable=True),
    sa.Column('authorId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['authorId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    op.drop_table('user')
    # ### end Alembic commands ###