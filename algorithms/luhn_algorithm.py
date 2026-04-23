def verify_card_number(card_number: str):
    card_number = card_number.replace(" ", "").replace("-", "")
    print(f'Card number: {card_number}')

    digits = [int(digit) for digit in card_number[::-1]]

    for i in range(len(digits)):
        if i % 2 == 1:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total_sum = sum(digits)

    if total_sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'
    


if __name__ == '__main__':
    print(verify_card_number('453914889'))

    print(verify_card_number('4111-1111-1111-1111'))

    print(verify_card_number('453914881'))

    print(verify_card_number('1234 5678 9012 3456'))
