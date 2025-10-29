# Main Entry Point
from input_analyzer import analyze_inputs
from domain_units import process_domain
from core_logic import central_logic
from simulation_engine import run_simulation
from feedback_system import update_models

def main():
    print("🔹 Starting Manofsteel Intelligent Simulator...")
    inputs = analyze_inputs()
    results = []

    for item in inputs:
        domain_output = process_domain(item)
        logic_output = central_logic(domain_output)
        sim_output = run_simulation(logic_output)
        results.append(sim_output)

    with open("simulation_results.json", "w") as f:
        json.dump(results, f, indent=4)

    update_models(results)
    print("✅ Simulation Complete. Results saved to simulation_results.json")

if __name__ == "__main__":
    main()
