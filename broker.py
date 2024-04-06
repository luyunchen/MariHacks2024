class Broker:
    def __init__(self, name, addedOrder, executedOrder, ratio):
        self._name = name
        self._addedOrder = addedOrder
        self._executedOrder = executedOrder
        self._ratio = ratio

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
    def get_executedOrder(self):
        return self._executedOrder

    # Setter method for canceledOrder
    def set_executedOrder(self, executedOrder):
        self._executedOrder = executedOrder
    
    def get_ratio(self):
        return self._ratio
    
    def set_ratio(self, ratio):
        self._ratio = ratio