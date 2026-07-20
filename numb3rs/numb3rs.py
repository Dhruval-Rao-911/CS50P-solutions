import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.fullmatch(pattern, ip)
    if match:
        for i in range(1, 5):
            num = match.group(i)
            if int(num) > 255:
                return False
            if len(num) > 1 and num[0] == "0":
                return False
        return True
    return False


if __name__ == "__main__":
    main()
