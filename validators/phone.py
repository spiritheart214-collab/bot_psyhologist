"""Валидатор ввода телефона"""
import phonenumbers


def _check_phone(phone: str) -> bool:
    """

    :param phone:  Номер телефона пользователя
    :return: True/False в зависимости от полученных данных
    :exept: NumberParseException - ошибка не корректного ввода (например введен тект), пустую строку и тд.
    """
    try:
        number = phonenumbers.parse(phone, "RU")
    except phonenumbers.NumberParseException:
        return False

    if not phonenumbers.is_valid_number(number):
        return False
    else:
        return True


def validate_phone(phone: str) -> str | None:
    """
    Проверяет номер телефона и возвращает его в формате E.164.

    :param phone: Номер телефона пользователя
    :return: None в случае ошибки и отформатированный номер в виде строки в случае успе[а
    """

    is_correct = _check_phone(phone=phone)

    if is_correct:
        number = phonenumbers.parse(phone, "RU")
        phone_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
        return phone_number

    else:
        return None


if __name__ == '__main__':
    print(validate_phone(phone="8 (903) 123 - 45 - 67"))
