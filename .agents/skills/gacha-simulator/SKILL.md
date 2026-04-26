---
name: gacha-simulator
description: Simulates gacha (loot box) pulls using Monte Carlo methods and reports how many pulls and how much money it takes to hit a target rarity. Use when the user asks about gacha odds, pull simulations, expected cost to get a rare card, or loot box probability analysis.
---

# Gacha Simulator

## When to use
- The user wants to know how many pulls it takes on average to get a target rarity
- The user wants to estimate the cost of pulling in a gacha system
- The user wants to see the probability distribution of pulls needed
- The user asks anything about gacha odds, loot box math, or pull simulations

## When not to use
- The user asks about a specific real game's exact gacha rates (this skill uses user-provided rates, not live game data)
- The user wants financial advice on whether to spend money on a game
- The user asks about general probability theory without a gacha context

## Expected inputs
The user should provide:
- Rarity tiers and their drop rates (must sum to 100%)
- Cost per pull in dollars
- Target rarity to simulate for

If the user does not specify rates, use these defaults:
- N (Normal): 40%
- R (Rare): 30%
- SR (Super Rare): 20%
- SSR (Superior Super Rare): 9%
- UR (Ultra Rare): 1%
- Cost per pull: $6

## Step-by-step instructions

1. Confirm the rarity tiers, drop rates, cost per pull, and target rarity with the user.
2. Run the simulation script:
python .agents/skills/gacha-simulator/scripts/simulate.py 
--rates "N:40,R:30,SR:20,SSR:9,UR:1" 
--cost 6 
--target UR 
--simulations 10000
3. The script outputs a JSON object. Read the JSON and present the results to the user in natural language.

## Output format
Present the results clearly, including:
- Average number of pulls to hit the target rarity
- Average cost in dollars
- Minimum and maximum pulls observed in the simulation
- Median pulls
- A note on what percentage of simulations required more than 2x the average

## Important limitations
- This is a statistical simulation, not a guarantee. Real results vary.
- The script assumes each pull is independent (no pity system or guaranteed pulls).
- Drop rates must sum to 100%. The script will reject invalid inputs.
- This skill does not model multi-step pity systems, banners, or duplicate protection.