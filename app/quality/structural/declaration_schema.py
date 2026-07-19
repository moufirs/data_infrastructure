import pandera.pandas as pa

from pandera import Check


declaration_schema = pa.DataFrameSchema({

    "numero_dum": pa.Column(str),

    "date_depot": pa.Column(pa.DateTime),

    "bureau_enregistrement": pa.Column(str),

    "code_regime": pa.Column(str),

    "importateur": pa.Column(str),

    "exportateur": pa.Column(str),

    "declarant": pa.Column(str),

    "pays_origine": pa.Column(str),

    "pays_provenance": pa.Column(str),

    "pays_destination": pa.Column(str),

    "conditions_livraison": pa.Column(str),

    "devise": pa.Column(str),

    "taux_change": pa.Column(
        float,
        Check.gt(0)
    ),

    "valeur_declaree": pa.Column(
        float,
        Check.gt(0)
    ),

    "code_marchandise": pa.Column(str),

    "designation_marchandise": pa.Column(str),

    "poids_net": pa.Column(
        float,
        Check.gt(0)
    ),

    "poids_brut": pa.Column(
        float,
        Check.gt(0)
    ),

    "mode_transport": pa.Column(str)

})