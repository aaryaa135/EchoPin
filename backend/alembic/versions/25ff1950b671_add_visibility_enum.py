"""add visibility enum

Revision ID: 25ff1950b671
Revises: 6c8152c2c4a6
Create Date: 2026-07-23 21:58:21.907640
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers
revision: str = "25ff1950b671"
down_revision: Union[str, Sequence[str], None] = "6c8152c2c4a6"
branch_labels = None
depends_on = None


visibility_enum = postgresql.ENUM(
    "public",
    "private",
    name="visibility",
    create_type=True,
)


def upgrade() -> None:
    bind = op.get_bind()

    # Create PostgreSQL enum type
    visibility_enum.create(bind, checkfirst=True)

    # Convert varchar -> enum
    op.execute(
        """
        ALTER TABLE echoes
        ALTER COLUMN visibility
        TYPE visibility
        USING visibility::visibility;
        """
    )


def downgrade() -> None:
    # Convert enum -> varchar
    op.execute(
        """
        ALTER TABLE echoes
        ALTER COLUMN visibility
        TYPE VARCHAR(20)
        USING visibility::text;
        """
    )

    bind = op.get_bind()

    visibility_enum.drop(bind, checkfirst=True)