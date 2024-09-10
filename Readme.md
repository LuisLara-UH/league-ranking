# League Ranking System

This project is a league ranking system that reads match results, calculates points, ranks teams, and prints the standings in a formatted manner. It includes both the main logic for processing league data and a suite of tests to verify its correctness.

## Project Structure

- **`main.py`**: Contains the core functionality of the league ranking system.
- **`test.py`**: Includes unit tests for the different components of the project.

## Features

- **Parse Match Results**: Extracts team names and scores from match result strings.
- **Update Scores**: Updates the scores for teams based on match results.
- **Rank Teams**: Sorts teams by their scores and then alphabetically.
- **Print Rankings**: Outputs the team rankings in a formatted manner.
- **Integration Test**: Tests the entire process from reading input to generating the final output.

## Usage

### Running the Main Script

You can run the `main.py` script directly from the command line. It accepts input either from a file or from standard input.

#### Example Command Line Usage:

```bash
python main.py
```

To provide input from a file:

```bash
python main.py input.txt
```

### Testing
To run the unit tests, use the following command:

```bash
python -m unittest test.py
```
The tests cover:

- Parsing match results.
- Updating scores based on match results.
- Ranking teams by their points.
- Printing the rankings in the expected format.
- Integration testing with sample input data.

## Functions 
### parse_match(line)
Parses a match result string and returns the teams and their scores.

#### Parameters:

- line (str): A string containing the match result.

#### Returns:

- A tuple of (team1, score1, team2, score2).

### update_scores(teams, team1, score1, team2, score2)
Updates the scores of the teams based on the match result.

#### Parameters:

- teams (defaultdict): A dictionary where keys are team names and values are their points.
- team1 (str): The name of the first team.
- score1 (int): The score of the first team.
- team2 (str): The name of the second team.
- score2 (int): The score of the second team.

### rank_teams(teams)
Returns the teams sorted by their points in descending order and then alphabetically.

#### Parameters:

- teams (dict): A dictionary where keys are team names and values are their points.

#### Returns:

- A list of tuples containing (team, points), sorted accordingly.

### print_rankings(rankings)
Prints the team rankings in a formatted manner.

#### Parameters:

- rankings (list): A list of tuples containing (team, points) sorted by rank.

### main(input_scores=None)
Processes the input scores, updates team scores, ranks the teams, and prints the rankings.

#### Parameters:

- input_scores (list of str, optional): A list of match result strings. If not provided, the function reads from standard input.

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests. For major changes or new features, please open an issue to discuss.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
