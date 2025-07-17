import datetime
# List of commonly used weak MPINs
common_mpins = [
    "1234", "1111", "0000", "1212", "7777", "1004", "2000", "6969", "2222", "9999",
    "123456", "000000", "111111", "121212", "654321", "999999"
]
def get_date_patterns(date_str):
    """Generate different patterns from a date string."""
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return [
            dt.strftime("%d%m"),
            dt.strftime("%m%d"),
            dt.strftime("%d%m%y"),
            dt.strftime("%d%m%Y")
        ]
    except ValueError:
        return []

def check_mpin_strength(mpin, dob_self, dob_spouse, anniversary):
    """Analyze MPIN strength based on common patterns."""
    reasons = []
    
    # Get pattern combinations
    self_patterns = get_date_patterns(dob_self)
    spouse_patterns = get_date_patterns(dob_spouse)
    anniv_patterns = get_date_patterns(anniversary)

    # Check for weaknesses
    if mpin in common_mpins:
        reasons.append("COMMONLY_USED")
    if mpin in self_patterns:
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if mpin in spouse_patterns:
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if mpin in anniv_patterns:
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")
    strength = "WEAK" if reasons else "STRONG"
    return strength, reasons
#tUser Input 
print("MPIN STRENGTH CHECKER ")
mpin = input("Enter a 4 or 6-digit MPIN: ").strip()
dob_self = input("Enter your DOB (YYYY-MM-DD): ").strip()
dob_spouse = input("Enter Spouse DOB (YYYY-MM-DD): ").strip()
anniversary = input("Enter Anniversary Date (YYYY-MM-DD): ").strip()

# Result Evaluation 
strength, reasons = check_mpin_strength(mpin, dob_self, dob_spouse, anniversary)

# Output 
print("\n RESULT")
print(f"MPIN: {mpin}")
print(f"Strength: {strength}")
print(f"Weakness Reasons: {reasons if reasons else 'None'}")
%history -f mpin_checker_user_input.py
