from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    input_str = input("Введите данные карты или счёта: ")
    print(mask_account_card(input_str))

    input_str = input("Введите дату в формате 'YYYY-MM-DDTHH:MM:SS.SSSSSS': ")
    print(get_date(input_str))