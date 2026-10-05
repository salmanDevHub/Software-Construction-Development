import matplotlib.pyplot as plt

categories = [
    "Functional",
    "Non-Functional",
    "Flagged / Unclear"
]

counts = [5, 2, 2]


print("=== Activity 1: Requirements Classification ===\n")

print("Functional Requirements: 5")
print("Non-Functional Requirements: 2")
print("Flagged / Unclear Requirements: 2")
print("Total Genuine Requirements: 9")

# Create bar chart
plt.figure(figsize=(8, 5))

bars = plt.bar(categories, counts)

# Add values on top of bars
for bar, count in zip(bars, counts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        count + 0.1,
        str(count),
        ha="center",
        fontsize=12
    )

plt.title("Requirements Classification")
plt.xlabel("Requirement Type")
plt.ylabel("Number of Requirements")

plt.ylim(0, 6)
plt.tight_layout()

# Show graph
plt.show()