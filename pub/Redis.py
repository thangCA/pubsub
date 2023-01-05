import json
import redis
from django.core.management import BaseCommand

redis_client = redis.StrictRedis(host='localhost', port=6379, db=1)
def publish_data_on_redis(json_data, channel_name):
    redis_client.publish(channel_name, json.dumps(json_data))



## Response User Infor when sub

class Response_User_Infor(BaseCommand):
    def handle(self, *args, **options):
        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        p = r.pubsub()
        p.psubscribe('user.created')
        for message in p.listen():
            if message and message['data'] != 1:
                data = message['data'].decode('utf-8')
                data = json.loads(data)
                return data

        return None





