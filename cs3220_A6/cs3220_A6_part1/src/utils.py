from collections import defaultdict, Counter
from CSPclass import CSPBasic 

class UniversalDict:
    """A universal dict maps any key to the same value. 
    We use it here as the domains dict for CSPs 
    in which all variables have the same domain.
    >>> d = UniversalDict(list('RGB'))
    >>> d['SA']
    ['R','G','B']
    """

    def __init__(self, value): 
      self.value = value

    def __getitem__(self, key): 
      return self.value

    def __repr__(self): 
      return f'Any from {self.value}'


def different_values_constraint(A, a, B, b):
    """A constraint saying two neighboring variables must differ in value."""
    return a != b



def parse_neighbors(neighbors):
    """Convert a string of the form 'X: Y Z; Y: Z' into a dict mapping
    regions to neighbors. The syntax is a region name followed by a ':'
    followed by zero or more region names, followed by ';', repeated for
    each region name. If you say 'X: Y' you don't need 'Y: X'.
    >>> parse_neighbors('X: Y Z; Y: Z') == {'Y': ['X', 'Z'], 'X': ['Y', 'Z'], 'Z': ['X', 'Y']}
    True
    """
    dic = defaultdict(list)
    specs = [spec.split(':') for spec in neighbors.split(';')]
    for (A, Aneighbors) in specs:
        #print(A)
        A = A.strip()
        for B in Aneighbors.split():
            dic[A].append(B)
            dic[B].append(A)
    return dic


def MapColoringCSP(colors, neighbors):
    """Make a CSP for the problem of coloring a map with different colors
    for any two adjacent regions. Arguments are a list of colors, and a
    dict of {region: [neighbor,...]} entries. This dict may also be
    specified as a string of the form defined by parse_neighbors."""
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return CSPBasic(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)