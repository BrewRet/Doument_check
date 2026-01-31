import pytest

from app.services import verify

payload_true = ("22.08.1977", 
                "0525 185673", 
                "PNRUS<<IVANOV<<IVAN<<IVANOVICH<<<<<<<<<<<<<<\n0521856730RUS7708220M4510220<<<<<<<<<<<<<<44")
payload_false_date = ("22.08.1978", 
                "0525 185673", 
                "PNRUS<<IVANOV<<IVAN<<IVANOVICH<<<<<<<<<<<<<<\n0521856730RUS7708220M4510220<<<<<<<<<<<<<<44")

payload_false_doc = ("22.08.1977", 
                "0525 185633", 
                "PNRUS<<IVANOV<<IVAN<<IVANOVICH<<<<<<<<<<<<<<\n0521856730RUS7708220M4510220<<<<<<<<<<<<<<44")


def test_verify_true():
    assert verify(payload_true[0], payload_true[1], payload_true[2]) == 1


def test_verify_false_date():
    assert verify(payload_false_date[0], payload_false_date[1], payload_false_date[2]) == 0


def test_verify_false_doc():
    assert verify(payload_false_doc[0], payload_false_doc[1], payload_false_doc[2]) == 0