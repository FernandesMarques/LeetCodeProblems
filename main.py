class solution:
    def __init__(self,numeros):
        self.numeros = numeros

    def sortArrayByParity(self):
        self.numeros.sort(key=lambda x: x % 2)
        return a


a = solution([3, 1, 2, 4])
a.sortArrayByParity()
print(a.numeros)
