w = [1,2,3,4]
v = [10, 5, 20, 25]

def ks(n, total):
   
  return kanp_sack(len(w), total, )

knap_sack(n, total, mem):
  if mem[n][total]:
    return mem[n][total] 
  if n==0 or total==0:
    result = 0
  elif w[n] > total: 
    result = knap_sack(n-1, total)
  else:
    t1 = knap_sack(n-1, total)
    t2 = knap_sack(n-1, total - w[n])
    result = max(t1, t2)
  mem[n][total] = result
  return result
