def create_phone_number(n):
    phone_number = "".join(map(str, n))
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"