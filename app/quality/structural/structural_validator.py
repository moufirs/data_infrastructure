import pandas as pd
from app.shared.logger import logger
from app.quality.structural.declaration_schema import (
    declaration_schema,
)


class StructuralValidator:

    @staticmethod
    def validate(df):
        try:

            logger.info("Validation structurelle...")

            return declaration_schema.validate(df)

        except Exception:

            logger.exception("Validation structurelle échouée")

            raise