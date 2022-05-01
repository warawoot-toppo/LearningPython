class Stats:
    def __init__(self,data):
        self.data = data
    def mean(self):
        t = sum(self.data) / len(self.data)
        return t
        
    def min(self):
        r = min(self.data)
        return r
        
    def max(self):
        f = max(self.data)
        return f
        
    def summary(self):
        
        return 'Mean : %s, Min : %s, Max : %s' %(self.mean(),self.min(),self.max())




a = Stats([1,2,3,4,5,6,7,8,9])
print(a.mean())
print(a.min()) 
print(a.max())
print(a.summary())
          