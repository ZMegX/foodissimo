import os

# For a production app, you should use a secret key set in the environment
# The recommended way to generate a 64char secret key is to run:
# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', '0b953105dd30cf778a5b66c91955fed00a363af52639f1a63f7d25429e8306ee')

# When deploying, set in the environment to the PostgreSQL URL
FLASK_SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://ucd_foodissimo_user:jWomeOu6qJLajSs27jBrOCUz6h0SRIL7@dpg-d0og09mmcj7s73d586g0-a/ucd_foodissimo')
SQLALCHEMY_TRACK_MODIFICATIONS = False