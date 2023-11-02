from django.apps import AppConfig


class DjangoAdsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_ads_app'

    def ready(self):
        import django_ads_app.signals
