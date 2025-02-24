# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.ford = []  
        self.backward = [homepage]
        
    def visit(self, url: str) -> None:
        self.ford = []  
        self.backward.append(url)
        
    def back(self, steps: int) -> str:
        n = len(self.backward)
        if steps > n - 1:
            steps = n - 1
        while steps:
            self.ford.append(self.backward.pop())
            steps -= 1
        return self.backward[-1]

    def forward(self, steps: int) -> str:  
        n = len(self.ford)
        if steps > n:
            steps = n
        while steps:
            self.backward.append(self.ford.pop())
            steps -= 1
        return self.backward[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



