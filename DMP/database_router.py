from django.conf import settings


class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            res = settings.DATABASES_APPS_MAPPING[app_label]
            return res
        return None

    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            return settings.DATABASES_APPS_MAPPING[app_label]
        return None

    def db_for_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'BusinessLog':
            return db == 'BusinessLog'
        return None
