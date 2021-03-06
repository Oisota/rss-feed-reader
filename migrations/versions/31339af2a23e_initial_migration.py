"""Initial migration.

Revision ID: 31339af2a23e
Revises: 
Create Date: 2021-04-25 21:54:20.509356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31339af2a23e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hash', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url'),
    sa.UniqueConstraint('url', 'user_id', name='uc_user_url')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('feed_title', sa.String(length=255), nullable=False),
    sa.Column('saved', sa.Boolean(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscription.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url', 'user_id', name='uc_user_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('subscription')
    op.drop_table('user')
    # ### end Alembic commands ###
