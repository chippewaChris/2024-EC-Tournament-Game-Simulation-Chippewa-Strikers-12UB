import numpy as np

# Define the current standings
teams_pool_b = {
    "CSSC 12UB": {"wins": 2, "losses": 0, "ties": 0, "points": 18, "goals_for": 9, "goals_against": 4},
    "MCU U11C Murillo": {"wins": 1, "losses": 1, "ties": 0, "points": 6, "goals_for": 8, "goals_against": 8},
    "ECU 12U Boys White": {"wins": 1, "losses": 1, "ties": 0, "points": 6, "goals_for": 5, "goals_against": 5},
    "Hodag U12C Chiamulera": {"wins": 0, "losses": 2, "ties": 0, "points": 0, "goals_for": 2, "goals_against": 6}
}

teams_pool_a = {
    "MCU U11C Screnock": {"wins": 1, "losses": 0, "ties": 1, "points": 7, "goals_for": 4, "goals_against": 1},
    "RLSA Thunder": {"wins": 2, "losses": 0, "ties": 0, "points": 12, "goals_for": 7, "goals_against": 0},
    "Hayward 12U Boys": {"wins": 0, "losses": 2, "ties": 0, "points": 0, "goals_for": 0, "goals_against": 7},
    "MAS U12 Coed": {"wins": 1, "losses": 1, "ties": 0, "points": 3, "goals_for": 3, "goals_against": 5}
}

# Define the number of simulations
num_simulations = 1000000

def simulate_game(team1_name, team2_name, teams):
    """ Simulate a game between team1 and team2 and return the result. """
    team1 = teams[team1_name]
    team2 = teams[team2_name]
    total_points = team1["points"] + team2["points"]
    team1_prob = team1["points"] / total_points
    team2_prob = team2["points"] / total_points
    draw_prob = 0.2  # Probability of a draw

    # Normalize the probabilities
    remaining_prob = 1.0 - draw_prob
    team1_prob *= remaining_prob
    team2_prob *= remaining_prob

    result = np.random.choice(["win", "lose", "draw"], p=[team1_prob, team2_prob, draw_prob])
    if result == "win":
        return team1_name
    elif result == "lose":
        return team2_name
    else:
        return "draw"

def update_standings(teams, team1_name, team2_name, result):
    """ Update the standings based on the game result. """
    team1 = teams[team1_name]
    team2 = teams[team2_name]
    goals_team1 = min(np.random.randint(1, 5), 3)
    goals_team2 = min(np.random.randint(1, 5), 3)

    if result == team1_name:
        team1["wins"] += 1
        team1["points"] += 6 + goals_team1
        team2["losses"] += 1
        team1["goals_for"] += goals_team1
        team2["goals_against"] += goals_team1
        team2["goals_for"] += goals_team2
        team1["goals_against"] += goals_team2
        if goals_team2 == 0:
            team1["points"] += 1  # Shutout bonus point
    elif result == team2_name:
        team2["wins"] += 1
        team2["points"] += 6 + goals_team2
        team1["losses"] += 1
        team2["goals_for"] += goals_team2
        team1["goals_against"] += goals_team2
        team1["goals_for"] += goals_team1
        team2["goals_against"] += goals_team1
        if goals_team1 == 0:
            team2["points"] += 1  # Shutout bonus point
    else:
        team1["ties"] += 1
        team2["ties"] += 1
        team1["points"] += 3 + goals_team1
        team2["points"] += 3 + goals_team2
        team1["goals_for"] += goals_team1
        team2["goals_for"] += goals_team2
        team1["goals_against"] += goals_team2
        team2["goals_against"] += goals_team1

def get_winner(teams):
    """ Return the team with the highest points. """
    return max(teams, key=lambda k: teams[k]["points"])

def simulate_pool(teams):
    """ Simulate the pool and return the winner. """
    for team1 in teams:
        for team2 in teams:
            if team1 != team2:
                result = simulate_game(team1, team2, teams)
                update_standings(teams, team1, team2, result)
    return get_winner(teams)

def main():
    pool_b_wins = 0
    tournament_wins = 0

    for _ in range(num_simulations):
        # Simulate Pool B
        pool_b_teams = {k: v.copy() for k, v in teams_pool_b.items()}
        pool_b_winner = simulate_pool(pool_b_teams)
        if pool_b_winner == "CSSC 12UB":
            pool_b_wins += 1

        # Simulate Pool A
        pool_a_teams = {k: v.copy() for k, v in teams_pool_a.items()}
        pool_a_winner = simulate_pool(pool_a_teams)

        # Simulate the final game
        final_result = simulate_game(pool_b_winner, pool_a_winner, {**pool_b_teams, **pool_a_teams})
        if final_result == "CSSC 12UB":
            tournament_wins += 1

    pool_b_win_probability = pool_b_wins / num_simulations
    tournament_win_probability = tournament_wins / num_simulations

    print(f"Probability of winning Pool B: {pool_b_win_probability:.2f}")
    print(f"Probability of winning the tournament: {tournament_win_probability:.2f}")

if __name__ == "__main__":
    main()