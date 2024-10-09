from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    card_number = "2024 5555 7862 4983"
    print(get_mask_card_number(card_number))

    account_number = "57546868641646"
    print(get_mask_account(account_number))
