# Epidemic Spread Simulation

This project simulates the spread of an epidemic using the SIR (Susceptible, Infected, Recovered) model with Monte Carlo simulation.

## Overview

The SIR model divides the population into three compartments:
- **S**: Susceptible individuals who can become infected
- **I**: Infected individuals who can spread the disease
- **R**: Recovered individuals who have immunity

The model uses the following parameters:
- β (beta) = 0.3: Infection rate
- γ (gamma) = 0.1: Recovery rate
- Population size: 1000
- Simulation duration: 30 days

## Project Structure

- `sir_model.py`: Core implementation of the SIR model
- `simulation.py`: Runs the Monte Carlo simulation
- `data_analysis.py`: Analyzes results and finds the peak of infection
- `main.py`: Entry point that ties everything together
- `requirements.txt`: Required dependencies

## Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the simulation:
```bash
python main.py
```

## Results

The simulation produces plots showing:
- The number of susceptible, infected, and recovered individuals over time
- The peak of infection and when it occurs
