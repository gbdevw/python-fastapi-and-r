import uuid
from pydantic import BaseSettings

class Settings(BaseSettings):

    ###############################################################################
    #   APPLICATION MISC.                                                         #
    ###############################################################################

    # ENV : APPLICATION_ROOT
    # Prefix for all controllers
    application_root: str = ''
    # ENV : APPLICATION_NAME
    # Name of the application
    application_name: str = 'crypto-watch'
    # ENV : APPLICATION_INSTANCE
    # ID of the instance of the application
    application_instance: str = str(uuid.uuid4())
    # ENV : LOGGING_LEVEL
    logging_level: str = 'INFO'

    ###############################################################################
    #   Coinbase CONFIG.                                                          #
    ###############################################################################

    # ENV : COINBASE_URL
    coinbase_url: str = 'https://api-public.sandbox.pro.coinbase.com'

# Create settings object which loads env. in Settings
settings = Settings()