
from simulation import EpidemicSimulation
from data_analysis import EpidemicAnalyzer

def main():
    # Parameters
    population_size = input('Enter the population size:(d for 1000)\n')
    if population_size.lower().strip() == 'd':
        population_size = 1000
    else:
        population_size = int(population_size)

    beta = input("Enter beta(Infection rate): d for 0.3\n")
    if beta.lower().strip() == 'd':
        beta = 0.3
    else:
        beta = float(beta)
    while beta >1 or beta<=0:
        print("Invalid input. Please enter a value between 0 and 1.")
        beta = input("Enter beta(Infection rate):\n")
        beta = float(beta)
    
    gamma = input("Enter gamma(Recovery rate): d for 0.1\n")
    if gamma.lower().strip() == 'd':
        gamma = 0.1
    else:
        gamma = float(gamma)
    while gamma >1 or gamma<=0:
        print("Invalid input. Please enter a value between 0 and 1.\n")
        gamma = input("Enter gamma(Recovery rate):\n")
        gamma = float(gamma)
    
    days = input("Enter the number of days to simulate:(d for 30 days)\n")
    if days.lower().strip() == 'd':
        days = 30
    else:
        days = int(days)
    num_simulations = input("Enter the number of Monte Carlo simulations to run:(d for 100)\n")
    if num_simulations.lower().strip() == 'd':
        num_simulations = 100
    else:
        num_simulations = int(num_simulations)

    
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