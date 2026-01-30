def verify(date_of_birth: str, doc_number: str, mrz: str) -> int:
    second_row = mrz.split("\n")[1]
    doc_number_mrz = second_row[:9]
    date_of_birth_mrz = second_row[13:19]
    day, month, year = date_of_birth.split(".")
    date_of_birth =  year[2:] + month + day
    doc_number = doc_number[:3] + doc_number[5:]

    if (doc_number == doc_number_mrz
        and
        date_of_birth == date_of_birth_mrz):
        return 1
    return 0

