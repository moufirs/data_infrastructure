from app.quality.structural.structural_validator import (
    StructuralValidator,
)


class ValidationService:

    @staticmethod
    def validate(df):

        return StructuralValidator.validate(df)