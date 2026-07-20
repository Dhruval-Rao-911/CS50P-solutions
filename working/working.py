import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    start = format_time(h1, m1, p1)
    end = format_time(h2, m2, p2)

    return f"{start} to {end}"


def format_time(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if hour < 1 or hour > 12 or minute > 59:
        raise ValueError("Invalid time")

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
