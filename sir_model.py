
import numpy as np

class SIRModel:
    def __init__(self, population_size, beta, gamma, initial_infected=1):
        self.population_size = population_size
        self.beta = beta  # Infection rate
        self.gamma = gamma  # Recovery rate
        
        # Initialize population
        self.S = population_size - initial_infected
        self.I = initial_infected
        self.R = 0
        
        # History for tracking
        self.S_history = [self.S]
        self.I_history = [self.I]
        self.R_history = [self.R]
    
    def step(self):
        # Calculate transitions
        new_infections = np.random.binomial(self.S, 1 - np.exp(-self.beta * self.I / self.population_size))
        new_recoveries = np.random.binomial(self.I, 1 - np.exp(-self.gamma))
        
        # Update compartments
        self.S -= new_infections
        self.I += new_infections - new_recoveries
        self.R += new_recoveries
        
        # Record history
        self.S_history.append(self.S)
        self.I_history.append(self.I)
        self.R_history.append(self.R)
        
        return self.S, self.I, self.R
    
    def run_simulation(self, days):
        for _ in range(days):
            self.step()
        
        return {
            'S': self.S_history,
            'I': self.I_history,
            'R': self.R_history
        }
    
    def reset(self, initial_infected=1):
        self.S = self.population_size - initial_infected
        self.I = initial_infected
        self.R = 0
        
        self.S_history = [self.S]
        self.I_history = [self.I]
        self.R_history = [self.R]