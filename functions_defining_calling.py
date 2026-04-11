"""
=============================================================================
 Module: Defining and Calling Python Functions
 Author: InsightED Learning Module
 Description:
     Demonstrates core function concepts — defining with `def`, calling,
     passing arguments (positional, keyword, default), return values, and
     understanding local vs global scope — through real-world examples
     like student grading, BMI calculation, and eligibility checks.
=============================================================================
"""


# ─────────────────────────────────────────────────────────────────────────────
# Section 1: Defining a Function
# ─────────────────────────────────────────────────────────────────────────────
# A function is defined using the `def` keyword, followed by a name, parentheses
# for parameters, and a colon.  The indented block below it is the function body.
# Functions encapsulate reusable logic — write once, call many times.

def display_welcome_banner() -> None:
    """Display a formatted welcome banner — no parameters, no return value."""
    print("\n" + "═" * 50)
    print("  🎓 Welcome to the InsightED Grading System")
    print("═" * 50)


def calculate_percentage(scored_marks: float, total_marks: float) -> float:
    """
    Calculate percentage from scored and total marks.

    A well-defined function has:
      - A clear, descriptive name (verb + noun)
      - Type hints for parameters and return value
      - A docstring explaining what it does
      - A single responsibility (only calculates — does NOT print)
    """
    # Guard clause: prevent division by zero and reject invalid input
    if total_marks <= 0:
        return 0.0

    percentage = (scored_marks / total_marks) * 100
    return round(percentage, 2)


# Explanation:
# `display_welcome_banner` takes no arguments and returns nothing (pure side-effect).
# `calculate_percentage` takes two numbers and RETURNS a result — it's a pure function
# with no side effects, making it predictable, testable, and reusable.

print("\n--- Section 1: Defining a Function ---")
print("✅ Two functions defined: display_welcome_banner() and calculate_percentage()")
print("   • display_welcome_banner → no params, no return (action function)")
print("   • calculate_percentage   → 2 params, returns float (computation function)")


# ─────────────────────────────────────────────────────────────────────────────
# Section 2: Calling a Function
# ─────────────────────────────────────────────────────────────────────────────
# A function does NOTHING until it is called.  Calling means writing the
# function name followed by parentheses (with arguments if required).
# The function executes its body and optionally returns a value.

print("\n--- Section 2: Calling a Function ---\n")

# Call 1: Calling a function with no arguments
display_welcome_banner()

# Call 2: Calling a function that RETURNS a value — capture it in a variable
student_percentage = calculate_percentage(scored_marks=432, total_marks=500)
print(f"\n📊 Student scored 432/500 → Percentage: {student_percentage}%")

# Call 3: Using the return value directly in an expression (no intermediate variable)
print(f"📊 Another student: {calculate_percentage(375, 500)}%")

# Call 4: Edge case — what happens with total_marks = 0?
edge_case_result = calculate_percentage(scored_marks=80, total_marks=0)
print(f"📊 Edge case (0 total): {edge_case_result}%  ← handled gracefully")

# Explanation:
# A function call transfers control to the function body.  When the body finishes
# (or hits `return`), control returns to the caller.  If the function returns a
# value, the call expression evaluates to that value.


# ─────────────────────────────────────────────────────────────────────────────
# Section 3: Parameters and Arguments
# ─────────────────────────────────────────────────────────────────────────────
# Parameters are the VARIABLES in the function definition (placeholders).
# Arguments are the actual VALUES passed when the function is called.
#
# Python supports several argument-passing styles:
#   1. Positional arguments  — matched by order
#   2. Keyword arguments     — matched by name (explicit, readable)
#   3. Default parameters    — fallback values when arguments are omitted

print(f"\n{'='*50}")
print(f"  Section 3: Parameters and Arguments")
print(f"{'='*50}")


# ── 3a: Positional Arguments ────────────────────────────────────────────────

def create_student_report(student_name: str, roll_number: int, marks: float) -> str:
    """
    Generate a formatted report string for a student.

    Parameters (positional):
        student_name : Name of the student
        roll_number  : Unique roll number
        marks        : Marks obtained (out of 100)
    """
    # Determine pass/fail status inline
    status = "PASS ✅" if marks >= 40 else "FAIL ❌"

    report = (
        f"  ┌──────────────────────────────────┐\n"
        f"  │  Student Report                  │\n"
        f"  ├──────────────────────────────────┤\n"
        f"  │  Name : {student_name:<24}│\n"
        f"  │  Roll : {roll_number:<24}│\n"
        f"  │  Marks: {marks:<24}│\n"
        f"  │  Status: {status:<23}│\n"
        f"  └──────────────────────────────────┘"
    )
    return report


print("\n📋 3a — Positional Arguments:\n")

# Arguments are matched by POSITION: 1st → student_name, 2nd → roll_number, etc.
report_text = create_student_report("Aarav Sharma", 101, 87)
print(report_text)


# ── 3b: Keyword Arguments ───────────────────────────────────────────────────

print("\n📋 3b — Keyword Arguments:\n")

# Using keyword arguments — order doesn't matter, intent is crystal clear
report_text = create_student_report(
    marks=35,
    student_name="Priya Menon",
    roll_number=102,
)
print(report_text)


# ── 3c: Default Parameters ──────────────────────────────────────────────────

def calculate_bmi(
    weight_kg: float,
    height_m: float,
    round_digits: int = 1,    # default parameter — optional when calling
) -> dict:
    """
    Calculate Body Mass Index and classify the result.

    Parameters:
        weight_kg    : Body weight in kilograms
        height_m     : Height in metres
        round_digits : Decimal places for rounding (default: 1)

    Returns:
        A dictionary with BMI value and category.
    """
    # Validate inputs — functions should be defensive
    if weight_kg <= 0 or height_m <= 0:
        return {"bmi": 0.0, "category": "Invalid input"}

    bmi_value = round(weight_kg / (height_m ** 2), round_digits)

    # Classify using WHO standards
    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 25.0:
        category = "Normal weight"
    elif bmi_value < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    return {"bmi": bmi_value, "category": category}


print("\n📋 3c — Default Parameters:\n")

# Call WITHOUT the optional parameter — uses default round_digits=1
result_1 = calculate_bmi(weight_kg=68, height_m=1.75)
print(f"  BMI (default rounding) : {result_1['bmi']} → {result_1['category']}")

# Call WITH the optional parameter — overrides the default
result_2 = calculate_bmi(weight_kg=68, height_m=1.75, round_digits=3)
print(f"  BMI (3 decimal places) : {result_2['bmi']} → {result_2['category']}")

# Edge case: invalid input
result_3 = calculate_bmi(weight_kg=-5, height_m=1.70)
print(f"  BMI (negative weight)  : {result_3['bmi']} → {result_3['category']}")


# ── 3d: Multiple Return Values ──────────────────────────────────────────────

def analyze_class_performance(marks_list: list[int]) -> tuple[float, int, int]:
    """
    Analyze a list of marks and return multiple statistics.

    Returns:
        A tuple of (average, highest, lowest).
    """
    if not marks_list:
        return (0.0, 0, 0)

    average = round(sum(marks_list) / len(marks_list), 1)
    highest = max(marks_list)
    lowest = min(marks_list)

    return (average, highest, lowest)


print("\n📋 3d — Multiple Return Values:\n")

class_marks = [87, 45, 92, 38, 73, 61, 29, 95, 55, 80]

# Tuple unpacking — clean way to capture multiple return values
class_avg, class_high, class_low = analyze_class_performance(class_marks)

print(f"  Class of {len(class_marks)} students:")
print(f"    📈 Average : {class_avg}")
print(f"    🏆 Highest : {class_high}")
print(f"    📉 Lowest  : {class_low}")

# Edge case: empty list
empty_avg, empty_high, empty_low = analyze_class_performance([])
print(f"\n  Empty class (edge case): avg={empty_avg}, high={empty_high}, low={empty_low}")


# ─────────────────────────────────────────────────────────────────────────────
# Section 4: Function Scope (Local vs Global)
# ─────────────────────────────────────────────────────────────────────────────
# SCOPE determines where a variable is visible and accessible.
#
# Local scope  — Variables created INSIDE a function.  They exist only while
#                the function is running and are destroyed when it returns.
#
# Global scope — Variables created OUTSIDE all functions.  They are accessible
#                everywhere but should NOT be modified inside functions without
#                the `global` keyword (and even then, it's discouraged).
#
# BEST PRACTICE: Pass data INTO functions via parameters and get results OUT
# via return values.  This makes functions self-contained and predictable.

print(f"\n{'='*50}")
print(f"  Section 4: Function Scope (Local vs Global)")
print(f"{'='*50}")


# ── 4a: Local Variables ─────────────────────────────────────────────────────

def compute_grade(marks: int) -> str:
    """
    Determine the letter grade for given marks.
    `grade` is a LOCAL variable — it exists only inside this function.
    """
    # `grade` is created here — LOCAL to compute_grade()
    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"

    return grade    # The VALUE is returned, not the variable itself


print("\n🔍 4a — Local Variables:\n")

result = compute_grade(85)
print(f"  compute_grade(85) returned: '{result}'")

# Trying to access `grade` here would raise NameError because it's LOCAL:
# print(grade)  ← ❌ NameError: name 'grade' is not defined
print(f"  `grade` variable does NOT exist outside the function (local scope).")


# ── 4b: Global Variables — Reading vs Modifying ─────────────────────────────

# This is a GLOBAL variable — defined at module level
institution_name = "InsightED Academy"


def print_certificate(student_name: str, course: str) -> None:
    """
    Print a certificate using the global `institution_name`.
    Functions CAN READ global variables without any special keyword.
    """
    print(f"\n  ╔══════════════════════════════════════════╗")
    print(f"  ║       📜 CERTIFICATE OF COMPLETION       ║")
    print(f"  ╠══════════════════════════════════════════╣")
    print(f"  ║  Institution : {institution_name:<26}║")
    print(f"  ║  Student     : {student_name:<26}║")
    print(f"  ║  Course      : {course:<26}║")
    print(f"  ╚══════════════════════════════════════════╝")


print("\n🔍 4b — Global Variables (reading):")
print_certificate("Rohan Gupta", "Python Fundamentals")
print(f"\n  ✅ The function READ the global `institution_name` without issues.")


# ── 4c: Why NOT to Modify Globals (and the safe alternative) ────────────────

# ❌ BAD PRACTICE — modifying global state inside a function
total_students_bad = 0

def register_student_bad(name: str) -> None:
    """BAD: Uses `global` keyword to modify external state."""
    global total_students_bad
    total_students_bad += 1    # Side effect — unpredictable in large codebases
    print(f"  [BAD]  Registered: {name} (total: {total_students_bad})")


# ✅ GOOD PRACTICE — pass state in, return new state out
def register_student_good(name: str, current_count: int) -> int:
    """GOOD: Takes current count as input, returns updated count."""
    updated_count = current_count + 1    # Local variable — no side effects
    print(f"  [GOOD] Registered: {name} (total: {updated_count})")
    return updated_count


print(f"\n🔍 4c — Global Modification: Bad vs Good Practice:\n")

# Bad approach — relies on global state
register_student_bad("Aarav")
register_student_bad("Priya")
print(f"  Global `total_students_bad` = {total_students_bad}  ← hidden side effect\n")

# Good approach — explicit, predictable, testable
student_count = 0
student_count = register_student_good("Sneha", student_count)
student_count = register_student_good("Vikram", student_count)
print(f"  Local `student_count` = {student_count}  ← fully controlled by caller")


# ── 4d: Scope Summary Demonstration ─────────────────────────────────────────

def scope_demonstration() -> None:
    """Show that local variables shadow global ones with the same name."""
    # This `message` is LOCAL — it shadows any global `message`
    message = "I am LOCAL to scope_demonstration()"
    print(f"  Inside function : {message}")


# This `message` is GLOBAL
message = "I am GLOBAL"

print(f"\n🔍 4d — Scope Shadowing:\n")
print(f"  Before function : {message}")
scope_demonstration()
print(f"  After function  : {message}  ← global is UNCHANGED")
print(f"\n  💡 The local `message` inside the function did NOT affect the global one.")


# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"  SUMMARY — Defining and Calling Python Functions")
print(f"{'='*60}")
print("""
  1. Defining     → Use `def function_name(params):` with a docstring.
                    Each function should do ONE thing well.

  2. Calling      → Write the function name with parentheses and arguments.
                    Capture return values in variables for later use.

  3. Parameters   → Positional args are matched by order.
                    Keyword args are matched by name (more readable).
                    Default params provide fallback values.
                    Functions can return multiple values via tuples.

  4. Scope        → Local variables live inside the function only.
                    Global variables CAN be read but SHOULD NOT be modified.
                    Best practice: pass data IN via params, get data OUT
                    via return — keeps functions pure and predictable.

  Key best practices:
    • Give functions clear, verb-based names (calculate_bmi, not bmi).
    • Use type hints and docstrings for documentation.
    • Validate inputs with guard clauses (defensive programming).
    • Avoid global state — prefer parameters and return values.
    • Keep functions short and focused (single responsibility).
""")
