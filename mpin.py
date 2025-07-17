import pandas as pd
import random
from datetime import datetime, timedelta
# Load the CSV file
file_path = "mpin_test_dataset.csv"
df = pd.read_csv(file_path)
# Sample names, cities, genders for variety
names = ["Anjali", "Rohit", "Vikas", "Simran", "Neha", "Karan", "Tina", "Aman", "Preeti", "Manish"]
cities = ["Mumbai", "Delhi", "Lucknow", "Chennai", "Kolkata", "Bengaluru"]
genders = ["Male", "Female", "Other"]
# Common weak MPINs (4 and 6 digits)
common_mpins = ["1234", "1111", "0000", "1212", "7777", "1004", "2000", "6969", "2222", "9999",
                "123456", "000000", "111111", "121212", "654321", "999999" ]
#Function to generate a random date in YYYY-MM-DD format
def generate_random_date(start_year=1960, end_year=2022):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
# Generate 20 new rows
new_data = []

for i in range(20):
    dob_self = generate_random_date(1970, 2005)
    dob_spouse = generate_random_date(1970, 2005)
    anniversary = generate_random_date(1990, 2024)

    name = random.choice(names)
    gender = random.choice(genders)
    location = random.choice(cities)
# format DOBs for MPIN checking
dob_self_ddmmyy = datetime.strptime(dob_self, "%Y-%m-%d").strftime("%d%m%y")
dob_spouse_ddmmyy = datetime.strptime(dob_spouse, "%Y-%m-%d").strftime("%d%m%y")
anniversary_ddmmyy = datetime.strptime(anniversary, "%Y-%m-%d").strftime("%d%m%y")

dob_self_ddmm = dob_self_ddmmyy[:4]
dob_spouse_ddmm = dob_spouse_ddmmyy[:4]
anniversary_ddmm = anniversary_ddmmyy[:4]
# Choose MPIN length (4 or 6)
mpin_length = random.choice([4, 6])
# Decide MPIN type
is_weak = random.choice([True, False])
if is_weak:
    mpin = random.choice(common_mpins + [dob_self_ddmm, dob_spouse_ddmm, anniversary_ddmm])
else:
    while True:
        mpin_length = random.choice([4, 6])  # Randomly choose 4 or 6-digit
        mpin = ''.join(random.choices("0123456789", k=mpin_length))
        if mpin not in common_mpins and mpin not in [dob_self_ddmm, dob_self_ddmmyy,
                                                 dob_spouse_ddmm, dob_spouse_ddmmyy,
                                                 anniversary_ddmm, anniversary_ddmmyy]:
            break
# Determine weakness reasons
reasons = []
if mpin in [dob_self_ddmm, dob_self_ddmmyy]:
    reasons.append("DEMOGRAPHIC_DOB_SELF")
if mpin in common_mpins:
    reasons.append("COMMONLY_USED")
if mpin == dob_self_ddmm:
    reasons.append("DEMOGRAPHIC_DOB_SELF")
if mpin == dob_spouse_ddmm:
    reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
if mpin == anniversary_ddmm:
    reasons.append("DEMOGRAPHIC_ANNIVERSARY")
    
    final_strength = "WEAK" if reasons else "STRONG"

    new_data.append({
        "mpin": mpin,
        "mpin_length": len(mpin),
        "dob_self": dob_self,
        "dob_spouse": dob_spouse,
        "anniversary": anniversary,
        "expected_strength": final_strength,
        "expected_reasons": ";".join(reasons)
    })
# Append to existing data
df_new = pd.DataFrame(new_data)
df = pd.concat([df, df_new], ignore_index=True)
# Save back to CSV
df.to_csv(file_path, index=False)
print("Successfully appended 20+ random records.")
%history -f mpin.py
