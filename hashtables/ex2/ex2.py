#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    next_trip = hash_table_retrieve(hashtable, "NONE")

    while True:
        if next_trip != "NONE":
            route.append(next_trip)
            break
        route.append(next_trip)
        next_trip = hash_table_retrieve(hashtable, next_trip)

    return route
