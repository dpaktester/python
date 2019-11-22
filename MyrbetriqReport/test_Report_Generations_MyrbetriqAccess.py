import MyrbteriqAccessReport

def test_Myrbetriq_Status():
    Myrbetriq_Access=MyrbteriqAccessReport.Compare_Myrverify_total_Myrbetriqbetriq_Report()
    assert Myrbetriq_Access==0


def test_Vesicare_Status( ):
    Vesicare_Access=MyrbteriqAccessReport.Compare_Vesicare_Report()
    assert Vesicare_Access==0


def test__0__for__NationalID__In__Details_Tab():
    ZeroID=MyrbteriqAccessReport.Check_0_ID__in_National_Entity_ID()
    assert ZeroID==0

def test_alphabetical_charecters_in_all_numericfileds():
    numericfields=MyrbteriqAccessReport.Check_alphabets_in_NumericFields()
    assert numericfields==0

def test__Check_AstellasChannel():
    verifyChannel=MyrbteriqAccessReport.Check_AstellasChannel()
    assert verifyChannel==0

def test__Check_AstellasSubChannel__Asper__Channels():
    verifySubChannel=MyrbteriqAccessReport.Check_Astellas_Sub_Channel()
    assert verifySubChannel==0

def test__Check_Blank_Regional_ID_anyletters():
    verifyBlankRegionalId=MyrbteriqAccessReport.Check_Blank_ID__in_Regional_Entity_ID()
    assert verifyBlankRegionalId==0

