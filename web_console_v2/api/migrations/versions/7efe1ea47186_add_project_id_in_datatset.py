"""add project_id in datatset

Revision ID: 7efe1ea47186
Revises: 8f4d3ac26935
Create Date: 2021-04-20 14:58:41.414958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7efe1ea47186'
down_revision = '8f4d3ac26935'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datasets_v2', sa.Column('project_id', sa.Integer(), nullable=True, comment='project_id'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('datasets_v2', 'project_id')
    # ### end Alembic commands ###