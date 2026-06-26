import psycopg2
import psycopg2.extras
import os
from pathlib import Path
from typing import Any
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / '.env')


def get_connection() -> Any:
    return psycopg2.connect(
        os.getenv('DATABASE_URL'),
        cursor_factory=psycopg2.extras.RealDictCursor
    )