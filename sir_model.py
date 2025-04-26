
import numpy as np

class SIRModel:
    """
    SIR (Susceptible-Infected-Recovered) epidemiological model implementation.
    
    This class implements a stochastic SIR model where:
    - S: Number of susceptible individuals
    - I: Number of infected individuals
    - R: Number of recovered individuals
    
    The model is governed by two key parameters:
    - β (beta): Transmission rate - controls how quickly the disease spreads
    - γ (gamma): Recovery rate - controls how quickly infected individuals recover
    
    The basic reproduction number R₀ = β/γ determines the epidemic potential.
    
    The model uses discrete-time stochastic transitions with:
    - Infection probability: 1 - exp(-β*I/N) for each susceptible individual
    - Recovery probability: 1 - exp(-γ) for each infected individual
    
    This implementation tracks the population counts over time and provides
    methods to run simulations for a specified number of days.
    """

    def __init__(self, population_size, beta, gamma, initial_infected=1):
        self.population_size = population_size
        self.beta = beta  
        self.gamma = gamma  
        self.S = population_size - initial_infected
        self.I = initial_infected
        self.R = 0
        self.S_history = [self.S]
        self.I_history = [self.I]
        self.R_history = [self.R]
    
    def step(self):
        
        new_infections = np.random.binomial(self.S, 1 - np.exp(-self.beta * self.I / self.population_size))
        new_recoveries = np.random.binomial(self.I, 1 - np.exp(-self.gamma))
        
        self.S -= new_infections
        self.I += new_infections - new_recoveries
        self.R += new_recoveries
        
        
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