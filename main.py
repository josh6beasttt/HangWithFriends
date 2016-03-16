import json
from sets import Set
import redis


test_set = Set(['123','321'])

# from twilio.rest import TwilioRestClient
#
# account = "ACd4e53d3c72727960af4662c7287cad81"
# token = "140b4b3e138435fc5f9a3e42813ca04d"
# client = TwilioRestClient(account, token)
#
# message = client.messages.create(to="+13476333706",
#                                  from_="+12014925109",
#                                  body="Mark Zuckerberg wants to hang with you!")

r = redis.StrictRedis(host='localhost', port=6379, db=0)
# person = {'name':'Patrick', 'age':21}
#
# r.set('foo', json.dumps(person))
# obj = json.loads(r.get('foo'))
#
# print obj['name']

r.set(test_set, 1)
print r.get(test_set)
print r.get(Set(['321','123']))