from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add shirt image
    pdf.image("shirtificate.png", x=10, y=30, w=190)

    # Add name text on top of shirt
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 110)
    pdf.cell(w=210, h=10, text=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
