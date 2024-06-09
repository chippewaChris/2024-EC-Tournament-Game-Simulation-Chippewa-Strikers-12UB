# Soccer Tournament Probability Simulator

## Overview
This program simulates a soccer tournament to estimate the probabilities of a team winning its pool and the overall tournament. It uses empirical probabilities derived from multiple simulations to provide these estimates.

## Purpose
The purpose of this program is to provide an estimate of the likelihood that a specific soccer team (CSSC 12UB) will win its pool (Pool B) and the entire tournament. This is done by simulating the remaining games in the tournament thousands of times.

## How It Works
1. **Simulating Games**:
   - The program simulates the remaining soccer games in the tournament many times (1,000,000 times by default).
   - For each game, it decides whether a team wins, loses, or draws based on their current standings and points.

2. **Updating Standings**:
   - After each simulated game, the program updates the teams' standings. It adds points for wins, ties, goals scored, and shutouts.
   - It keeps track of wins, losses, ties, goals scored, and points for each team.

3. **Determining Pool Winners**:
   - The program identifies which team has the highest points in Pool B after all simulated games.
   - It checks if CSSC 12UB wins Pool B in each simulation.

4. **Simulating the Tournament Final**:
   - After determining the winner of Pool B, the program simulates the final game between the winners of Pool B and Pool A.
   - It checks if CSSC 12UB wins the final game.

5. **Calculating Probabilities**:
   - The program counts how many times CSSC 12UB wins Pool B and how many times it wins the final game out of all the simulations.
   - It calculates the probability of winning Pool B and the probability of winning the entire tournament based on these counts.

## Types of Probabilities
The program uses the following types of probabilities:

1. **Empirical Probability**: 
   - The probability is derived from the outcomes observed in the simulations.
   - Formula: \( P(A) = \frac{\text{Number of times event A occurs}}{\text{Total number of trials}} \)

2. **Conditional Probability**:
   - The program calculates the probability of winning the tournament given that the team has won its pool.
   - Formula: \( P(A|B) = \frac{P(A \cap B)}{P(B)} \), provided \( P(B) \neq 0 \)

3. **Joint Probability**:
   - The probability of two events happening together, such as winning a pool and winning the final.
   - Formula: \( P(A \cap B) = P(A) \times P(B) \), for independent events

## Usage
To run the program, follow these steps:

1. **Install Python**: Make sure you have Python installed on your system.
2. **Clone the Repository**: Clone this repository to your local machine.
3. **Create and Activate a Virtual Environment**:
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate  # On macOS/Linux
   myenv\Scripts\activate  # On Windows
