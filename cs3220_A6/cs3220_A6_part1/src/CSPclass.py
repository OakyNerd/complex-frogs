from problemClass import Problem

class CSPBasic(Problem):
      def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem. If variables is empty, it becomes domains.keys()."""
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0

      # These are for constraint propagation

      def support_pruning(self):
        """Make sure we can prune values from domains. 
        (We want to pay for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

      def prune(self, var, value):
        """Rule out var=value."""
        self.curr_domains[var].remove(value)

