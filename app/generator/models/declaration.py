from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class DeclarationDUM:

    declaration_id: UUID

    numero_dum: str

    date_depot: date

    bureau_enregistrement: str

    code_regime: str

    exportateur: str

    importateur: str

    declarant: str

    pays_provenance: str

    pays_origine: str

    pays_destination: str

    conditions_livraison: str

    devise: str

    taux_change: float

    valeur_declaree: float

    code_marchandise: str

    designation_marchandise: str

    poids_net: float

    poids_brut: float

    mode_transport: str