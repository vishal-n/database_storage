### To implement a simple database transaction storage

import time
import logging
import doctest


class TransactionalStorage:

    def __init__(self):
        self.data = {}                  ### The main data storage
        self.transaction_backup = None  ### Holds backup of the data, when a transaction begins


    def set_key(self, key, val):
        """
        Creates a new key or updates an existing key with the given value.
        """
        self.data[key] = val
        print(f"Set key {val} to {val}")


    def get_key(self, key):
        """
        To retrive the value of a key
        """
        if self.data.get(key):
            return self.data[key]
        else:
            print(f"The given key: {key}, does not exist")
            return None
    

    def delete_key(self, key):
        """ 
        Deletes a key if it exists.
        """
        if key in self.data:
            del self.data[key]
            print(f"Key '{key}' deleted.")
        else:
            print(f"Key '{key}' not found.")


    def begin(self):
        """
        Begins a transaction by saving a snapshot of the current state.
        Only one transaction can be active at a time.
        """
        if self.transaction_backup is not None:
            print("\n Transaction already in progress.")
        else:
            self.transaction_backup = self.data.copy()
            print("\n Transaction started !!")


    def commit(self):
        """
        Finalizes the transaction. 
        Once committed, the changes cannot be rolled back.
        """
        if self.transaction_backup is None:
            print("No transaction to commit.")
        else:
            self.transaction_backup = None
            print("Transaction commit successful !!")


    def rollback(self):
        """
        Reverts all changes made since the last 'begin'.
        """
        if self.transaction_backup is None:
            print("No transaction to rollback.")
        else:
            # Revert data to the backup state
            self.data = self.transaction_backup
            self.transaction_backup = None
            print("Transaction rollback successful !!")
        


if __name__ == '__main__':

    store = TransactionalStorage()

    store.set_key("name", "Alice")
    print("name = ", store.get_key("name"))

    # Start a transaction
    store.begin()
    store.set_key("name", "Bob")
    store.set_key("age", 30)
    print("name =", store.get_key("name"))
    print("age =", store.get_key("age"))
    store.rollback()
    print("\n")
    print("After rollback: \n")
    print("name = ", store.get_key("name"))
    print("age =", store.get_key("age"))


    # Begin a new transaction and commit changes
    store.begin()
    store.set_key("name", "Charlie")
    store.delete_key("name")
    store.commit()
    print("\n")
    print("After commit: ")
    print("name =", store.get_key("name"))
