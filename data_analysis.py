import numpy as np
import matplotlib.pyplot as plt

class EpidemicAnalyzer:
    def __init__(self):
        pass
    
    def find_peak_infection(self, infected_data):
        peak_value = max(infected_data)
        peak_day = infected_data.index(peak_value)
        return peak_day, peak_value
    
    def plot_sir_curves(self, results, days=30, show=True, save_path=None):
        days_range = range(days + 1)
        
        plt.figure(figsize=(12, 8))
        plt.plot(days_range, results['S_mean'], 'b-', label='Susceptible')
        plt.plot(days_range, results['I_mean'], 'r-', label='Infected')
        plt.plot(days_range, results['R_mean'], 'g-', label='Recovered')
        
        # Find and mark the peak
        peak_day, peak_value = self.find_peak_infection(results['I_mean'].tolist())
        plt.plot(peak_day, peak_value, 'ro', markersize=10)
        plt.annotate(f'Peak: Day {peak_day}, {peak_value:.1f} infected',
                     xy=(peak_day, peak_value),
                     xytext=(peak_day + 1, peak_value + 50),
                     arrowprops=dict(facecolor='black', shrink=0.05))
        
        plt.title('SIR Model: Epidemic Spread Simulation')
        plt.xlabel('Days')
        plt.ylabel('Population')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        
        if show:
            plt.show()
        
        return peak_day, peak_value