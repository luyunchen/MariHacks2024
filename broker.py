class Broker:
    def __init__(self, name, addedOrder, canceledOrder):
        self._name = name
        self._addedOrder = addedOrder
        self._canceledOrder = canceledOrder

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for addedOrder
    def get_addedOrder(self):
        return self._addedOrder

    # Setter method for addedOrder
    def set_addedOrder(self, addedOrder):
        self._addedOrder = addedOrder

    # Getter method for canceledOrder
    def get_canceledOrder(self):
        return self._canceledOrder

    # Setter method for canceledOrder
    def set_canceledOrder(self, canceledOrder):
        self._canceledOrder = canceledOrder