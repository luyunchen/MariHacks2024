class Broker:
    def __init__(self, name, addedOrder, executedOrder, ratio, highestAsk, lowestBid, spread, overallScore):
        self._name = name
        self._addedOrder = addedOrder
        self._executedOrder = executedOrder
        self._ratio = ratio
        self._highestAsk = highestAsk
        self._lowestBid = lowestBid
        self._spread = spread
        self._overeallScore = overallScore

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
        
    def get_highestAsk(self):
        return self._highestAsk
    def get_lowestBid(self):
        return self._lowestBid
    def get_spread(self):
        return self._spread
    def get_overallScore(self):
        return self._overeallScore
    
    def set_overallScore(self, overallScore):
        self._overeallScore = overallScore