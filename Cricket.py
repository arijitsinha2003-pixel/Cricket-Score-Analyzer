# Cricket Score Analyzer
# Basic Python Project

print("=" * 40)
print("      🏏 CRICKET SCORE ANALYZER")
print("=" * 40)

player = input("Enter player name: ")

matches = int(input("Enter number of matches: "))

runs = []

for i in range(matches):
    score = int(input(f"Enter runs in Match {i + 1}: "))
    runs.append(score)

# Calculations
total_runs = sum(runs)
average = total_runs / matches
best_score = max(runs)

# Strike rate requires balls faced
balls = int(input("\nEnter total balls faced: "))

if balls > 0:
    strike_rate = (total_runs / balls) * 100
else:
    strike_rate = 0

# Performance rating
if average >= 50:
    rating = "Excellent 🔥"
elif average >= 35:
    rating = "Very Good 🟢"
elif average >= 25:
    rating = "Good 🟡"
else:
    rating = "Needs Improvement 🔴"

# Display results
print("\n" + "=" * 40)
print("       PERFORMANCE REPORT")
print("=" * 40)

print(f"Player Name      : {player}")
print(f"Matches Played   : {matches}")
print(f"Total Runs       : {total_runs}")
print(f"Average          : {average:.2f}")
print(f"Best Score       : {best_score}")
print(f"Strike Rate      : {strike_rate:.2f}")
print(f"Performance      : {rating}")

print("=" * 40)