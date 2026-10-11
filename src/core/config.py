"""
UrjaCycle AI - Config
Author: Bhomesh Razdan (Lead Architect)
"""

import os

class Settings:
    PROJECT_NAME: str = "UrjaCycle AI"
    VERSION: str = "1.0.0"
    TRACK: str = "Track 03: Waste and Energy"
    LEAD_ARCHITECT: str = "Bhomesh Razdan"
    AWS_REGION: str = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
    DYNAMODB_WASTE_TABLE: str = os.getenv("DYNAMODB_WASTE_TABLE", "UrjaCycle-Waste-Logs")
    DYNAMODB_SOLAR_TABLE: str = os.getenv("DYNAMODB_SOLAR_TABLE", "UrjaCycle-Solar-Audits")

settings = Settings()
