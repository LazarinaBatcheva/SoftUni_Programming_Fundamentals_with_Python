def header_function():
    return "CASH RECEIPT\n------------------------------"


def body_function():
    return "Charged to____________________\nReceived by___________________"


def text_footer():
    return "------------------------------\n\u00A9 SoftUni"


def base_function():
    print(header_function())
    print(body_function())
    print(text_footer())


base_function()