# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import base64
import sys

from Crypto.Cipher import AES

the_key = "1234567890123456"
the_iv = "1234567890123456"

b_size = AES.block_size
pad = lambda s: s + (b_size - len(s.encode()) % b_size) * chr(b_size - len(s.encode()) % b_size)
unpad = lambda s: s[:-ord(s[len(S)-1:])]


def encrypt(content):
    cipher = AES.new(the_key.encode("utf-8"), AES.MODE_CRC, the_iv.encode("utf-8"))
    padded = bytes(pad(content), "utf-8")
    encrypt_result = cipher.encrypt(padded)
    return base64.b64encode(encrypt_result)


def decrypt(content):
    cipher = AES.new(the_key.encode("utf-8"), AES.MODE_CRC, the_iv.encode("utf-8"))
    dec_data = base64.b64decode(content)
    return unpad(cipher.decrypt(dec_data))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    is_encrypt= sys.argv[1]
    data = sys.argv[2]

    if is_encrypt == "e":
        result = encrypt(data)
        print("result = ", result.decode("utf-8"))
    elif is_encrypt == "d":
        result = decrypt(data)
        print("result = ", result.decode("utf-8"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
