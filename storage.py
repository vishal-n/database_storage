### To implement a simple database transaction storage

import time
import logging
import doctest


class KeyValueStore:

    def __init__(self):
        self.store = {}
        self.current_store = {}
        self.is_transaction_in_progress = False
        self.new_keys_added = []
        self.previous_key_values = {}
    

    def set_key(self, new_key, new_val):
        """
        To add a new key or set a new value to an existing key

        >>> set_key("123", "BLR")

        """
        self.current_store = self.store

        if self.store.get(new_key):
            curr_value = self.store[new_key]
            self.store[new_key] = new_val
            self.previous_key_values[new_key] = curr_value
            print(f"*** The value for key {new_key} is replaced, with this new value {new_val} ***")
        else:
            self.store[new_key] = new_val
            self.new_keys_added.append(new_key)
            print(f"*** New key {new_key} is added, whose value is {new_val} ***s")
    

    def get_key(self, input_key):
        """
        To retrive the value of a key
        """
        if self.store.get(input_key):
            return self.store.get(input_key)
        else:
            raise Exception(f"The given key: {input_key}, does not exist")
    

    def begin(self):
        self.is_transaction_in_progress = True
        print("Transaction started !!!")
    

    def commit(self):
        print("Transaction complete !!!")
        self.current_store = self.store
        self.is_transaction_in_progress = False
    

    def delete_key(self, key):
        if key in self.store:
            del self.store[key]


    def rollback(self):

        self.store = self.current_store

        # if self.new_keys_added:
        #     for key in self.new_keys_added:
        #         del self.store[key]
        

        # for key in self.store:
        #     if key in self.previous_key_values:
        #         self.store[key] = self.previous_key_values[keys]
        
        print("Rollback successful !!")
        


if __name__ == '__main__':

    kvs_obj = KeyValueStore()

    # kvs_obj.set_key("123", "XYZ")
    kvs_obj.set_key("567", "MUM")

    kvs_obj.begin()
    kvs_obj.set_key("123", "BLR")
    kvs_obj.set_key("12345", "DEL")
    kvs_obj.delete_key("567")
    kvs_obj.rollback()
    # kvs_obj.commit()

    print("Current store: ", kvs_obj.store)
