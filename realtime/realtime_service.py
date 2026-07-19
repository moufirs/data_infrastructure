import pandas as pd

from app.config.settings import (
    REALTIME_BUFFER_SIZE,
)

from app.quality.structural.validation_service import (
    ValidationService,
)

from app.datalake.bronze.bronze_writer import (
    BronzeWriter,
)


class RealtimeService:

    def __init__(self):

        self.buffer = []


    def process(
        self,
        declaration: dict,
    ):

        self.buffer.append(
            declaration
        )


        if len(self.buffer) < REALTIME_BUFFER_SIZE:

            return


        df = pd.DataFrame(
            self.buffer
        )


        #====================
        # conversions
        #====================

        df["date_depot"] = pd.to_datetime(
            df["date_depot"]
        )


        #====================
        # validation
        #====================

        df = ValidationService.validate(
            df
        )


        #====================
        # bronze
        #====================

        writer = BronzeWriter()

        writer.write(
            df
        )


        print()

        print(
            f"{len(df)} déclarations stockées."
        )

        print()


        #====================
        # vider le buffer
        #====================

        self.buffer.clear()