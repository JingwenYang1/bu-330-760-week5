# Gacha Simulator Skill

## What it does
This skill simulates gacha (loot box) pulls using Monte Carlo methods. Given a set of rarity tiers with drop rates, a cost per pull, and a target rarity, it runs thousands of simulated pull sessions and reports how many pulls and how much money it takes on average to hit the target.

## Why I chose it
Gacha systems are everywhere in mobile and pc games, but players rarely have a clear picture of how much they will actually spend. A language model cannot reliably run 10,000 random simulations and compute accurate statistics from them, so a Python script is genuinely necessary for this task. The model handles user interaction and result interpretation, while the script handles the math.

## How to use it
Place the `.agents/skills/gacha-simulator/` folder in your project. When you ask a coding assistant about gacha odds, pull costs, or loot box simulations, it will find and activate the skill automatically.

You can also run the script directly:
python .agents/skills/gacha-simulator/scripts/simulate.py 
--rates "N:40,R:30,SR:20,SSR:9,UR:1" 
--cost 6 
--target UR 
--count 1 
--simulations 10000

## What the script does
The script uses weighted random sampling to simulate pulls. For each simulation run, it draws from the rarity pool until the target rarity is hit the required number of times, then records how many pulls it took. After all runs complete, it outputs a JSON object with average pulls, median, min, max, cost estimates, and the percentage of runs that exceeded 2x the average.

## What worked well
The skill was correctly discovered and activated by Claude Code in all three test cases. The agent read the SKILL.md defaults, constructed the right command, and interpreted the JSON output naturally. When asked about a real game (Genshin Impact), the agent ran the simulation but appropriately declined to give spending advice and noted that the skill does not model pity systems.

## Limitations
The script assumes each pull is fully independent. It does not model pity systems, banners, duplicate protection, or guaranteed pulls, which most real gacha games use. The simulation is statistical, not a guarantee, and results vary between runs. For real spending decisions, players should use game-specific calculators.

## Walkthrough Video
https://youtu.be/dTkx94PbDgI
