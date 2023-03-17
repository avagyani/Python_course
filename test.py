#year_of_born = 1988
#age = 2023 - year_of_born 
#result = ((age >= 20 and age <= 30) * "vayelir") or ((age > 30 and age <= 40) * "ush e")
#print(result)



birth_year = int(input("Please enter your birth year > "))

age_by_years = 2023 - birth_year

leap_years = (birth_year % 4 == 0) + age_by_years // 4

age_by_days = age_by_years * 365 + leap_years

print(age_by_days)