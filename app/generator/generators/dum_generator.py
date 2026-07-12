from app.generator.generators.faker_generator import FakerGenerator


class DUMGenerator:

    def __init__(self):
        self.generator = FakerGenerator()

    def generate(self):
        return self.generator.generate()