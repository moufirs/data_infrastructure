import random
import time

from app.generator.generators.dum_generator import DUMGenerator


class RealtimeGenerator:

    def __init__(self):

        self.generator = DUMGenerator()


    def generate(self):

        return self.generator.generate()


    def start(self):

        print("Realtime Generator Started...")

        while True:

            declaration = self.generate()

            print(declaration)

            time.sleep(
                random.uniform(1, 5)
            )