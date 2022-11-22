"""configurations

Revision ID: 89fb89880fdd
Revises: 10daeff9f983
Create Date: 2022-11-21 22:38:52.402542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89fb89880fdd'
down_revision = '10daeff9f983'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('config_attributes',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('config_name',sa.String,nullable=False),
        sa.Column('config_value',sa.String,nullable=False),
        sa.Column('variant_id',sa.Integer,nullable=False)
    )
    op.create_foreign_key('fk_config_variant_id','config_attributes', 'product_variants',['variant_id'], ['id'],)

def downgrade() -> None:
    op.drop_constraint('fk_config_variant_id','config_attributes', 'foreignkey')
    op.drop_table('config_attributes')
