from django.apps import AppConfig


class DependenciaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Dependencia'
    
    def ready(self):
        from Dependencia.api.seeds.dependencias_seeder import seed_data
        from django.db.models.signals import pre_migrate
        
        def migrate_callback(sender, **kwargs):
            # Verifica que es la primera migración
            if kwargs['using'] == 'default':
                seed_data()

        # Registra la señal
            pre_migrate.connect(migrate_callback, sender=self)