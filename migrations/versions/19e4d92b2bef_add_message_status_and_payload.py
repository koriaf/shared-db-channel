"""Add message status and payload

Revision ID: 19e4d92b2bef
Revises: 4bd072d67d85
Create Date: 2020-04-16 12:34:03.014993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19e4d92b2bef'
down_revision = '4bd072d67d85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('payload', sa.JSON(), nullable=True))
    op.add_column('message', sa.Column('status', sa.Enum('received', 'confirmed', 'revoked', 'undeliverable', name='messagestatus', native_enum=False), nullable=True))
    op.drop_column('message', 'predicate')
    op.drop_column('message', 'obj')
    op.drop_column('message', 'subject')
    op.drop_column('message', 'receiver')
    op.drop_column('message', 'sender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('sender', sa.VARCHAR(length=8), autoincrement=False, nullable=True))
    op.add_column('message', sa.Column('receiver', sa.VARCHAR(length=8), autoincrement=False, nullable=True))
    op.add_column('message', sa.Column('subject', sa.VARCHAR(length=1024), autoincrement=False, nullable=True))
    op.add_column('message', sa.Column('obj', sa.VARCHAR(length=1024), autoincrement=False, nullable=True))
    op.add_column('message', sa.Column('predicate', sa.VARCHAR(length=1024), autoincrement=False, nullable=True))
    op.drop_column('message', 'status')
    op.drop_column('message', 'payload')
    # ### end Alembic commands ###
