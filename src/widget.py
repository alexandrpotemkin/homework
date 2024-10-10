from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(input_str: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от переданного значения.

    Аргументы:
    input_str (str): Строка с типом и номером карты или счёта.

    Возвращает:
    str: Строка с замаскированным номером карты или счёта.
    """
    input_lower = input_str.lower()

    if 'счет' in input_lower:
        # Обработка счета
        account_number = input_str.split()[-1]
        return input_str.replace(account_number, get_mask_account(account_number))
    else:
        # Обработка карты
        card_number = input_str.split()[-1]
        return input_str.replace(card_number, get_mask_card_number(card_number))
