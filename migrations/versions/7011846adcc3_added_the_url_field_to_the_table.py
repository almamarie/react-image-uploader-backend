"""added the url field to the table

Revision ID: 7011846adcc3
Revises: efbbe71b8bb0
Create Date: 2022-12-09 12:20:49.149050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7011846adcc3'
down_revision = 'efbbe71b8bb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('files_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_url', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('files_data', schema=None) as batch_op:
        batch_op.drop_column('file_url')

    # ### end Alembic commands ###
