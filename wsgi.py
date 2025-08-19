import os
import sys

# Ensure the project directory is on the path
PROJECT_DIR = os.path.dirname(__file__)
if PROJECT_DIR not in sys.path:
	sys.path.append(PROJECT_DIR)

from app import app as application  # noqa: E402 