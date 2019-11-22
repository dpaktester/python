import LupinDataValidation

def test_DiffernecOfMattyBetweenQVandLITE():
    DiffernceofMatty=LupinDataValidation.CheckQVandLiteMatty()
    assert DiffernceofMatty==0

def test_QVandRAWDB():
    QVandRawDBDiffenreceofMatty=LupinDataValidation.Comparison()
    assert QVandRawDBDiffenreceofMatty==0

def test_Prescriber_Matty():
    DiffernceOfPrescriberMatty=LupinDataValidation.PrecriberMatty()
    assert DiffernceOfPrescriberMatty==0