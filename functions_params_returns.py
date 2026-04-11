"""
=============================================================================
 Module: Passing Data into Functions and Returning Results
 Author: InsightED Learning Module
 Description:
     Demonstrates how to pass data into functions via parameters, return
     computed results (instead of printing inside functions), store and
     reuse returned values, and chain function outputs as inputs to other
     functions — through real-world examples like student grading, loan
     eligibility, and invoice generation.
=============================================================================
"""


# ─────────────────────────────────────────────────────────────────────────────
# Section 1: Function with Parameters
# ─────────────────────────────────────────────────────────────────────────────
# Parameters let functions accept external data, making them flexible and
# reusable.  The function body operates on the parameter VALUES — never on
# hardcoded data.  This separation is what makes functions truly reusable.

def calculate_percentage(scored_marks: float, total_marks: float) -> float:
    """
    Calculate percentage from scored and total marks.

    Parameters:
        scored_marks : Marks obtained by the student
        total_marks  : Maximum possible marks

    Returns:
        Percentage as a float, or 0.0 for invalid input.

    NOTE: This function RETURNS the result — it does NOT print it.
          Printing is the caller's responsibility.
    """
    # Guard clause: reject invalid inputs
    if total_marks <= 0:
        return 0.0
    if scored_marks < 0:
        return 0.0

    # Cap percentage at 100% (scored cannot exceed total logically)
    if scored_marks > total_marks:
        scored_marks = total_marks

    percentage = (scored_marks / total_marks) * 100
    return round(percentage, 2)


def calculate_discount(original_price: float, discount_rate: float) -> float:
    """
    Calculate the discounted price of a product.

    Parameters:
        original_price : Original price before discount
        discount_rate  : Discount percentage (0–100)

    Returns:
        Final price after discount, or original price for invalid rates.
    """
    # Guard: reject negative prices
    if original_price < 0:
        return 0.0

    # Clamp discount rate to valid range (0% to 100%)
    effective_rate = max(0, min(discount_rate, 100))

    discount_amount = original_price * (effective_rate / 100)
    final_price = original_price - discount_amount
    return round(final_price, 2)


# ── Demonstration ───────────────────────────────────────────────────────────
print(f"\n{'='*55}")
print(f"  Section 1: Function with Parameters")
print(f"{'='*55}")

# Calling with different arguments — same function, different data
print(f"\n📊 Percentage calculations:")
print(f"  432/500 → {calculate_percentage(432, 500)}%")
print(f"  375/500 → {calculate_percentage(375, 500)}%")
print(f"  280/400 → {calculate_percentage(280, 400)}%")

# Edge cases
print(f"\n⚠️  Edge cases:")
print(f"  Negative marks  → {calculate_percentage(-10, 100)}%  (returns 0.0)")
print(f"  Zero total      → {calculate_percentage(80, 0)}%  (returns 0.0)")
print(f"  Exceeds total   → {calculate_percentage(110, 100)}%  (capped at 100)")

# Explanation:
# `calculate_percentage` accepts ANY pair of numbers — nothing is hardcoded.
# The function RETURNS the result; the caller decides how to use it (print,
# store, pass to another function, etc.).


# ─────────────────────────────────────────────────────────────────────────────
# Section 2: Returning Values
# ─────────────────────────────────────────────────────────────────────────────
# `return` sends a value BACK to the caller.  This is fundamentally different
# from `print` — print displays text on screen but produces NO usable value.
#
# KEY RULE: Functions that COMPUTE should RETURN.
#           Functions that DISPLAY may print (but ideally take data as input).

def classify_grade(percentage: float) -> str:
    """
    Classify a percentage into a letter grade.

    Returns a grade string — does NOT print anything.
    """
    if percentage < 0 or percentage > 100:
        return "INVALID"

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def assess_pass_fail(percentage: float, passing_threshold: float = 40.0) -> bool:
    """
    Determine if a student has passed.

    Parameters:
        percentage         : Student's percentage score
        passing_threshold  : Minimum percentage to pass (default: 40.0)

    Returns:
        True if passed, False otherwise.
    """
    return percentage >= passing_threshold


def compute_tax(annual_income: float) -> dict:
    """
    Compute income tax based on Indian tax slab (simplified).

    Returns a dictionary with tax details — structured return value.
    """
    if annual_income <= 0:
        return {"taxable_income": 0, "tax_amount": 0, "tax_bracket": "N/A"}

    # Simplified Indian tax slabs
    if annual_income <= 250_000:
        tax = 0
        bracket = "Nil (up to ₹2.5L)"
    elif annual_income <= 500_000:
        tax = (annual_income - 250_000) * 0.05
        bracket = "5% (₹2.5L – ₹5L)"
    elif annual_income <= 1_000_000:
        tax = 12_500 + (annual_income - 500_000) * 0.20
        bracket = "20% (₹5L – ₹10L)"
    else:
        tax = 112_500 + (annual_income - 1_000_000) * 0.30
        bracket = "30% (above ₹10L)"

    return {
        "taxable_income": annual_income,
        "tax_amount": round(tax, 2),
        "tax_bracket": bracket,
    }


# ── Demonstration ───────────────────────────────────────────────────────────
print(f"\n{'='*55}")
print(f"  Section 2: Returning Values")
print(f"{'='*55}")

# Return a string
grade = classify_grade(87.5)
print(f"\n📋 Grade classification:")
print(f"  87.5% → Grade: {grade}")

# Return a boolean
has_passed = assess_pass_fail(87.5)
print(f"  Passed? {has_passed}")

# Return a dictionary (structured data)
tax_info = compute_tax(750_000)
print(f"\n💰 Tax computation for ₹7,50,000:")
print(f"  Tax bracket : {tax_info['tax_bracket']}")
print(f"  Tax amount  : ₹{tax_info['tax_amount']:,.0f}")

# Explanation:
# Each function returns a DIFFERENT type (float, str, bool, dict) —
# Python is flexible about return types.  The caller captures the returned
# value in a variable and decides what to do with it.


# ─────────────────────────────────────────────────────────────────────────────
# Section 3: Using Returned Values
# ─────────────────────────────────────────────────────────────────────────────
# Returned values aren't just for printing — they can be stored in variables,
# used in calculations, compared in conditions, or added to collections.

def calculate_gpa(marks_list: list[float], max_marks: float) -> float:
    """
    Calculate GPA on a 10-point scale from a list of subject marks.

    Returns GPA rounded to 2 decimal places.
    """
    if not marks_list or max_marks <= 0:
        return 0.0

    total_percentage = sum(
        calculate_percentage(marks, max_marks) for marks in marks_list
    )
    average_percentage = total_percentage / len(marks_list)

    # Convert percentage to 10-point GPA scale
    gpa = average_percentage / 10
    return round(gpa, 2)


def determine_scholarship_tier(gpa: float) -> tuple[str, float]:
    """
    Determine scholarship tier based on GPA.

    Returns:
        A tuple of (tier_name, scholarship_percentage).
    """
    if gpa >= 9.5:
        return ("Platinum", 100.0)
    elif gpa >= 9.0:
        return ("Gold", 75.0)
    elif gpa >= 8.0:
        return ("Silver", 50.0)
    elif gpa >= 7.0:
        return ("Bronze", 25.0)
    else:
        return ("None", 0.0)


# ── Demonstration ───────────────────────────────────────────────────────────
print(f"\n{'='*55}")
print(f"  Section 3: Using Returned Values")
print(f"{'='*55}")

# Step 1: Store returned values in variables
subject_marks = [92, 85, 78, 95, 88]
student_gpa = calculate_gpa(subject_marks, max_marks=100)

print(f"\n📚 Student's subject marks: {subject_marks}")
print(f"   Calculated GPA: {student_gpa}")

# Step 2: Use the returned value in a CONDITION
if student_gpa >= 8.0:
    print(f"   🎉 Eligible for Dean's List!")
else:
    print(f"   📌 Not on Dean's List this semester.")

# Step 3: Use the returned value in FURTHER COMPUTATION
tuition_fee = 150_000
scholarship_tier, scholarship_percent = determine_scholarship_tier(student_gpa)
scholarship_amount = tuition_fee * (scholarship_percent / 100)
fee_after_scholarship = tuition_fee - scholarship_amount

print(f"\n💰 Scholarship Assessment:")
print(f"   GPA: {student_gpa} → Tier: {scholarship_tier} ({scholarship_percent}% off)")
print(f"   Original fee    : ₹{tuition_fee:,.0f}")
print(f"   Scholarship     : -₹{scholarship_amount:,.0f}")
print(f"   Fee after award : ₹{fee_after_scholarship:,.0f}")

# Step 4: Use returned values in a collection (building a report)
students_data = [
    ("Aarav",   [92, 85, 78, 95, 88]),
    ("Priya",   [76, 82, 69, 71, 80]),
    ("Rohan",   [95, 98, 92, 97, 96]),
    ("Sneha",   [55, 48, 62, 44, 58]),
    ("Vikram",  [88, 91, 85, 79, 93]),
]

print(f"\n📊 Class GPA Report:")
print(f"   {'Name':<10} {'GPA':>5}  {'Tier':<10} {'Scholarship':>12}")
print(f"   {'─'*10} {'─'*5}  {'─'*10} {'─'*12}")

for name, marks in students_data:
    gpa = calculate_gpa(marks, max_marks=100)             # returned value → variable
    tier, percent = determine_scholarship_tier(gpa)        # returned value → variable
    discount = tuition_fee * (percent / 100)               # used in computation
    print(f"   {name:<10} {gpa:>5}  {tier:<10} ₹{discount:>10,.0f}")

# Explanation:
# Returned values are the currency of function communication.  By returning
# instead of printing, functions become composable building blocks — their
# output can drive conditions, feed calculations, or build data structures.


# ─────────────────────────────────────────────────────────────────────────────
# Section 4: Function Chaining
# ─────────────────────────────────────────────────────────────────────────────
# Function chaining means passing the RETURN VALUE of one function directly
# as an ARGUMENT to another function.  This creates a pipeline where data
# flows through a sequence of transformations.
#
# Pattern:  result = func_c(func_b(func_a(raw_data)))
#           ↑ data flows from innermost call outward

def extract_subject_total(
    subject_scores: dict[str, float],
) -> float:
    """
    Sum all subject scores.

    Returns the total marks scored.
    """
    if not subject_scores:
        return 0.0
    return sum(subject_scores.values())


def compute_overall_percentage(
    total_scored: float,
    number_of_subjects: int,
    max_per_subject: float = 100.0,
) -> float:
    """
    Compute overall percentage from total scored marks.

    Returns percentage rounded to 2 places.
    """
    grand_total = number_of_subjects * max_per_subject
    if grand_total <= 0:
        return 0.0
    return round((total_scored / grand_total) * 100, 2)


def generate_result_summary(
    student_name: str,
    percentage: float,
    grade: str,
    passed: bool,
) -> str:
    """
    Generate a formatted result summary string.

    Returns a multi-line string — does NOT print.
    """
    status_icon = "✅ PASSED" if passed else "❌ FAILED"

    summary = (
        f"\n  ╔═══════════════════════════════════════════════╗\n"
        f"  ║         📜 STUDENT RESULT SUMMARY             ║\n"
        f"  ╠═══════════════════════════════════════════════╣\n"
        f"  ║  Name       : {student_name:<32}║\n"
        f"  ║  Percentage : {percentage:<32}║\n"
        f"  ║  Grade      : {grade:<32}║\n"
        f"  ║  Status     : {status_icon:<32}║\n"
        f"  ╚═══════════════════════════════════════════════╝"
    )
    return summary


# ── Demonstration: Full Pipeline ─────────────────────────────────────────────
print(f"\n{'='*55}")
print(f"  Section 4: Function Chaining")
print(f"{'='*55}")

# Raw input data
student_name = "Aarav Sharma"
scores = {
    "Mathematics": 92,
    "Physics": 85,
    "Chemistry": 78,
    "English": 95,
    "Computer Science": 88,
}

print(f"\n📝 Raw scores: {scores}")

# ── Chain 1: Step-by-step (explicit — best for readability) ────────────────
print(f"\n🔗 Chain 1 — Step-by-step chaining:\n")

# Step A: Extract total → returns float
total = extract_subject_total(scores)
print(f"  Step A → extract_subject_total()  = {total}")

# Step B: Compute percentage → uses return from Step A
percentage = compute_overall_percentage(total, len(scores))
print(f"  Step B → compute_overall_percentage({total}, {len(scores)}) = {percentage}%")

# Step C: Classify grade → uses return from Step B
grade = classify_grade(percentage)
print(f"  Step C → classify_grade({percentage}) = '{grade}'")

# Step D: Assess pass/fail → uses return from Step B
passed = assess_pass_fail(percentage)
print(f"  Step D → assess_pass_fail({percentage}) = {passed}")

# Step E: Generate summary → uses returns from Steps B, C, D
summary = generate_result_summary(student_name, percentage, grade, passed)
print(f"  Step E → generate_result_summary():")
print(summary)


# ── Chain 2: Inline chaining (compact — for experienced readers) ───────────
print(f"\n🔗 Chain 2 — Inline chaining (compact):\n")

# The return value of one function flows directly into the next
# No intermediate variables needed (but harder to debug)
compact_grade = classify_grade(
    compute_overall_percentage(
        extract_subject_total(scores),
        len(scores),
    )
)
print(f"  Inline result: Grade = '{compact_grade}'")
print(f"  ↑ extract_subject_total → compute_overall_percentage → classify_grade")


# ── Chain 3: Real-world pipeline — Invoice generator ─────────────────────────
print(f"\n🔗 Chain 3 — Real-world pipeline: Invoice Generator\n")


def calculate_subtotal(items: list[tuple[str, float, int]]) -> float:
    """Calculate subtotal from a list of (item_name, unit_price, quantity)."""
    return sum(price * qty for _, price, qty in items)


def apply_tax(subtotal: float, tax_rate: float = 18.0) -> dict:
    """Apply tax and return breakdown."""
    tax_amount = round(subtotal * (tax_rate / 100), 2)
    return {
        "subtotal": subtotal,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "grand_total": round(subtotal + tax_amount, 2),
    }


def format_invoice(
    customer_name: str,
    items: list[tuple[str, float, int]],
    billing: dict,
) -> str:
    """Format a complete invoice as a string."""
    lines = [
        f"\n  ┌───────────────────────────────────────────────┐",
        f"  │             🧾 TAX INVOICE                    │",
        f"  ├───────────────────────────────────────────────┤",
        f"  │  Customer: {customer_name:<35}│",
        f"  ├───────────────────────────────────────────────┤",
    ]

    for item_name, price, qty in items:
        line_total = price * qty
        lines.append(
            f"  │  {item_name:<18} {qty:>3} × ₹{price:>7,.0f} = ₹{line_total:>8,.0f} │"
        )

    lines.extend([
        f"  ├───────────────────────────────────────────────┤",
        f"  │  Subtotal              : ₹{billing['subtotal']:>14,.2f}  │",
        f"  │  GST ({billing['tax_rate']}%)            : ₹{billing['tax_amount']:>14,.2f}  │",
        f"  │  ─────────────────────────────────────────    │",
        f"  │  GRAND TOTAL           : ₹{billing['grand_total']:>14,.2f}  │",
        f"  └───────────────────────────────────────────────┘",
    ])

    return "\n".join(lines)


# Data
customer = "Priya Menon"
order_items = [
    ("Laptop",       65_000, 1),
    ("Mouse",           800, 2),
    ("USB Hub",       1_200, 1),
    ("Monitor Stand",  3_500, 1),
]

# CHAINED PIPELINE: items → subtotal → tax → invoice
subtotal = calculate_subtotal(order_items)           # Step 1: returns float
billing_details = apply_tax(subtotal)                 # Step 2: returns dict (uses Step 1)
invoice_text = format_invoice(                        # Step 3: returns string (uses Step 2)
    customer, order_items, billing_details
)
print(invoice_text)                                   # Caller prints — functions only return

print(f"\n  💡 Pipeline: calculate_subtotal → apply_tax → format_invoice")
print(f"     Each function's RETURN feeds the next function's PARAMETERS.")


# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"  SUMMARY — Passing Data and Returning Results")
print(f"{'='*60}")
print("""
  1. Parameters      → Functions accept external data via parameters.
                       Never hardcode values inside functions.

  2. Return values   → Use `return` to send results back to the caller.
                       Functions that COMPUTE should RETURN, not print.
                       Return types can be: int, float, str, bool, dict,
                       tuple, list — whatever the caller needs.

  3. Using returns   → Returned values can be:
                       • Stored in variables for later use
                       • Used in conditions (if/elif)
                       • Fed into further calculations
                       • Added to collections (lists, dicts)

  4. Chaining        → The return of function A becomes the argument of
                       function B.  This creates composable pipelines:
                         raw data → transform → classify → format → output

  Key best practices:
    • Functions RETURN data; callers PRINT data (separation of concerns).
    • Each function does ONE thing — single responsibility principle.
    • Validate inputs with guard clauses (defensive programming).
    • Prefer explicit step-by-step chaining over deeply nested inline calls.
    • Name functions as verb+noun: calculate_tax, classify_grade, format_invoice.
""")
