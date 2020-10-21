"""create users table

Revision ID: 62b6a23c9ba9
Revises: 
Create Date: 2020-09-24 12:27:59.471094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62b6a23c9ba9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('user_type', sa.String))


def downgrade():
    pass
