import re

def analyze_password(password, personal_data):
    score = 10
    feedback = []

    personal_data_found = False

    for key in ['first_name', 'last_name']:
        value = personal_data.get(key, "")
        if value and value.lower() in password.lower():
            score -= 4
            feedback.append(f"Пароль містить ваші персональні дані: '{value}'")
            personal_data_found = True

    birth = personal_data.get("birth_date", {})
    day = str(birth.get("day", "")).zfill(2)
    month = str(birth.get("month", "")).zfill(2)
    year = str(birth.get("year", ""))

    date_matches = set()

    if day and day in password:
        date_matches.add(day)
    if month and month in password:
        date_matches.add(month)
    if year and year in password:
        date_matches.add(year)

    long_patterns = [
        day + month + year,
        month + day + year,
        year + month + day,
        year + day + month
    ]
    for pattern in long_patterns:
        if pattern and pattern in password:
            date_matches.add(pattern)

    if date_matches:
        score -= 3
        feedback.append(f"Пароль містить вашу дату народження або її частини: {', '.join(date_matches)}")
        personal_data_found = True

    if not personal_data_found:
        feedback.append("У паролі не виявлено особистих даних")

    min_length = 8
    if len(password) < min_length:
        score -= 2
        feedback.append(f"Пароль занадто короткий. Мінімум {min_length} символів")
    else:
        feedback.append("Довжина пароля достатня")

    has_lowercase = re.search('[a-z]', password)
    has_uppercase = re.search('[A-Z]', password)
    has_digit = re.search('[0-9]', password)
    has_special = re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?`~]', password)

    char_types = sum([bool(has_lowercase), bool(has_uppercase), bool(has_digit), bool(has_special)])
    if char_types < 3:
        score -= 2
        feedback.append("Пароль не містить достатньої різноманітності символів")
    else:
        feedback.append("Пароль містить різноманітні символи")

    common_words = ['password', '123456', 'user', '11111111']
    if password.lower() in common_words:
        score -= 5
        feedback.append("Пароль є занадто поширеним")

    final_score = max(1, min(10, score))

    recommendations = []
    if final_score < 7:
        if not has_lowercase or not has_uppercase:
            recommendations.append("-- Використовуйте великі та малі літери")
        if not has_digit:
            recommendations.append("-- Додайте цифри")
        if not has_special:
            recommendations.append("-- Додайте спеціальні символи (!@#$ тощо)")
        if personal_data_found:
            recommendations.append("-- Уникайте використання особистих даних (ім'я, прізвище, дата народження)")
        if len(password) < min_length:
            recommendations.append("-- Збільшіть довжину пароля")

    if not recommendations and final_score >= 7:
        recommendations.append("Пароль достатньо надійний")

    return {
        'score': final_score,
        'feedback': feedback,
        'recommendations': recommendations
    }
