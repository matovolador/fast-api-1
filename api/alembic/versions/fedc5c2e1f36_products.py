"""products

Revision ID: fedc5c2e1f36
Revises: 
Create Date: 2022-11-21 22:29:10.218187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fedc5c2e1f36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name',sa.String,nullable=False,unique=True),
        sa.Column('uom',sa.String,nullable=False),
        sa.Column('category_name',sa.String,nullable=False),
        sa.Column('is_producible',sa.Boolean,nullable=False),
        sa.Column('is_purchasable',sa.Boolean,nullable=False),
        sa.Column('type',sa.String,nullable=False,default='product'),
        sa.Column('additional_info',sa.String,nullable=False),
        sa.Column('purchase_uom',sa.String,nullable=True,default=None),
        sa.Column('purchase_uom_conversion_rate',sa.Numeric,nullable=True,default=None),
        sa.Column('batch_tracked',sa.Boolean,nullable=False,default=False),
        sa.Column('updated_at',sa.DateTime(timezone=False),nullable=False, default=sa.func.now()),
        sa.Column('created',sa.DateTime(timezone=False),nullable=False, default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('products')
