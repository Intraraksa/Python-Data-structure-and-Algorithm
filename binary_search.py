class binarySearch():
    def __init__(self):
        pass
    def input_data(self,array):
        self.array = array
    def search(self,query):
        lo , hi = 0 , len(self.array)
        while lo <= hi:
            mid = (lo + hi)//2
            if self.array[mid] = query:
                return mid
            elif self.array[mid] > query:
                hi = mid - 1
            elif self.array[mid] < query:
                lo = mid +1
        return -1