# backend/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://PLA:PLA@localhost:28002/planeargas')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
