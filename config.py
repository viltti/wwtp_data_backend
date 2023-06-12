import os

def get_config():
    config_dict = {
        'BASIC_AUTH_USERNAME': os.getenv("BASIC_AUTH_USERNAME"),
        'BASIC_AUTH_PASSWORD': os.getenv("BASIC_AUTH_PASSWORD"),
        'BASIC_AUTH_FORCE': True,
        'API_BASE_URL': os.getenv("API_BASE_URL")
    }
    return config_dict