from src.widget import mask_account_card

if __name__ == "__main__":
    input_str = input("Введите данные карты или счёта: ")
    print(mask_account_card(input_str))
