import random
from datetime import date
from uuid import uuid4

from faker import Faker

from app.generator.interfaces.generator_interface import GeneratorInterface
from app.generator.models.declaration import DeclarationDUM

from app.generator.reference.reference_data import (
    COUNTRIES,
    CURRENCIES,
    CUSTOMS_OFFICES,
    CUSTOMS_REGIMES,
    PRODUCTS,
    TRANSPORT_MODES,
    CONDITIONS_LIVRAISON,
    MIN_WEIGHT,
    MAX_WEIGHT,
    MIN_VALUE,
    MAX_VALUE,
    MIN_EXCHANGE_RATE,
    MAX_EXCHANGE_RATE,
) 


class FakerGenerator(GeneratorInterface):

    def __init__(self, locale: str = "fr_FR"):
        self.fake = Faker(locale)

    def generate(self) -> DeclarationDUM:

        product = random.choice(PRODUCTS)

        poids_net = round(
            random.uniform(
                MIN_WEIGHT,
                MAX_WEIGHT,
            ),
            2,
        )

        poids_brut = round(
            poids_net + random.uniform(5, 300),
            2,
        )

        return DeclarationDUM(

            declaration_id=uuid4(),

            numero_dum=self._generate_dum_number(),

            date_depot=self.fake.date_between(
                start_date="-2y",
                end_date="today",
            ),

            bureau_enregistrement=random.choice(CUSTOMS_OFFICES),

            code_regime=random.choice(CUSTOMS_REGIMES),

            importateur=self.fake.company(),

            exportateur=self.fake.company(),

            declarant=self.fake.company(),

            pays_origine=random.choice(COUNTRIES),

            pays_provenance=random.choice(COUNTRIES),

            pays_destination=random.choice(COUNTRIES),

            conditions_livraison=random.choice(CONDITIONS_LIVRAISON),

            devise=random.choice(CURRENCIES),

            taux_change=round(
                random.uniform(
                    MIN_EXCHANGE_RATE,
                    MAX_EXCHANGE_RATE,
                ),
                4,
            ),

            valeur_declaree=round(
                random.uniform(
                    MIN_VALUE,
                    MAX_VALUE,
                ),
                2,
            ),

            code_marchandise=product["code_marchandise"],

            designation_marchandise=product["designation_marchandise"],

            poids_net=poids_net,

            poids_brut=poids_brut,

            mode_transport=random.choice(TRANSPORT_MODES),
        )

    def _generate_dum_number(self):

        year = date.today().year

        number = random.randint(
            1,
            999999,
        )

        return f"DUM-{year}-{number:06d}"