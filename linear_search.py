class linear_search():
    def __init__(self):
        pass
    def input_data(self,array):
        self.array = array
    def search(self,query):
        position = 0
        while position < len(self.array):
            if self.array[position] == query:
                return position
            position = position+1
        return -1