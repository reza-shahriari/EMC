import numpy as np
from sir_model import SIRModel

class EpidemicSimulation:
    """
    A wrapper class for running epidemic simulations using the SIR model.
    
    This class provides functionality to:
    1. Run individual SIR model simulations with specified parameters
    2. Perform Monte Carlo simulations to analyze the distribution of outcomes
    
    The simulation uses the stochastic SIR model to account for randomness in disease
    transmission and recovery processes. Monte Carlo methods allow for quantifying
    uncertainty and variability in epidemic trajectories.
    
    Parameters:
    -----------
    population_size : int, default=1000
        Total number of individuals in the population
    beta : float, default=0.3
        Transmission rate parameter (contact rate * transmission probability)
    gamma : float, default=0.1
        Recovery rate parameter (1/infectious period)
    initial_infected : int, default=1
        Number of infected individuals at the start of the simulation
        
    Methods:
    --------
    run_single_simulation(days=30):
        Runs a single epidemic simulation for the specified number of days
    run_monte_carlo(num_simulations=100, days=30):
        Runs multiple simulations and provides statistical summaries
    """
    def __init__(self, population_size=1000, beta=0.3, gamma=0.1, initial_infected=1):
        self.population_size = population_size
        self.beta = beta
        self.gamma = gamma
        self.initial_infected = initial_infected
        self.model = SIRModel(population_size, beta, gamma, initial_infected)
    
    def run_single_simulation(self, days=30):
        self.model.reset(self.initial_infected)
        return self.model.run_simulation(days)
    
    def run_monte_carlo(self, num_simulations=100, days=30):
        all_results = []
        
        for _ in range(num_simulations):
            result = self.run_single_simulation(days)
            all_results.append(result)
        
        # Aggregate results
        S_mean = np.mean([result['S'] for result in all_results], axis=0)
        I_mean = np.mean([result['I'] for result in all_results], axis=0)
        R_mean = np.mean([result['R'] for result in all_results], axis=0)
        
        return {
            'S_mean': S_mean,
            'I_mean': I_mean,
            'R_mean': R_mean,
            'all_results': all_results
        }