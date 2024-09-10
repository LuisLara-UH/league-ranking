import sys
from collections import defaultdict


def parse_match(line):
    """Parses a match result and returns the teams and their scores."""
    team1, score1, team2, score2 = None, None, None, None
    try:
        parts = line.split(", ")
        team1_info, team2_info = parts[0], parts[1]

        team1, score1 = " ".join(team1_info.split()[:-1]), int(team1_info.split()[-1])
        team2, score2 = " ".join(team2_info.split()[:-1]), int(team2_info.split()[-1])
    except Exception as e:
        print(f"Error parsing line: {line}, Error: {e}")
    return team1, score1, team2, score2


def update_scores(teams, team1, score1, team2, score2):
    """Updates the scores based on the match result."""
    # Save teams with score 0 by default
    teams[team1] += 0
    teams[team2] += 0

    if score1 > score2:
        teams[team1] += 3
    elif score1 < score2:
        teams[team2] += 3
    else:
        teams[team1] += 1
        teams[team2] += 1


def rank_teams(teams):
    """Returns the teams sorted by points and then alphabetically."""
    return sorted(teams.items(), key=lambda x: (-x[1], x[0]))


def print_rankings(rankings):
    """Prints the rankings in the requested format."""
    rank = 1
    prev_points = None
    for idx, (team, points) in enumerate(rankings):
        if points != prev_points:
            rank = idx + 1
        prev_points = points
        point_str = "pts" if points != 1 else "pt"
        print(f"{rank}. {team}, {points} {point_str}")


def main(input_scores=None):
    teams = defaultdict(int)

    if input_scores is None:
        # Read from stdin
        input_scores = sys.stdin.read().strip().splitlines()

    for line in input_scores:
        team1, score1, team2, score2 = parse_match(line)
        update_scores(teams, team1, score1, team2, score2)

    rankings = rank_teams(teams)
    print_rankings(rankings)


if __name__ == "__main__":
    # For command line arguments (optional file input)
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            input_lines = f.readlines()
    else:
        # Input directly from stdin
        input_lines = sys.stdin.read().strip().splitlines()

    main(input_lines)
