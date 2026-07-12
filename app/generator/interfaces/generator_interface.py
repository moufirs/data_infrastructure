from abc import ABC, abstractmethod

from app.generator.models.declaration import DeclarationDUM


class GeneratorInterface(ABC):

    @abstractmethod
    def generate(self) -> DeclarationDUM:
        pass