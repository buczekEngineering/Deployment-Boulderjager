from django.apps import AppConfig


class JagdConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "jagd"

    def ready(self):
        import jagd.signals
