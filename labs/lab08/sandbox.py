# Lab 08 Sandbox - Follow along with the lab instructions

# Step 1: The Problem - Data doesn't persist
scores = []
scores.append(85)
scores.append(92)
scores.append(78)

print("Scores:", scores)

# Write scores to a file
# Read scores from the file
f = open("labs/lab08/data/scores.txt", "r")
data = f.read()
print(data)
f.close()
# Try running this program again - scores will be empty!
