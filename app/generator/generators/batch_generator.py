from app.generator.generators.dum_generator import DUMGenerator


class BatchGenerator:

    def __init__(self):
        self.generator = DUMGenerator()

    def generate(self, number_of_records: int):

        declarations = []

        for _ in range(number_of_records):
            declarations.append(
                self.generator.generate()
            )

        return declarations