class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    if x<120:
        return x
    else:
       raise StopIteration

num=MyNumbers()
for i in num:
   print(i)
  
  
