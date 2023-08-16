import os
import sys
from dotenv import load_dotenv

from django.conf import settings
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv()

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "__main__",
    ],
    DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "ecommerce-practice",
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
        }
    },
    MIGRATION_MODULES={"__main__": "migrations"},
    USE_TZ=True,
)
# Initialize Django
import django

django.setup()
# Required to make the models in models.py available to Django ORM
import models

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
