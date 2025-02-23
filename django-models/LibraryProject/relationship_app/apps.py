from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

# connecting signals for assn3
    def ready(self):
        import relationship_app.signals
