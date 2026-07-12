from typing import List

from app.generator.interfaces.generator_interface import GeneratorInterface
from app.generator.models.declaration import DeclarationDUM


class DeclarationService:

    def __init__(self, generator: GeneratorInterface):

        self.generator = generator

    def generate(
        self,
        number_of_records: int,
    ) -> List[DeclarationDUM]:

        declarations = []

        for _ in range(number_of_records):

            declarations.append(
                self.generator.generate()
            )

        return declarations