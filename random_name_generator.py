from faker import Faker

# Create an instance of the Faker class
def random_name(gender):
    fake = Faker('en')

    # Generate a random Canadian name
    if gender == 'male':
        random_name = fake.name_male()
    elif gender == 'female':
        random_name = fake.name_female()
    else:
        random_name = fake.name()

    split_name = random_name.split()

    # Extract the first name and last name
    first_name = split_name[0]
    last_name = split_name[1]
    return first_name, last_name

# print(random_name('female'))