from analyze_password import analyze_password


def run_password_check():
    print("\n--- Перевірка безпеки паролів ---")
    
    print("\nБудь ласка, введіть ваші дані для аналізу:")
    name = input("Ваше ім'я (латиницею): ")
    last_name = input("Ваше прізвище (латиницею): ")
    dob_day = input("День народження (наприклад, 09): ")
    dob_month = input("Місяць народження (наприклад, 02): ")
    dob_year = input("Рік народження (наприклад, 2005): ")

    personal_data = {
        'first_name': name,
        'last_name': last_name,
        'birth_date': {
            'day': dob_day,
            'month': dob_month,
            'year': dob_year
        }
    }
    
    password = input("\nВведіть пароль для перевірки: ")
    
    analysis_result = analyze_password(password, personal_data)
    
    print("\n--- Результати аналізу ---")
    
    print(f"\nОцінка безпеки: {analysis_result['score']}/10")
    
    print("\nДеталі аналізу:")
    for item in analysis_result['feedback']:
        print(item)
    
    print("\nРекомендації для покращення:")
    if analysis_result['recommendations']:
        for item in analysis_result['recommendations']:
            print(item)
    else:
        print("Чудово! Немає конкретних рекомендацій")