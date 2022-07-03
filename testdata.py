import pandas
from faker import Faker

fake = Faker('de_DE')

data_list = []

for num in range(200):
    data_list.append({
        'Name': fake.last_name(),
        'Vorname': fake.first_name(),
        'Telefon': fake.phone_number(),
        'Strasse': fake.street_address(),
        'Postleitzahl': fake.postcode(),
        'Stadt': fake.building_number(),
        'Bank': fake.iban(),
        'Eintritt': fake.date_between().strftime('%d.%m.%Y')
    })
pandas.options.display.max_columns = None
df = pandas.DataFrame(data_list)

df.to_excel('testdata.xlsx')
