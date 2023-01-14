"""empty message

Revision ID: 28b2af9e8819
Revises: c494274d446e
Create Date: 2023-01-14 21:52:12.496121

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '28b2af9e8819'
down_revision = 'c494274d446e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participations',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=False),
    sa.Column('event_id', postgresql.UUID(), nullable=False),
    sa.Column('participation_stage', postgresql.ENUM('PENDING', 'APPROVED', 'DECLINED', name='participationstages'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name=op.f('fk__participations__event_id__events'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk__participations__user_id__users'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__participations')),
    sa.UniqueConstraint('id', name=op.f('uq__participations__id')),
    sa.UniqueConstraint('user_id', 'event_id', name=op.f('uq__participations__user_id_event_id'))
    )
    op.drop_table('booked')
    op.create_unique_constraint(op.f('uq__channels__id'), 'channels', ['id'])
    op.create_unique_constraint(op.f('uq__credentials__id'), 'credentials', ['id'])
    op.create_unique_constraint(op.f('uq__events__id'), 'events', ['id'])
    op.create_unique_constraint(op.f('uq__favourites__id'), 'favourites', ['id'])
    op.create_unique_constraint(op.f('uq__likes__id'), 'likes', ['id'])
    op.create_unique_constraint(op.f('uq__subscribed__id'), 'subscribed', ['id'])
    op.create_unique_constraint(op.f('uq__users__id'), 'users', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq__users__id'), 'users', type_='unique')
    op.drop_constraint(op.f('uq__subscribed__id'), 'subscribed', type_='unique')
    op.drop_constraint(op.f('uq__likes__id'), 'likes', type_='unique')
    op.drop_constraint(op.f('uq__favourites__id'), 'favourites', type_='unique')
    op.drop_constraint(op.f('uq__events__id'), 'events', type_='unique')
    op.drop_constraint(op.f('uq__credentials__id'), 'credentials', type_='unique')
    op.drop_constraint(op.f('uq__channels__id'), 'channels', type_='unique')
    op.create_table('booked',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('user_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('event_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='fk__booked__event_id__events', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk__booked__user_id__users', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pk__booked'),
    sa.UniqueConstraint('user_id', 'event_id', name='uq__booked__user_id_event_id')
    )
    op.drop_table('participations')
    op.execute('drop type participationstages')
    # ### end Alembic commands ###
