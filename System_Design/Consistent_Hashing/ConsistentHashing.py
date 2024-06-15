import hashlib
from bisect import bisect, bisect_left
from collections import defaultdict

class ConsistentHashing:

    def __init__(self, num_replicas=3):

    def _hash(self, key):

    def _repl_hash(self, server, replica):


    def add_server(self, server_id):

    def remove_server(self, server_id):

    def get_server(self, key):

    def reassign_keys(self, server_id):


    def add_key(self, key):

    def remove_key(self, key):

    def get_keys(self, server_id):


if :
    ch = ConsistentHashing(num_replicas=3)
ch.add_server('server1')
ch.add_server('server2')
ch.add_server('server3')

print("Server for key1:", ch.add_key('key1'))
print("Server for key2:", ch.add_key('key2'))
print("Server for key3:", ch.add_key('key3'))

ch.remove_server('server2')

print("Reassigned Server for key1:", ch.get_server('key1'))
print("Reassigned Server for key2:", ch.get_server('key2'))
print("Reassigned Server for key3:", ch.get_server('key3'))
