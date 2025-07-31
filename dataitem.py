# Step 1: Initial player list
players = ["Messi", "Ronaldo", "Mbappe", "Neymar"]

# Step 2: Player stats (matches played, goals)
stats = [
    (1010, 820),   # Messi
    (1150, 850),   # Ronaldo
    (320, 270),    # Mbappe
    (500, 310)     # Neymar
]

# Step 3: Create dictionary to map players to stats
team = {}
for i in range(len(players)):
    # print('length of players.......')
    team[players[i]] = stats[i]

# --- Method 1: APPEND ---
# Step 4: Add a new player
new_player = "Haaland"
new_stats = (150, 130)
players.append(new_player)
stats.append(new_stats)
team[new_player] = new_stats  # Add to dictionary
print(f"\n📌 Added new player: {new_player}")
print(team.items())

new_player = "sharmila"
new_stats = (230, 890)
players.insert(2, new_player)
players.insert(2, new_stats)
team[new_player] = new_stats
print(f"\n📌 Another new player Added: {new_player}")
print(team.items())



# --- Method 2: ACCESSING & IF ---
# Step 5: Check if a player is in the team
check_name = "Mbpe"
if check_name in team:
    print(f"\n ✅ {check_name} is in the team with {team[check_name][1]} goals.")
else:
    print(f"\n❌ {check_name} is not found in the team")

# --- Method 3: CHANGE / UPDATE ---
# Step 6: Update Neymar's goal count
if "Neymar" in team:
    old = team["Neymar"]
    updated = (old[0], old[1] + 5)  # Scored 5 more goals
    team["Neymar"] = updated
    print(f"🔄 Updated Neymar's goals:  {old[1]} -> {updated[1]}")

# --- Method 4: FOR LOOP + CONDITIONAL ---
# Step 7: Remove underperforming players (<300 goals)
to_remove = []
for name, (matches, goals) in team.items():
    if goals < 300:
        to_remove.append(name)
    print("\n Underperforming players:",to_remove)

for name in to_remove:
    team.pop(name)
    print(f"❌ Removed underperforming player: {name}")

# --- Method 5: ADDING new player manually ---
# Step 8: Add one more player
team["Vinicius"] = (220, 190)
print("➕ Manually added Vinicius to the team.")

# --- Final Output ---
print("\n🏆 Final Team Stats:")
for name, (matches, goals) in team.items():
    print(f"{name}: Matches = {matches}, Goals = {goals}")






    # Step 1: Initial player list
players = ["Messi", "Ronaldo", "Mbappe", "Neymar"]
stats = [
    (1010, 820),
    (1150, 850),
    (320, 270),
    (500, 310)
]

# --- Using copy() to keep a backup ---
backup_players = players.copy()
print("📋 Backup of original players list:", backup_players)

# Step 2: Extend with a few more player names
new_players = ["Haaland", "Vinicius"]
players.extend(new_players)  # Add new players to the main list
print("\n📌 Extended player list:", players)

# Add stats for new players
stats.extend([(150, 130), (220, 190)])

# Step 3: Create dictionary from lists
team = {}
for i in range(len(players)):
    team[players[i]] = stats[i]

# Step 4: Reverse the player list
players.reverse()
print("\n🔁 Reversed player list (for viewing order):", players)

# Step 5: Check and update Neymar's goals
if "Neymar" in team:
    old = team["Neymar"]
    updated = (old[0], old[1] + 5)
    team["Neymar"] = updated
    print(f"\n🔄 Updated Neymar's goals: {old[1]} ➡ {updated[1]}")

# Step 6: Remove underperformers (< 300 goals)
to_remove = []
for name, (matches, goals) in team.items():
    if goals < 300:
        to_remove.append(name)

for name in to_remove:
    team.pop(name)
    print(f"❌ Removed underperforming player: {name}")

# Step 7: Sort players by goals
sorted_team = list(team.items())
sorted_team.sort(key=lambda x: x[1][1], reverse=True)

# Step 8: Display sorted results
print("\n🏆 Final Team Stats (Sorted by Goals):")
for name, (matches, goals) in sorted_team:
    print(f"{name}: Matches = {matches}, Goals = {goals}")

