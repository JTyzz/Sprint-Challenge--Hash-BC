#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    #arr = []

    #for i in range(len(weights)):
    #    hash_table_insert(ht, weights[i], i)
    #david notes
    # dont need to fill out entire index
    # handle duplicate entries for ex1test2

    for i in range(length):

        retrieve_ht = hash_table_retrieve(ht, weights[i])
        if retrieve_ht is not None and retrieve_ht is not i:
            return (i, retrieve_ht)

        else:
            hash_table_insert(ht, limit - weights[i], i)



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
