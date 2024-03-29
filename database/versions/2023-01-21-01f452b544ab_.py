"""empty message

Revision ID: 01f452b544ab
Revises: eb99eaff62b3
Create Date: 2023-01-21 17:13:03.307441

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '01f452b544ab'
down_revision = 'eb99eaff62b3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE logovariant AS ENUM ('SCOUT', 'CAMP', 'FOREST', 'TRIPLE_DANCING', 'PAIR_STANDING', 'TRIPLE_STANDING', 'TRIPLE_SITTING')")
    op.add_column('events', sa.Column('logo_variant', postgresql.ENUM('SCOUT', 'CAMP', 'FOREST', 'TRIPLE_DANCING', 'PAIR_STANDING', 'TRIPLE_STANDING', 'TRIPLE_SITTING', name='logovariant'), nullable=False))
    op.drop_column('events', 'color_variant')
    op.execute('drop type colorvariant')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE colorvariant AS ENUM ('RED', 'ORANGE', 'YELLOW', 'GREEN', 'GRAY')")
    op.add_column('events', sa.Column('color_variant', postgresql.ENUM('RED', 'ORANGE', 'YELLOW', 'GREEN', 'GRAY', name='colorvariant'), autoincrement=False, nullable=False))
    op.drop_column('events', 'logo_variant')
    # ### end Alembic commands ###
