def user_info(name, surname, birth_year, city, email, phone_number):
    print(name, surname, birth_year, city, email, phone_number)


user_info(name=input('Name: '), surname=input('Surname: '), birth_year=input('Birth year: '), city=input('City: '),
          email=input('Email: '), phone_number=input('Phone number: '))
