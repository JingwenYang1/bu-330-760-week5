"""Gacha pull simulator using Monte Carlo sampling."""

import argparse
import json
import random
import sys


def parse_rates(rates_str: str) -> dict:
    """Parse rate string like 'N:40,R:30,SR:20,SSR:9,UR:1' into a dict."""
    tiers = {}
    for pair in rates_str.split(","):
        name, pct = pair.strip().split(":")
        tiers[name.strip()] = float(pct.strip())
    return tiers


def validate_rates(tiers: dict) -> None:
    """Check that rates sum to 100."""
    total = sum(tiers.values())
    if abs(total - 100.0) > 0.01:
        print(json.dumps({"error": f"Rates sum to {total}, not 100."}))
        sys.exit(1)
    for name, pct in tiers.items():
        if pct < 0:
            print(json.dumps({"error": f"Rate for {name} is negative."}))
            sys.exit(1)


def simulate_once(names: list, weights: list, target: str) -> int:
    """Simulate pulls until the target rarity is hit. Return pull count."""
    pulls = 0
    while True:
        pulls += 1
        result = random.choices(names, weights=weights, k=1)[0]
        if result == target:
            return pulls


def run_simulation(tiers: dict, target: str, cost: float, n_sims: int) -> dict:
    """Run n_sims simulations and return statistics."""
    if target not in tiers:
        return {"error": f"Target '{target}' not in tiers. Available: {list(tiers.keys())}"}

    names = list(tiers.keys())
    weights = [tiers[n] for n in names]

    results = [simulate_once(names, weights, target) for _ in range(n_sims)]
    results.sort()

    avg = sum(results) / len(results)
    median = results[len(results) // 2]
    minimum = results[0]
    maximum = results[-1]
    over_2x_avg = sum(1 for r in results if r > 2 * avg) / len(results) * 100

    return {
        "target_rarity": target,
        "drop_rate_percent": tiers[target],
        "cost_per_pull": cost,
        "simulations": n_sims,
        "average_pulls": round(avg, 1),
        "median_pulls": median,
        "min_pulls": minimum,
        "max_pulls": maximum,
        "average_cost": round(avg * cost, 2),
        "median_cost": round(median * cost, 2),
        "percent_over_2x_average": round(over_2x_avg, 1),
    }


def main():
    parser = argparse.ArgumentParser(description="Gacha pull simulator")
    parser.add_argument("--rates", required=True, help="Rarity rates, e.g. 'N:40,R:30,SR:20,SSR:9,UR:1'")
    parser.add_argument("--cost", type=float, required=True, help="Cost per pull in dollars")
    parser.add_argument("--target", required=True, help="Target rarity to simulate for")
    parser.add_argument("--simulations", type=int, default=10000, help="Number of simulations to run")
    args = parser.parse_args()

    tiers = parse_rates(args.rates)
    validate_rates(tiers)

    result = run_simulation(tiers, args.target, args.cost, args.simulations)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()