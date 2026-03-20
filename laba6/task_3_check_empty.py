def check_empty(text):
    text = "".join(text.split())
    text = text.replace("ㅤ", "")
    return True if text else False
