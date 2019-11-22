import Automate_Lupin_iPadRx_Report

def test_NationalAggregate__Agaisnt__Prescriber__Plan__Level():
    Matty_Comparison=Automate_Lupin_iPadRx_Report.verify__NationalAggregate()
    assert Matty_Comparison==0



def test_Channel_in_Natioanl_Aggregate():
    Chhanelsin_Natioanl_Aggregate=Automate_Lupin_iPadRx_Report.Verify_Channel_in_NationalAggregate()
    assert Chhanelsin_Natioanl_Aggregate==0

def test_Drugs_in_Natioanl_Aggregate():
    Drugs_in_Natioanl_Aggregate=Automate_Lupin_iPadRx_Report.Verify_Drugs_in_NationalAggregate()
    assert Drugs_in_Natioanl_Aggregate==0

def test_Channel_in_Prescriber_Plan_Level():
    Chhanelsin_Prescriber_Plan_Level=Automate_Lupin_iPadRx_Report.Verify_Channel_in__Prescriber_Plan_Level_Sheet()
    assert Chhanelsin_Prescriber_Plan_Level==0


def test_Drugs_in_Prescriber_Plan_Level():
    Drugs_in_Prescriber_Plan_Level=Automate_Lupin_iPadRx_Report.Verify_Drugs_in_Prescriber_Plan_Level_Sheet()
    assert Drugs_in_Prescriber_Plan_Level==0

def test_RawDB_Matty_Against_iPAD_DB_Matty_Prescriber_Plan_Level():
    Difference_Between_ipad_And_RawDB_Matty_in_Prescriber_Plan_Level=Automate_Lupin_iPadRx_Report.Verify_RawDB_Matty_Agaisnt_IpadDB_Matty_in_Prescriber_Plan_Level_Sheet()
    assert Difference_Between_ipad_And_RawDB_Matty_in_Prescriber_Plan_Level==0

def test_Check_Blank_Rows_in_EntityName_Field_Prescriber_Plan_Level():
    Blank_Rows_in_Entity_Name_Field_in_Prescriber_Plan_Level=Automate_Lupin_iPadRx_Report.Verify_BlankEntity__in_Prescriber_Plan_Level_Sheet()
    assert Blank_Rows_in_Entity_Name_Field_in_Prescriber_Plan_Level==0

def test_Check_Blank_Rows_in_PrescriberID_Field_in_Prescriber_Plan_Level():
    Blank_Rows_in_PrescriberID_Field_in_Prescriber_Plan_Level=Automate_Lupin_iPadRx_Report.Verify_Blank_Precriber_in_Prescriber_Plan_Level_Sheet()
    assert Blank_Rows_in_PrescriberID_Field_in_Prescriber_Plan_Level==0

def test_Antara_In_National_Aggregate_Sheet_Staticinfo():
   Antara_in_National_Aggregate_Sheet_Staticinfo=Automate_Lupin_iPadRx_Report.verify__Antara_in_NationalAggregate_Sheet()
   assert Antara_in_National_Aggregate_Sheet_Staticinfo==0

def test_Antara_In_Prescriber_Plan_Level_Sheet_Staticinfo():
    Antara_in_Prescriber_Plan_Level_Sheet_Staticinfo=Automate_Lupin_iPadRx_Report.verify__Antara_in_Prescriber_Plan_Level_sheet()
    assert Antara_in_Prescriber_Plan_Level_Sheet_Staticinfo==0




def test_Difference__in__Bothin__Pad__and__RawDb():
    Compare_RAWDB_iPadRxDB=Automate_Lupin_iPadRx_Report.DifferenceofMattyinRawDbandIpadDB()
    assert Compare_RAWDB_iPadRxDB==0