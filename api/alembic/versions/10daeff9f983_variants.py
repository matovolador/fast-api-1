"""variants

Revision ID: 10daeff9f983
Revises: fedc5c2e1f36
Create Date: 2022-11-21 22:33:22.478002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10daeff9f983'
down_revision = 'fedc5c2e1f36'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('product_variants',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('sku',sa.String,nullable=False,unique=True),
        sa.Column('sales_price',sa.Numeric,nullable=False),
        sa.Column('type',sa.String,nullable=False,default='product'),
        sa.Column('updated_at',sa.DateTime(timezone=False), nullable=False, default=sa.func.now()),
        sa.Column('created_at',sa.DateTime(timezone=False),nullable=False, default=sa.func.now()),
        sa.Column('product_id',sa.Integer,nullable=False)

    )
    op.create_foreign_key('fk_variant_product_id','product_variants', 'products',['product_id'], ['id'],)
    


def downgrade() -> None:
    op.drop_constraint('fk_variant_product_id','product_variants', 'foreignkey')
    op.drop_table('product_variants')
