import csv

# Helper function to calculate win-loss percentage from a record string
def calculate_pct(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses) if wins + losses > 0 else 0

# Read the CSV file
teams = []
with open('/Users/chiao/Downloads/pe8_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    eastern_teams = []
    team_scores = {}
    for row in reader:
        team = {
            'Team': row['Team'],
            'Conference': row['Conference'],
            'Home_record': row['HOME'],
            'Away_record': row['AWAY'],
            'PF': float(row['PF']),  # Changed from int to float to prevent errors
            'PA': float(row['PA']),
            'W-L': row['W-L']
        }
        teams.append(team)

        # Part 1: Identify Eastern Conference teams with lower home than away win percentages
        if team['Conference'] == 'Eastern':
            home_pct = calculate_pct(team['Home_record'])
            away_pct = calculate_pct(team['Away_record'])
            if home_pct < away_pct:
                eastern_teams.append(team['Team'])
        
        # Part 2: Calculate PF minus PA
        pf_pa_diff = team['PF'] - team['PA']
        if team['Conference'] not in team_scores:
            team_scores[team['Conference']] = []
        team_scores[team['Conference']].append(pf_pa_diff)

# Output for Part 1
print("Part 1: Eastern teams with lower home win-loss percentage than away:", eastern_teams)

# Output for Part 2
average_diff = {conf: sum(scores) / len(scores) for conf, scores in team_scores.items()}
higher_avg_diff_conf = max(average_diff, key=average_diff.get)
print("\nPart 2: Conference with higher average PF minus PA difference:", higher_avg_diff_conf)

# Part 3: Sort teams by overall win rate (assuming as a proxy for inter-conference win rate)
for team in teams:
    wins, losses = map(int, team['W-L'].split('-'))
    team['Win_rate'] = wins / (wins + losses) if wins + losses > 0 else 0
teams_sorted = sorted(teams, key=lambda x: x['Win_rate'], reverse=True)

print("\nPart 3: Teams ranked by win rate (assuming as proxy for against other conference):")
for rank, team in enumerate(teams_sorted, start=1):
    print(f"{rank}. {team['Team']} - {team['Win_rate']*100:.2f}% win rate")