dog_years_alive = int(input("Enter dog's years of life: "))

if dog_years_alive <= 2:
    dog_years_age = dog_years_alive * 12
else:
    dog_years_age = ((dog_years_alive - 2) * 6) + 24

print("Human age ", dog_years_age)
