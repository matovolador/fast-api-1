"""products created rename

Revision ID: 60652c143441
Revises: 89fb89880fdd
Create Date: 2022-11-22 00:18:51.325827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60652c143441'
down_revision = '89fb89880fdd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('products','created',new_column_name='created_at')


def downgrade() -> None:
    op.alter_column('products','created_at',new_column_name='created')
