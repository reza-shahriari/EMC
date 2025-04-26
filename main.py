
from simulation import EpidemicSimulation
from data_analysis import EpidemicAnalyzer

def main():
    # Parameters
    population_size = 1000
    beta = 0.3  # Infection rate
    gamma = 0.1  # Recovery rate
    days = 30
    num_simulations = 100
    
    print(f"Running epidemic simulation with parameters:")
    print(f"Population: {population_size}")
    print(f"Beta (infection rate): {beta}")
    print(f"Gamma (recovery rate): {gamma}")
    print(f"Days: {days}")
    print(f"Monte Carlo simulations: {num_simulations}")
    
    # Run simulation
    simulator = EpidemicSimulation(
        population_size=population_size,
        beta=beta,
        gamma=gamma
    )
    
    results = simulator.run_monte_carlo(
        num_simulations=num_simulations,
        days=days
    )
    
    # Analyze results
    analyzer = EpidemicAnalyzer()
    peak_day, peak_value = analyzer.plot_sir_curves(
        results,
        days=days,
        save_path="epidemic_simulation.png"
    )
    
    print(f"\nResults:")
    print(f"Peak infection occurs on day {peak_day}")
    print(f"Peak number of infected individuals: {peak_value:.1f}")
    print(f"Percentage of population infected at peak: {(peak_value/population_size)*100:.1f}%")

if __name__ == "__main__":
    main()