# CSE325 — Software Construction and Development
# Lab 05
# Activity 3: Find the Duplicate
# Activity 4: Rewrite the Vague Ones


# ============================================================
# ACTIVITY 3: FIND THE DUPLICATE
# ============================================================

# Source text containing the deliberately hidden duplicate
source_sentences = [
    "Users should be able to register for an account.",
    "It should be fast.",
    "Users should be able to log in to the system.",
    "The system should send reminders to users.",
    "Login must also be quick."
]


print("=" * 70)
print("ACTIVITY 3: FIND THE DUPLICATE")
print("=" * 70)

print("\nSource Sentences:")
for number, sentence in enumerate(source_sentences, start=1):
    print(f"{number}. {sentence}")


# The 5th sentence restates the 2nd sentence.
sentence_2 = source_sentences[1]
sentence_5 = source_sentences[4]

print("\nDuplicate Analysis:")
print("-" * 70)

print(f"Sentence 2: {sentence_2}")
print(f"Sentence 5: {sentence_5}")

# Compare the meaning rather than exact wording
if "fast" in sentence_2.lower() and "quick" in sentence_5.lower():
    print("\nRESULT: DUPLICATE FOUND")
    print("Sentence 5 is a duplicate of Sentence 2.")
    print("Reason: Both requirements express the same need:")
    print("The login/system should be fast or quick.")
else:
    print("\nNo duplicate found.")


# ============================================================
# ACTIVITY 4: REWRITE THE VAGUE ONES
# ============================================================

print("\n" + "=" * 70)
print("ACTIVITY 4: REWRITE THE VAGUE ONES")
print("=" * 70)


# Original vague requirements
vague_requirements = {
    "Requirement 1": "Fast",
    "Requirement 2": "Should handle many users"
}


# Specific and measurable versions
rewritten_requirements = {
    "Requirement 1":
        "Login must complete in under 2 seconds on a standard "
        "university WiFi connection, 95% of the time.",

    "Requirement 2":
        "The system must support at least 5,000 concurrent active "
        "users without degraded response time."
}


print("\n1. Vague Requirement:")
print(vague_requirements["Requirement 1"])

print("\nRewritten Requirement:")
print(rewritten_requirements["Requirement 1"])

print("\nWhy it is testable:")
print("- Response time is specified: under 2 seconds")
print("- Network condition is specified: university WiFi")
print("- Success rate is specified: 95%")


print("\n" + "-" * 70)

print("\n2. Vague Requirement:")
print(vague_requirements["Requirement 2"])

print("\nRewritten Requirement:")
print(rewritten_requirements["Requirement 2"])

print("\nWhy it is testable:")
print("- User capacity is specified: 5,000 concurrent users")
print("- Performance condition is specified: no degraded response time")


# ============================================================
# FINAL VERIFICATION
# ============================================================

print("\n" + "=" * 70)
print("FINAL VERIFICATION")
print("=" * 70)

print("\nActivity 3:")
print("Duplicate identified:")
print('  "Login must also be quick"')
print('  restates "It should be fast".')

print("\nActivity 4:")
print("'Fast' was converted into a measurable login response-time")
print("  requirement.")

print("'Should handle many users' was converted into a measurable")
print("  concurrent-user capacity requirement.")

print("\nConclusion:")
print("Both vague requirements can now be objectively tested as")
print("pass/fail requirements.")