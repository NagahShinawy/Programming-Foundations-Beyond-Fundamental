"""
created by Nagaj at 18/06/2021
"""
countries = [
    "Egypt",
    "Morocco",
    "Tunis",
    "USA",
    "Germany",
    "Egypt",
    "England"
]

for country in enumerate(countries, start=1):
    print(country)

print(countries.count("Egypt"))


def starts_with_e(cntry: str):
    if cntry.startswith("E"):
        return cntry


print("#" * 100)

e_countries = filter(starts_with_e, countries)
m_countries = filter(lambda cntry: cntry.startswith("M"), countries)
for e_country in e_countries:
    print(e_country)

print(list(m_countries))
print(countries)
print(countries.pop())
print(countries)
