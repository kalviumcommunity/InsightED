"""
=============================================================================
 Module: Conditional Statements for Data Logic
 Author: InsightED Learning Module
 Description:
     Demonstrates Python conditional constructs — if, if-else, if-elif-else,
     and logical operators — through real-world, meaningful examples such as
     student grading, eligibility checks, and boundary-value handling.
=============================================================================
"""


# ─────────────────────────────────────────────────────────────────────────────
# Section 1: Basic if Example
# ─────────────────────────────────────────────────────────────────────────────
# A basic `if` statement executes a block of code ONLY when its condition
# evaluates to True.  If the condition is False, the block is silently skipped.

def check_passing_status(student_marks: int) -> None:
    """Check whether a student has passed (marks >= 40)."""
    print(f"\n--- Basic if Example ---")
    print(f"Student marks: {student_marks}")

    # The block below runs only when the student scored 40 or above
    if student_marks >= 40:
        print("✅ Result: The student has PASSED the examination.")

    # NOTE: If marks < 40, nothing is printed — there is no else branch here.
    # This is intentional; a basic `if` handles only the truthy path.


# Demonstrate with a passing score
check_passing_status(75)

# Demonstrate with a failing score — observe that no output is generated
check_passing_status(30)


# ─────────────────────────────────────────────────────────────────────────────
# Section 2: if–else Example
# ─────────────────────────────────────────────────────────────────────────────
# `if-else` provides two mutually exclusive paths: one for True, one for False.
# This guarantees that exactly ONE branch always executes.

def evaluate_voting_eligibility(citizen_age: int) -> None:
    """Determine if a citizen is eligible to vote (age >= 18)."""
    print(f"\n--- if–else Example ---")
    print(f"Citizen age: {citizen_age}")

    if citizen_age >= 18:
        print("✅ Eligible: You are old enough to vote.")
    else:
        years_remaining = 18 - citizen_age
        print(f"❌ Not eligible: You need to wait {years_remaining} more year(s).")


# Edge case: exactly at the boundary (age = 18)
evaluate_voting_eligibility(18)

# Standard cases
evaluate_voting_eligibility(25)
evaluate_voting_eligibility(14)


# ─────────────────────────────────────────────────────────────────────────────
# Section 3: if–elif–else Example
# ─────────────────────────────────────────────────────────────────────────────
# `if-elif-else` chains let us evaluate MULTIPLE mutually exclusive conditions
# in sequence.  The first condition that evaluates to True wins; the rest are
# skipped entirely.  The `else` acts as a catch-all fallback.

def assign_letter_grade(student_marks: int) -> str:
    """
    Assign a letter grade based on marks (0–100 scale).

    Grading scheme:
        90–100  →  A+ (Outstanding)
        80–89   →  A  (Excellent)
        70–79   →  B  (Good)
        60–69   →  C  (Above Average)
        50–59   →  D  (Average)
        40–49   →  E  (Below Average — but passing)
         0–39   →  F  (Fail)
    """
    print(f"\n--- if–elif–else Example ---")
    print(f"Student marks: {student_marks}")

    # Guard clause: validate input before processing
    if student_marks < 0 or student_marks > 100:
        print("⚠️  Invalid marks! Marks must be between 0 and 100.")
        return "INVALID"

    # Conditions are checked top-down; the FIRST match executes
    if student_marks >= 90:
        grade = "A+"
        remark = "Outstanding performance"
    elif student_marks >= 80:
        grade = "A"
        remark = "Excellent performance"
    elif student_marks >= 70:
        grade = "B"
        remark = "Good performance"
    elif student_marks >= 60:
        grade = "C"
        remark = "Above average"
    elif student_marks >= 50:
        grade = "D"
        remark = "Average — scope for improvement"
    elif student_marks >= 40:
        grade = "E"
        remark = "Below average — barely passing"
    else:
        grade = "F"
        remark = "Fail — needs significant improvement"

    print(f"📋 Grade: {grade} | Remark: {remark}")
    return grade


# Boundary-value tests  ← important for edge-case handling
assign_letter_grade(100)   # Upper boundary  → A+
assign_letter_grade(90)    # Exact threshold  → A+
assign_letter_grade(89)    # Just below A+ threshold → A
assign_letter_grade(0)     # Lower boundary  → F
assign_letter_grade(40)    # Pass/fail boundary → E
assign_letter_grade(39)    # Just below pass  → F
assign_letter_grade(105)   # Out-of-range (invalid)


# ─────────────────────────────────────────────────────────────────────────────
# Section 4: Logical Operators Example
# ─────────────────────────────────────────────────────────────────────────────
# Python provides three logical operators:
#   `and`  — True only when BOTH operands are True
#   `or`   — True when AT LEAST ONE operand is True
#   `not`  — Inverts the truth value
#
# These operators let us express compound conditions concisely.

def evaluate_scholarship_eligibility(
    student_marks: int,
    family_income: float,
    has_disciplinary_record: bool,
) -> None:
    """
    Determine scholarship eligibility using compound conditions.

    Criteria:
      1. Academic merit    : marks >= 85
      2. Financial need    : family annual income < ₹5,00,000
      3. Clean record      : no disciplinary actions
      4. Special provision  : marks == 100 (perfect score) overrides income rule
    """
    print(f"\n--- Logical Operators Example ---")
    print(f"Marks: {student_marks} | Income: ₹{family_income:,.0f} | "
          f"Disciplinary record: {has_disciplinary_record}")

    # ── `not` operator ──
    # A student with a disciplinary record is immediately disqualified
    if has_disciplinary_record:
        print("❌ Disqualified: Disciplinary record found.")
        return

    # ── `and` operator ──
    # Both academic merit AND financial need must be satisfied
    meets_merit = student_marks >= 85
    meets_financial_need = family_income < 500_000

    if meets_merit and meets_financial_need:
        print("🎓 Eligible: Meets both academic merit and financial need criteria.")
        return

    # ── `or` operator ──
    # Special provision: a perfect score OR exceptional financial hardship
    # (income < ₹1,50,000) grants eligibility regardless of other factors
    has_perfect_score = student_marks == 100
    severe_financial_hardship = family_income < 150_000

    if has_perfect_score or severe_financial_hardship:
        print("🎓 Eligible (special provision): Perfect score or severe hardship.")
        return

    # ── Combined `not` with `and` ──
    # If the student has merit but does NOT meet financial criteria
    if meets_merit and not meets_financial_need:
        print("⏳ Waitlisted: Strong academics, but income exceeds threshold.")
        return

    # Default: does not qualify
    print("❌ Not eligible: Does not meet the required criteria.")


# Case 1: Meets both merit and financial need
evaluate_scholarship_eligibility(
    student_marks=92, family_income=350_000, has_disciplinary_record=False
)

# Case 2: Perfect score overrides income via `or`
evaluate_scholarship_eligibility(
    student_marks=100, family_income=800_000, has_disciplinary_record=False
)

# Case 3: Disciplinary record — disqualified via `not` logic
evaluate_scholarship_eligibility(
    student_marks=95, family_income=200_000, has_disciplinary_record=True
)

# Case 4: High marks but income too high — waitlisted via `and` + `not`
evaluate_scholarship_eligibility(
    student_marks=88, family_income=600_000, has_disciplinary_record=False
)

# Case 5: Severe hardship overrides low marks via `or`
evaluate_scholarship_eligibility(
    student_marks=60, family_income=120_000, has_disciplinary_record=False
)

# Case 6: Does not meet any criteria
evaluate_scholarship_eligibility(
    student_marks=70, family_income=550_000, has_disciplinary_record=False
)


# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  SUMMARY — Conditional Statements in Python")
print("=" * 60)
print("""
  1. `if`           → Executes a block when the condition is True.
  2. `if-else`      → Two branches — guarantees one always runs.
  3. `if-elif-else` → Multiple mutually exclusive conditions checked
                      in order; first match wins.
  4. Logical ops    → `and`, `or`, `not` combine/invert conditions
                      for powerful compound logic.

  Key best practices:
    • Always validate input BEFORE processing (guard clauses).
    • Use boundary-value testing to catch off-by-one errors.
    • Keep conditions mutually exclusive to avoid ambiguity.
    • Prefer early returns to reduce nesting depth.
""")
