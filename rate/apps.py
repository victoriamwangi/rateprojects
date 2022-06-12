from django.apps import AppConfig


class RateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rate'
    
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import signals
