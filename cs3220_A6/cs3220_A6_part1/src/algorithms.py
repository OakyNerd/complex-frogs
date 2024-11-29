from queue import Queue

def AC3(csp):
  queue = Queue()
  
  print(f"Initial queue:")
  for Xi in csp.variables:
    for Xk in csp.neighbors[Xi]:
      queue.put((Xi, Xk))
      print((Xi, Xk), end=" ")
    print()
   
  csp.support_pruning()
  checks = 0
  while list(queue.queue):
    (Xi, Xj) = queue.get()
    #print(f'Arc {(Xi, Xj)} is cheking')
    revised, checks = revise(csp, Xi, Xj, checks)
    if revised:
      if not csp.curr_domains[Xi]:
        return False, checks  # CSP is inconsistent
      for Xk in csp.neighbors[Xi]:
        if Xk != Xj:
          queue.put((Xk, Xi))
    print(list(queue.queue))

    '''print(f'Arc {(Xj, Xi)} is cheking')
    revised, checks1 = back_revise(csp, Xi, Xj, checks)
    if revised:
      if not csp.curr_domains[Xj]:
        return False, checks  # CSP is inconsistent
      for Xk in csp.neighbors[Xj]:
        if Xk != Xi:
          queue.add((Xk, Xj))'''

      
  return True, checks  # CSP is satisfiable


def revise(csp, Xi, Xj, checks=0):
    """Return true if we remove a value."""
    revised = False
    print(f'Arc {(Xi, Xj)} is checking')
    for x in csp.curr_domains[Xi][:]:
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        # if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
        conflict = True
        #print(csp.curr_domains[Xj])
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y):
                conflict = False
            checks += 1
            if not conflict:
                break
        if conflict:
            csp.prune(Xi, x)
            print(f'The val {x} was deleted from {Xi} domain')
            revised = True
    return revised, checks


def back_revise(csp, Xi, Xj, checks=0):
    """Return true if we remove a value."""
    revised = False
    for x in csp.curr_domains[Xi][:]:
        conflict = False
        for y in csp.curr_domains[Xj]:
            conflict = False
            #print(y)
            if csp.constraints(Xi, x, Xj, y)==False:
              #print(x,y)
              conflict = True
            checks +=1
            '''if not conflict:
                break'''
            if conflict:
              csp.prune(Xj, y)
              print(f'The val {y} was deleted from {Xj} domain')
              #print(y)
              revised = True
    return revised, checks