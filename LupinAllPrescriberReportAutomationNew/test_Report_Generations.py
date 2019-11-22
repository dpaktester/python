import Lupin_general_validations

def test_check_Regions():
    region=Lupin_general_validations.CheckRegions_For_Report()
    assert region ==0

def test_Channels_SupraxTRX():
    channel=Lupin_general_validations.Channels_Suprax_TRX()
    assert channel==0
def test_Channels_WomensHealthCareTQTY():
    Channel2=Lupin_general_validations.Channels_WomensHealthCare_TQTY()
    assert Channel2==0

def test_Drugs_SupraxTRX():
    Drugs1 = Lupin_general_validations.Drugs_Suprax_TRX()
    assert Drugs1 ==0

def test_Drugs_WomensHealthCareTQTY():
    Drugs2 = Lupin_general_validations.Drugs_WomensHealthCare_TQTY()
    assert Drugs2 ==0

def test_CompareMatty_SupraxCap_TabManagedMedicaid():
    compareSupraxCapTabMM = Lupin_general_validations.CompareMattySupraxCapTabManagedMedicaid()
    assert compareSupraxCapTabMM ==0
def test_RAWDBMatty_SupraxCapTab_commercialwithoutManagedMedicaid():
    compareSupraxCapTabCoMM=Lupin_general_validations.CompareMattySupraxCapTabcommercialwoManagedMedicaid()
    assert compareSupraxCapTabCoMM==0
   ## print(Lupin_general_validations.Report_Matty())
def test_Compare_RAWDBMatty_WomensHealthcare_ManagedMedicaid():
    compare_WomensHealthcare_ManagedMedicaid=Lupin_general_validations.CompareRAWDBMattyWomensHealthcareManagedMedicaid()
    assert compare_WomensHealthcare_ManagedMedicaid==0

def test_Compare_RAWDBMatty_WomensHealthcare_Commercial_withoutManagedMedicaid():
    compare_WomensHealthcare_commwithout_ManagedMedicaid=Lupin_general_validations.CompareRAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid()
    assert compare_WomensHealthcare_commwithout_ManagedMedicaid==0