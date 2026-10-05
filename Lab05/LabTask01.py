
# BUILD A REQUIREMENTS REGISTER WITH HARD TRACEABILITY
# ============================================================

REQ_SOURCE_MAP = {

    "REQ-001": {
        "requirement": "The system must allow users to register for an account.",
        "type": "Functional",
        "source": "Users should be able to register for an account."
    },

    "REQ-002": {
        "requirement": "The system must allow users to log in.",
        "type": "Functional",
        "source": "Users should be able to log in to the system."
    },

    "REQ-003": {
        "requirement": "The system should provide fast response.",
        "type": "Non-Functional",
        "source": "It should be fast."
    },

    "REQ-004": {
        "requirement": "The system must send reminders to users.",
        "type": "Functional",
        "source": "The system should send reminders to users."
    }
}


# ============================================================
# UNSOURCED REQUIREMENTS
# ============================================================
# Any requirement for which an exact source sentence cannot
# be identified must NOT be deleted. It is reported separately.

UNSOURCED = [
    {
        "requirement": "Login must complete in under 2 seconds on a "
                       "standard university WiFi connection, 95% of the time.",
        "reason": "This is a rewritten/testable version of the vague "
                  "requirement 'Fast', not an exact stakeholder statement."
    },
    {
        "requirement": "The system must support at least 5,000 concurrent "
                       "active users without degraded response time.",
        "reason": "This is a rewritten/testable version of "
                  "'Should handle many users'; no exact stakeholder "
                  "source quote was provided."
    }
]


# ============================================================
# DISPLAY REQUIREMENTS REGISTER
# ============================================================

print("=" * 100)
print("CSE325 — LAB 05 — TASK 1")
print("REQUIREMENTS REGISTER WITH HARD TRACEABILITY")
print("=" * 100)

print(
    f"{'ID':<12}"
    f"{'TYPE':<18}"
    f"{'REQUIREMENT':<55}"
    f"SOURCE"
)

print("-" * 100)

for req_id, data in REQ_SOURCE_MAP.items():

    print(
        f"{req_id:<12}"
        f"{data['type']:<18}"
        f"{data['requirement']:<55}"
        f"{data['source']}"
    )


# ============================================================
# DISPLAY UNSOURCED REQUIREMENTS
# ============================================================

print("\n")
print("=" * 100)
print("UNSOURCED REQUIREMENTS")
print("=" * 100)

if len(UNSOURCED) == 0:

    print("No unsourced requirements found.")

else:

    for number, item in enumerate(UNSOURCED, start=1):

        print(f"\nUNSOURCED-{number}")
        print(f"Requirement : {item['requirement']}")
        print(f"Reason      : {item['reason']}")


# ============================================================
# TRACEABILITY VERIFICATION
# ============================================================

print("\n")
print("=" * 100)
print("TRACEABILITY VERIFICATION")
print("=" * 100)

all_traced = True

for req_id, data in REQ_SOURCE_MAP.items():

    if data["source"].strip() == "":
        all_traced = False
        print(f"{req_id}: UNSOURCED")

    else:
        print(f"{req_id}: Source quote available ")

print("\nVerification Result:")

if all_traced:
    print("Every registered requirement has a verbatim source quote.")
else:
    print(" Some registered requirements do not have a source quote.")


print("\n Unsourced findings were preserved separately.")
print("Requirements were not deleted because they lacked traceability.")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 100)
print("FINAL SUMMARY")
print("=" * 100)

print(f"Traceable requirements : {len(REQ_SOURCE_MAP)}")
print(f"Unsourced requirements : {len(UNSOURCED)}")
print(f"Total findings         : {len(REQ_SOURCE_MAP) + len(UNSOURCED)}")

print("\nTask completed successfully.")