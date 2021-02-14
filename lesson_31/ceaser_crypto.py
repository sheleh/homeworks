def encrypt(text, s):
    text = str(text)
    s = int(s)
    result = ''
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase ch in text
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase ch in text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(text, s):
    text = str(text)
    s = int(s)
    result = ''
    for i in range(len(text)):
        char = text[i]
        # Decrypt uppercase ch in text
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Decrypt lowercase ch in text
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

if __name__ == '__main__':
    print(encrypt('Hello Mars', 5))
    print(decrypt('MjqqtsRfwx',5))