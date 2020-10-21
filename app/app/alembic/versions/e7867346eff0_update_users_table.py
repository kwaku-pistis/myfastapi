"""update users table

Revision ID: e7867346eff0
Revises: 62b6a23c9ba9
Create Date: 2020-09-24 13:10:58.530744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7867346eff0'
down_revision = '62b6a23c9ba9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('role', sa.String))
    op.add_column('users', sa.Column('phone_number', sa.String))
    op.add_column('users', sa.Column('payment_info_id', sa.Integer, nullable=True))


def downgrade():
    pass
