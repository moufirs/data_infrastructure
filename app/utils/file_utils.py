from datetime import datetime


class FileUtils:

    @staticmethod
    def generate_filename(prefix: str = "part") -> str:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        return f"{prefix}_{timestamp}.parquet"