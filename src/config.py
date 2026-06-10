from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Project directories
DATA_DIR = BASE_DIR / "data"
TRANSCRIPTS_DIR = BASE_DIR / "transcripts"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"


def create_directories() -> None:
    """
    Create all required project directories if they do not already exist.
    """
    for directory in (DATA_DIR, TRANSCRIPTS_DIR, VECTORSTORE_DIR):
        directory.mkdir(parents=True, exist_ok=True)

# Create project directories when the module is imported
create_directories()