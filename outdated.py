months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)
            else:
                m_name, d, y = date.split(" ", 2)
                if not d.endswith(","):
                    raise ValueError
                d = d.rstrip(",")
                m = months.index(m_name) + 1
                d, y = int(d), int(y)

            if m < 1 or m > 12 or d < 1 or d > 31:
                raise ValueError

            print(f"{y:04}-{m:02}-{d:02}")
            break

        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
