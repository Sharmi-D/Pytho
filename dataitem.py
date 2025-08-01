# Step 1: Initial player list
players = ["Jaddu", "varun", "Sai"]

# matches played and runs of players
stats = [
    (1010, 820),
    (1150, 850),
    (320, 470)
]

# finding players strength
print("Total players: " , len(players))

# Extend Team with a few more player names
new_players = ["Venky", "ruthu", "Aswin"]
players.extend(new_players)  # Add new players to the main list
print("\n Extended player list:", players)

# Add stats for new players
stats.extend([(150, 130), (220, 190), (168, 445)])

# Create dictionary from lists
team = {}
for i in range(len(players)):
    team[players[i]] = stats[i]
print("Current Player's: ", team.items())

# ACCESSING & IF 
# Check if a player is in the team
check_name = "Sai"
if check_name in team:
    print(f"\n {check_name} is in the team with {team[check_name][1]} runs.")
else:
    print(f"\n {check_name} is not found in the team")

# APPEND - adding new player
new_player = "Nattu"
new_stats = (190, 230)
players.append(new_player)
stats.append(new_stats)
team[new_player] = new_stats  # Add to dictionary
print(f"\n Added new player: {new_player}")
print(team.items())
print(len(team))

# Using copy() to keep a backup
backup_players = team.copy()
print("\n Backup of original players list:", backup_players)

# Remove underperforming players and copy to new list
to_removed = []
for names, (matches, runs) in team.items():
    if matches > 120 and runs < 300:
        to_removed.append(names)

for name in to_removed:
    team.pop(name)
print("\n Removed players: ", to_removed) 

# change
 # Update Sai's runs 
if "Sai" in team:
    old = team["Sai"]
    updated = (old[0], old[1] + 5)  # add 20 more runs
    team["Sai"] = updated
    print(f" Updated Sai's goals:  {old[1]} -> {updated[1]}")

# --- Final Output ---
print("\n🏆 Final Team Stats:")
for name, (matches, goals) in team.items():
    print(f"{name}: Matches = {matches}, Goals = {goals}")
