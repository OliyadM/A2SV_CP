# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.arr = []  
        self.product = [1]  

    def add(self, num: int) -> None:
        if num == 0:
     
            self.arr = []
            self.product = [1]
        else:
            self.arr.append(num)
            self.product.append(self.product[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.arr):
            return 0  
            
        return self.product[-1] // self.product[-(k + 1)]
