def corr(x, y):
      
  def mean(x):
    return sum(x) / len(x)
    
  def stdev(x):
    m = mean(x)
    ss = sum([(i-m)**2 for i in x])
    return (ss/len(x))**0.5
  
  def cov(x, y):
    mean_x, mean_y = mean(x), mean(y)
    n = len(x)
    return (1/n)*sum([(x[i] - mean_x)*(y[i] - mean_y) for i in range(n)])
    
  def sqrt_var(x):
    return (stdev(x))**0.5
  
  res = cov(x,y) / (sqrt_var(x) * sqrt_var(y))
  return round(res,4) 

# Trial 1
x=[1, 3, 5, 7]
y=[2, 4, 6, 8]
print(f"The pearson correlation for x = {x} and y = {y} is {corr(x,y)}")

# Trial 2
x=[-2, 3, 0, 2]
y=[-5, -3, 3, 1]
print(f"The pearson correlation for x = {x} and y = {y} is {corr(x,y)}")