from django.conf import settings
from pymongo import MongoClient

class MongodbMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        mongodbs = getattr(settings, 'MONGODB_DATABASES', None)
        db = mongodbs['default']
        uri = 'mongodb://{user}:{password}@{host}:{port}/{name}'.format(
            user=db['USER'],
            password=db['PASSWORD'],
            host=db['HOST'],
            port=db['PORT'],
            name=db['NAME'],
        )
        self.client = MongoClient(uri)
        self.db = self.client[db['NAME']]

    def __call__(self, request):
        request.mongo_client = self.client
        request.mongo_db = self.db
        response = self.get_response(request)
        return response
