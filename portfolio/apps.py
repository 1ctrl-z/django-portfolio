from django.apps import AppConfig


# This is a configuration class for a Django app named "portfolio" with a default auto field set to
# "BigAutoField".
class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
