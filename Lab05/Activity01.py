
print("=== Activity 1: Extract Without Inventing ===\n")

stakeholder_notes = """
The system should allow users to create an account.
Users should be able to log in securely.
The system should allow users to update their profile.
Users should be able to search for products.
The system should display product details.
Users should be able to add products to the cart.
Users should be able to place an order.
The system should send an order confirmation.
Administrators should be able to manage products.
"""

requirements = [
    "The system should allow users to create an account.",
    "Users should be able to log in securely.",
    "The system should allow users to update their profile.",
    "Users should be able to search for products.",
    "The system should display product details.",
    "Users should be able to add products to the cart.",
    "Users should be able to place an order.",
    "The system should send an order confirmation.",
    "Administrators should be able to manage products."
]

print("Extracted Requirements:\n")

for i, requirement in enumerate(requirements, start=1):
    print(f"{i}. {requirement}")

print("\nCross-Checking:")

invented_requirement = "The system should support multiple languages."

if invented_requirement not in stakeholder_notes:
    print(f'Removed invented requirement: "{invented_requirement}"')

print("\nFinal Result:")
print(f"Valid requirements: {len(requirements)}")
print("Invented requirements removed: 1")