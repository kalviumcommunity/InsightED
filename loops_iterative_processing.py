"""
=============================================================================
 Module: Using for and while Loops for Iterative Data Processing
 Author: InsightED Learning Module
 Description:
     Demonstrates Python loop constructs — for loops (with range and lists),
     while loops, break/continue control flow, and safe loop design — through
     real-world examples like student score processing and attendance tracking.
=============================================================================
"""


# ─────────────────────────────────────────────────────────────────────────────
# Section 1: For Loop with Range
# ─────────────────────────────────────────────────────────────────────────────
# `range(start, stop, step)` generates a sequence of integers.
# The loop variable takes each value in turn; the body executes once per value.
# Common use: when you know the exact number of iterations in advance.

def display_multiplication_table(number: int, up_to: int = 10) -> None:
    """Print the multiplication table for a given number."""
    print(f"\n{'='*50}")
    print(f"  Section 1: For Loop with Range")
    print(f"{'='*50}")
    print(f"\n📐 Multiplication table for {number}:\n")

    # range(1, up_to + 1) generates integers from 1 to up_to (inclusive)
    for multiplier in range(1, up_to + 1):
        product = number * multiplier
        print(f"  {number} × {multiplier:>2} = {product:>3}")

    print(f"\n✅ Table generated using {up_to} iterations via range().")


# Demonstrate: 7's table up to 12
display_multiplication_table(number=7, up_to=12)


# ─────────────────────────────────────────────────────────────────────────────
# Section 2: For Loop with List
# ─────────────────────────────────────────────────────────────────────────────
# A for loop can iterate directly over any iterable (list, tuple, string, etc.).
# Each element is bound to the loop variable on successive iterations.
# Common use: processing collections of real data — scores, names, records.

def analyze_student_scores(student_scores: dict[str, int]) -> None:
    """
    Analyze a dictionary of student scores:
      - Classify each student as Pass (≥40) or Fail
      - Track the highest scorer and compute the class average
    """
    print(f"\n{'='*50}")
    print(f"  Section 2: For Loop with List")
    print(f"{'='*50}")
    print(f"\n📊 Student Score Analysis:\n")

    total_marks = 0
    pass_count = 0
    fail_count = 0
    highest_score = -1
    topper_name = ""

    # .items() returns (key, value) pairs — clean Pythonic iteration
    for student_name, marks in student_scores.items():
        total_marks += marks

        # Classify pass/fail
        if marks >= 40:
            status = "✅ Pass"
            pass_count += 1
        else:
            status = "❌ Fail"
            fail_count += 1

        # Track the topper
        if marks > highest_score:
            highest_score = marks
            topper_name = student_name

        print(f"  {student_name:<12} → {marks:>3} marks  [{status}]")

    # Compute average safely (guard against empty dict)
    student_count = len(student_scores)
    class_average = total_marks / student_count if student_count > 0 else 0

    print(f"\n  📈 Class average : {class_average:.1f}")
    print(f"  🏆 Topper        : {topper_name} ({highest_score} marks)")
    print(f"  ✅ Passed        : {pass_count} | ❌ Failed: {fail_count}")


# Real-world dataset
scores = {
    "Aarav":    87,
    "Priya":    45,
    "Rohan":    92,
    "Sneha":    38,
    "Vikram":   73,
    "Diya":     61,
    "Karthik":  29,
}

analyze_student_scores(scores)


# ─────────────────────────────────────────────────────────────────────────────
# Section 3: While Loop Example
# ─────────────────────────────────────────────────────────────────────────────
# A `while` loop repeats as long as its condition remains True.
# CRITICAL: the condition variable MUST be updated inside the loop body,
# otherwise the loop will run forever (infinite loop).
# Common use: when the number of iterations is unknown upfront.

def simulate_attendance_tracker(total_days: int, daily_attendance: list[bool]) -> None:
    """
    Simulate tracking student attendance day-by-day.
    Stops early if attendance drops below 75% at any point.
    """
    print(f"\n{'='*50}")
    print(f"  Section 3: While Loop Example")
    print(f"{'='*50}")
    print(f"\n📅 Attendance Tracker (minimum 75% required):\n")

    current_day = 0           # Loop control variable — starts at 0
    days_present = 0

    # Loop runs as long as there are days left to process
    while current_day < total_days:
        # Read today's attendance from the list
        is_present = daily_attendance[current_day]

        if is_present:
            days_present += 1
            status_icon = "✅ Present"
        else:
            status_icon = "❌ Absent"

        # current_day is incremented EVERY iteration — prevents infinite loop
        current_day += 1

        # Calculate running attendance percentage
        attendance_percentage = (days_present / current_day) * 100

        print(f"  Day {current_day:>2}: {status_icon}  "
              f"(Running: {attendance_percentage:.0f}%)")

        # Early warning if attendance falls below threshold
        if current_day >= 5 and attendance_percentage < 75:
            print(f"\n  ⚠️  WARNING: Attendance dropped to {attendance_percentage:.0f}% "
                  f"after {current_day} days!")
            print(f"  📌 Student flagged for counselling.\n")
            break  # Exit the while loop early

    # Summary
    final_percentage = (days_present / current_day) * 100 if current_day > 0 else 0
    print(f"  📊 Final: {days_present}/{current_day} days present "
          f"({final_percentage:.0f}%)")


# 15 days of attendance data (True = present, False = absent)
attendance_record = [
    True, True, False, True, True,     # Week 1
    True, False, False, True, False,   # Week 2
    True, True, True, False, True,     # Week 3
]

simulate_attendance_tracker(total_days=15, daily_attendance=attendance_record)


# ─────────────────────────────────────────────────────────────────────────────
# Section 4: Using break and continue
# ─────────────────────────────────────────────────────────────────────────────
# `break`    — Immediately exits the ENTIRE loop (no more iterations).
# `continue` — Skips the REST of the current iteration and jumps to the next.
# These are flow-control tools that make loops smarter and more efficient.

def find_first_failing_student(student_records: list[tuple[str, int]]) -> None:
    """
    Demonstrate `break`: scan student records and stop at the FIRST failure.
    This avoids processing the entire list when only the first match matters.
    """
    print(f"\n{'='*50}")
    print(f"  Section 4a: Using break")
    print(f"{'='*50}")
    print(f"\n🔍 Scanning for the first failing student (marks < 40):\n")

    for student_name, marks in student_records:
        print(f"  Checking {student_name}... ({marks} marks)", end="")

        if marks < 40:
            # Found what we need — no point checking the rest
            print(f"  ← ❌ FAIL (first failure found)")
            print(f"\n  🛑 Search stopped. First failing student: {student_name}")
            break
        else:
            print(f"  ← ✅ Pass")
    else:
        # This else block runs ONLY if the loop completed WITHOUT a break
        print(f"\n  🎉 All students passed! No failures found.")


records = [
    ("Aarav", 78),
    ("Priya", 85),
    ("Rohan", 56),
    ("Sneha", 33),   # ← First failure — loop should stop here
    ("Vikram", 91),
    ("Diya", 27),
]

find_first_failing_student(records)


def process_scores_skip_invalid(raw_scores: list[int]) -> None:
    """
    Demonstrate `continue`: process a list of scores but skip any
    invalid (negative) values without stopping the entire loop.
    """
    print(f"\n{'='*50}")
    print(f"  Section 4b: Using continue")
    print(f"{'='*50}")
    print(f"\n🧹 Processing scores (skipping invalid negatives):\n")

    valid_total = 0
    valid_count = 0

    for index, score in enumerate(raw_scores, start=1):
        # Skip invalid entries — continue jumps to the next iteration
        if score < 0:
            print(f"  Score #{index}: {score:>4}  ← ⚠️ SKIPPED (invalid negative)")
            continue

        # This code only runs for valid scores (continue skips past it)
        valid_total += score
        valid_count += 1
        print(f"  Score #{index}: {score:>4}  ← ✅ Processed")

    # Final summary
    average = valid_total / valid_count if valid_count > 0 else 0
    skipped = len(raw_scores) - valid_count
    print(f"\n  📊 Valid scores: {valid_count} | Skipped: {skipped}")
    print(f"  📈 Average (valid only): {average:.1f}")


# Dataset with some corrupted/invalid entries
raw_data = [85, 92, -1, 76, -5, 88, 64, -3, 95, 71]
process_scores_skip_invalid(raw_data)


# ─────────────────────────────────────────────────────────────────────────────
# Section 5: Avoiding Infinite Loops
# ─────────────────────────────────────────────────────────────────────────────
# An infinite loop occurs when the loop condition NEVER becomes False.
# This section shows common mistakes and their safe alternatives.

def demonstrate_safe_while_loop() -> None:
    """
    Show a while loop with THREE safety mechanisms:
      1. Proper condition variable update
      2. A maximum iteration cap (safety net)
      3. Clear termination logging
    """
    print(f"\n{'='*50}")
    print(f"  Section 5: Avoiding Infinite Loops")
    print(f"{'='*50}")

    # ── DANGEROUS pattern (commented out — DO NOT RUN) ──────────────────────
    # counter = 0
    # while counter < 5:
    #     print(counter)
    #     # BUG: counter is NEVER incremented → infinite loop!
    # ────────────────────────────────────────────────────────────────────────

    print(f"\n  ⚠️  Dangerous pattern (DO NOT USE):")
    print(f"      counter = 0")
    print(f"      while counter < 5:")
    print(f"          print(counter)")
    print(f"          # ← Missing: counter += 1  → INFINITE LOOP!\n")

    # ── SAFE pattern ────────────────────────────────────────────────────────
    print(f"  ✅ Safe pattern with three safeguards:\n")

    # Safeguard 1: Proper condition variable initialization
    attempts = 0
    max_attempts = 10    # Safeguard 2: Hard cap prevents runaway execution

    # Simulating: keep rolling a "dice" until we get a target number
    import random
    random.seed(42)      # Fixed seed for reproducible output
    target_number = 6

    while attempts < max_attempts:
        attempts += 1    # Safeguard 1: ALWAYS update the loop variable
        dice_roll = random.randint(1, 6)

        print(f"    Attempt {attempts:>2}: Rolled {dice_roll}", end="")

        if dice_roll == target_number:
            print(f"  ← 🎯 Target {target_number} hit!")
            print(f"\n  ✅ Loop exited naturally after {attempts} attempt(s).")
            break
        else:
            print()
    else:
        # Safeguard 3: Handle the case where max attempts are exhausted
        print(f"\n  🛑 Safety cap reached ({max_attempts} attempts).")
        print(f"     Target {target_number} was NOT found — but loop exited safely.")

    # ── Summary of best practices ───────────────────────────────────────────
    print(f"\n  💡 Three rules to prevent infinite loops:")
    print(f"     1. Always update the condition variable inside the loop body.")
    print(f"     2. Set a maximum iteration cap as a safety net.")
    print(f"     3. Log or handle the case where the cap is reached.")


demonstrate_safe_while_loop()


# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"  SUMMARY — Loops for Iterative Data Processing")
print(f"{'='*60}")
print("""
  1. for + range()  → Use when the iteration count is known.
                      range(start, stop, step) generates integers.

  2. for + list     → Use to iterate over collections (lists, dicts, etc.).
                      Pythonic: use .items() for dicts, enumerate() for indices.

  3. while          → Use when the iteration count is UNKNOWN; depends on
                      a condition that changes during execution.

  4. break          → Exit the loop immediately when a condition is met.
     continue       → Skip the current iteration and proceed to the next.
     for-else       → The else block runs ONLY if the loop wasn't broken.

  5. Infinite loops → Prevented by:
                      • Always updating the loop variable
                      • Setting maximum iteration caps
                      • Logging / handling exhaustion gracefully

  Key best practices:
    • Prefer `for` loops when iterating over known collections.
    • Use `while` only when termination depends on runtime conditions.
    • Always ensure the loop condition will eventually become False.
    • Use `break` to exit early and avoid unnecessary work.
    • Use `continue` to skip invalid data without stopping the loop.
""")
