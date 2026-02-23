import pdfplumber 

pdf = pdfplumber.open("report.pdf")

pages = pdf.pages

financial_data = {}

for page in pages:
    tables = page.extract_tables()

    for table in tables:

        for row in table:

            if row and len(row) >= 2:
                label = row[0]
                value = row[1]
                
                if label and value:
                    clean_value = value.replace("," , "").strip()
                    financial_data[label.lower()] = (clean_value)


print(financial_data)