import numpy as np
from sir_model import SIRModel

class EpidemicSimulation:
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