import pyodbc

defaultchannels = ['Commercial w/o Managed Medicaid', 'Managed Medicaid']
cnxnto15Db = pyodbc.connect(
    'DRIVER={SQL Server Native Client 10.0};SERVER=10.0.0.15;PORT=1433;DATABASE=Reports_DB;UID=m1bqc;PWD=m1b0813')
cnxnto36Db = pyodbc.connect(
    'DRIVER={SQL Server Native Client 10.0};SERVER=10.0.0.36;PORT=1433;DATABASE=M1B_LupRx;UID=m1bqc;PWD=m1bqc@0813')

cursor = cnxnto15Db.cursor()
cursorOn36Db=cnxnto36Db.cursor()
Suprax_TRX_drugs=['cefdinir','Suprax']
WomensHealthCare_TQTY_drugs=['Cleocin Vaginal','Cleocin Vaginal Ovules','clindamycin phosphate vaginal cream','Clindesse','Flagyl','Metrogel-Vaginal','metronidazole','metronidazole vaginal',
'Nuvessa','Solosec','Tindamax','tinidazole']


ReportOutput=[]
RAWDbOutputSupraxCapTabManagedMedicaid=[]
RAWDbOutputSupraxCapTabcommercialwithoutManagedMedicaid=[]
RAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid=[]
RAWDBMattyWomensHealthcare_Managed_Medicaid=[]


####  Checking Channel for Suprax _TRX  ######

def Channels_Suprax_TRX():
    Channels_Suprax_TRX_query = "Select DISTINCT CHANNEL [Suprax_TRX] FROM LupinAllPrescribersReportData Where REPORT_NO =3"

    Channels_Suprax_TRX_query_output = cursor.execute(Channels_Suprax_TRX_query)
    Suprax_TRX_ReportChannel = Channels_Suprax_TRX_query_output.fetchall()
    Suprax_TRX_ReportChannel_list1 = []

    #print(ReportChannel)
    for i in range(list(Suprax_TRX_ReportChannel).__len__()):
        Suprax_TRX_ReportChannel_list1.append(tuple(Suprax_TRX_ReportChannel[i]).__getitem__(0))
        Missing_Channels_IN_Suprax_TRX = set(Suprax_TRX_ReportChannel_list1) - set(defaultchannels)
    ##print(res)
    if(Missing_Channels_IN_Suprax_TRX.__len__())==0:
        print("The Channel is matching aganist The Requiement")
    else:
        print("The Channel is not matching against The Reqirement")

    return Missing_Channels_IN_Suprax_TRX.__len__()


####  Checking Channel for WomensHealthCare_TQTY  ######

def Channels_WomensHealthCare_TQTY():
    Channels_WomensHealthCare_TQTY_query1 = "Select DISTINCT CHANNEL [Antara NRX] FROM LupinAllPrescribersReportData Where REPORT_NO =4"

    Channels_WomensHealthCare_TQTY_output1 = cursor.execute(Channels_WomensHealthCare_TQTY_query1)
    WomensHealthCare_TQTY_ReportChannel = Channels_WomensHealthCare_TQTY_output1.fetchall()
    WomensHealthCare_TQTY_list1 = []

    # print(ReportChannel)
    for i in range(list(WomensHealthCare_TQTY_ReportChannel).__len__()):
        WomensHealthCare_TQTY_list1.append(tuple(WomensHealthCare_TQTY_ReportChannel[i]).__getitem__(0))
    Missing_Chhanels_InWomensHealthCare_TQTY = set(WomensHealthCare_TQTY_list1) - set(defaultchannels)
    ##print(Missing_Chhanels_InWomensHealthCare_TQTY)
    if(Missing_Chhanels_InWomensHealthCare_TQTY.__len__())==0:
        print("The Channel is matching aganist The Requiement")
    else:
        print("The Channel is not matching against The Reqirement")


    return Missing_Chhanels_InWomensHealthCare_TQTY.__len__()


####  Checking Drugs for Suprax_TRX  ######

def Drugs_Suprax_TRX():

    query3 = "Select DISTINCT [Drug Name] [Suprax TRX] FROM LupinAllPrescribersReportData Where REPORT_NO =3"

    output3 = cursor.execute(query3)
    ReportDrugs = output3.fetchall()
    list1 = []

    # print(ReportChannel)
    for i in range(list(ReportDrugs).__len__()):
        list1.append(tuple(ReportDrugs[i]).__getitem__(0))
    res = set(list1) - set(Suprax_TRX_drugs)
    print(res)
    return res.__len__()

####  Checking Drugs for WomensHealthCare_TQTY  ######

def Drugs_WomensHealthCare_TQTY():

    query4 = "Select DISTINCT [Drug Name] [Suprax TRX] FROM LupinAllPrescribersReportData Where REPORT_NO =4"

    output4 = cursor.execute(query4)
    ReportDrugs1 = output4.fetchall()
    list1 = []

    # print(ReportChannel)
    for i in range(list(ReportDrugs1).__len__()):
        list1.append(tuple(ReportDrugs1[i]).__getitem__(0))
    res = set(list1) - set(WomensHealthCare_TQTY_drugs)
    print(res)
    return res.__len__()

###     Getting The Report Matty and saving it into a Variable "ReportMatty"    ###

def Report_Matty():

    query5 =    """     SELECT Channel,[Drug Name],[Prescriber Name],[Prescriber ME #],Region,Report_NO,
				CASE 
					WHEN REPORT_NO=1 THEN 'Antara Market TRX'
					WHEN REPORT_No=2 THEN 'Antara Market NRX'
					WHEN REPORT_No=3 THEN 'Suprax Chew MAREKT TRX'
					WHEN REPORT_No=4 THEN 'Womens Health Care Market TQTY' END AS MARKET ,sum(Matty) Matty
                        into #tmp FROM LupinAllPrescribersReportData

                        group by Channel,Report_No,[Drug Name],[Prescriber Name],[Prescriber ME #],Region,Report_NO
                        order by sum(Matty) desc 
                """

    output5 = cursor.execute(query5)
    ##tempReportMatty = output5.fetchall()

    query6= """         SELECT MARKET,Channel,Region,SUM(MATTY) AS Matty FROM #tmp WHERE MARKET IN ('Suprax Chew MAREKT TRX','Womens Health Care Market TQTY')
                        GROUP BY Region,Channel,MARKET
                        ORDER BY MARKET,Region,Channel 
            """


    output6 = cursor.execute(query6)
    ReportMatty = output6.fetchall()
    print("-------------------Report OutPut-----------------")
    for each in range(list(ReportMatty).__len__()):
        ##print("Report Matty is :---------",ReportMatty)

        ##ReportOutput.append(ReportMatty[each][0]+"|"+str(ReportMatty[each][1])+"|"+str(ReportMatty[each][2])+"|"+str(round(ReportMatty[each][3],2)))
        ReportOutput.append(ReportMatty[each][0] + "|" + ReportMatty[each][1] + "|" + str(ReportMatty[each][2]) + "|" + str(ReportMatty[each][3]))
        print(ReportOutput)



###     Getting The  Matty of Suprax Cap  Tab TRX for Managed medicaid Cahhenl   ###

def RAWDBMattySupraxCapTabManagedMedicaid():

        global RAWDbOutputSupraxCapTabManagedMedicaid

        rawDbQuery1= """    Select regionid,BUID,ME_NO,SRA2 IMSDR_Key,F_NM,L_NM,c.drug_name DrugName,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End as PDRP,
                            SUM(TRX1+TRX2+TRX3+TRX4+TRX5+TRX6+TRX7+TRX8+TRX9+TRX10+TRX11+TRX12) Matty 
                            into #MMRX_Thera_Name1 from EXT_RAW_DATA A  
                            INNER JOIN DI_MASTER.dbo.MHC_EXT_DRUG_REL B	ON A.PROD_ID=B.EXT_DRUG_ID AND B.CLIENT_ID = 2 AND B.STATUS='A' 
	                        Inner join [B1-124].M1B_DF.DBO.MASTER_THERA_Class H ON B.THERA_ID=H.THERA_ID AND Thera_Name='Antibiotics Market Suprax Cap/Tab'--Change Thera
	                        INNER JOIN [B1-124].M1B_DF.DBO.MASTER_THERA_DRUG C ON B.DRUG_BRD_ID=C.DRUG_ID  AND C.DRUG_STRENGTH='ALL' 
	                        AND C.DRUG_NAME in ('cefdinir','Suprax')--Change Drugs as per market 
	                        INNER JOIN DI_MASTER..TMP_ENTITY_IMS_XREF D ON A.PAYER_PLAN_CD=D.PAYER_PLAN_ID 
	                        INNER JOIN [B1-124].[BOTMAster].Dbo.VWLinkageChannelXref G ON D.Channel_id=G.Subchannelid AND G.subchannel='managed Medicaid'--Change Channel
	                        LEFT JOIN DF_PDRP_LIST F ON A.SRA2=F.IMS_NUM  
	                        Inner join M1B_LUPRX.dbo.PrescriberAlignment T on A.SRA2=T.IMSID  and BUID is not null
                            Group by RegionID,BUID,ME_NO,SRA2,F_NM,L_NM,c.drug_name,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End
                     """
        rawDbOutput1=cursorOn36Db.execute(rawDbQuery1)

        rawDbQuery2=""" Select ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty into #tmp1 FROM  #MMRX_Thera_Name1
                        Where  PDRP='N'---- AND RETL_TERR_ID='Unassigned'
                         Group BY ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty
                    """
        rawDbOutput2=cursorOn36Db.execute(rawDbQuery2)

        rawDbQuery4=""" SELECT RegionID,SUM(MATTY) FROM #tmp1 GROUP BY RegionID """

        rawDbOutput4 = cursorOn36Db.execute(rawDbQuery4)
        RAWDbMatty = rawDbOutput4.fetchall()

        for each in range(list(RAWDbMatty).__len__()):
            print("-------------------RAW DB OutPut-----------------")
            RAWDbOutputSupraxCapTabManagedMedicaid.append("Suprax Chew MAREKT TRX" + "|" + "Managed Medicaid"+ "|" + RAWDbMatty[each][0] + "|" + str(RAWDbMatty[each][1]))
            print(RAWDbOutputSupraxCapTabManagedMedicaid)

###     Comparing The  Matty of Suprax Cap  Tab TRX for Managed medicaid Channel against Report Matty   ###

def CompareMattySupraxCapTabManagedMedicaid():
        global ReportOutput
        Report_Matty()
        RAWDBMattySupraxCapTabManagedMedicaid()
        count = 0
        for i in range(RAWDbOutputSupraxCapTabManagedMedicaid.__len__()):
            item = RAWDbOutputSupraxCapTabManagedMedicaid[i]
            if ReportOutput.__contains__(item):
                print("")
            else:

                count = count + 1

        return count

###     Getting  The  Matty of Suprax Cap  Tab TRX for Commercial w/o Managed medicaid Channel     ###

def RAWDBMattySupraxCapTabcommercialwithoutManagedMedicaid():
    global RAWDbOutputSupraxCapTabcommercialwithoutManagedMedicaid
    rawDbQuery2 = """    Select regionid,BUID,ME_NO,SRA2 IMSDR_Key,F_NM,L_NM,c.drug_name DrugName,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End as PDRP,
                                SUM(TRX1+TRX2+TRX3+TRX4+TRX5+TRX6+TRX7+TRX8+TRX9+TRX10+TRX11+TRX12) Matty 
                                into #MMRX_Thera_Name2 from EXT_RAW_DATA A  
                                INNER JOIN DI_MASTER.dbo.MHC_EXT_DRUG_REL B	ON A.PROD_ID=B.EXT_DRUG_ID AND B.CLIENT_ID = 2 AND B.STATUS='A' 
    	                        Inner join [B1-124].M1B_DF.DBO.MASTER_THERA_Class H ON B.THERA_ID=H.THERA_ID AND Thera_Name='Antibiotics Market Suprax Cap/Tab'--Change Thera
    	                        INNER JOIN [B1-124].M1B_DF.DBO.MASTER_THERA_DRUG C ON B.DRUG_BRD_ID=C.DRUG_ID  AND C.DRUG_STRENGTH='ALL' 
    	                        AND C.DRUG_NAME in ('cefdinir','Suprax')--Change Drugs as per market 
    	                        INNER JOIN DI_MASTER..TMP_ENTITY_IMS_XREF D ON A.PAYER_PLAN_CD=D.PAYER_PLAN_ID 
    	                        INNER JOIN [B1-124].[BOTMAster].Dbo.VWLinkageChannelXref G ON D.Channel_id=G.Subchannelid AND G.subchannel='commercial w/o managed Medicaid'--Change Channel
    	                        LEFT JOIN DF_PDRP_LIST F ON A.SRA2=F.IMS_NUM  
    	                        Inner join M1B_LUPRX.dbo.PrescriberAlignment T on A.SRA2=T.IMSID  and BUID is not null
                                Group by RegionID,BUID,ME_NO,SRA2,F_NM,L_NM,c.drug_name,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End
                         """
    rawDbOutput2 = cursorOn36Db.execute(rawDbQuery2)

    rawDbQuery3 = """ Select ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty into #tmp2 FROM  #MMRX_Thera_Name2
                            Where  PDRP='N'---- AND RETL_TERR_ID='Unassigned'
                             Group BY ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty
                        """
    rawDbOutput3 = cursorOn36Db.execute(rawDbQuery3)

    rawDbQuery5 = """ SELECT RegionID,SUM(MATTY) FROM #tmp2 GROUP BY RegionID """

    rawDbOutput5 = cursorOn36Db.execute(rawDbQuery5)
    RAWDbMatty2 = rawDbOutput5.fetchall()

    for each in range(list(RAWDbMatty2).__len__()):
        print("-------------------RAW DB OutPut-----------------")
        RAWDbOutputSupraxCapTabcommercialwithoutManagedMedicaid.append("Suprax Chew MAREKT TRX" + "|" + "commercial w/o Managed Medicaid" + "|" + RAWDbMatty2[each][0] + "|" + str(RAWDbMatty2[each][1]))
        ###RAWDbOutputSupraxCapTabManagedMedicaid.append                 ("Suprax Chew MAREKT TRX" + "|" + "Commercial w/o Managed Medicaid" + "|" + RAWDbMatty2[each][0] + "|" + str(RAWDbMatty2[each][1]))
        print(RAWDbOutputSupraxCapTabcommercialwithoutManagedMedicaid)


###     Comparing  The  Matty of Suprax Cap  Tab TRX for Commercial w/o Managed medicaid Channel against Report Matty    ###

def CompareMattySupraxCapTabcommercialwoManagedMedicaid():
        global ReportOutput
        ##Report_Matty()
        RAWDBMattySupraxCapTabcommercialwithoutManagedMedicaid()
        count1 = 0
        ##print(ReportOutput)
        for i in range(RAWDbOutputSupraxCapTabcommercialwithoutManagedMedicaid.__len__()):
            item1 = RAWDbOutputSupraxCapTabcommercialwithoutManagedMedicaid[i]
            print(" ")
            for j in range(ReportOutput.__len__()):
                ##print(ReportOutput[j])
                if (ReportOutput[j] == item1):
                    print(" ")
                    count1 = count1 + 1

        return count1


###     Getting  The  Matty of Womens' Healthcare TQTY for  Managed medicaid Channel      ###

def RAWDBMattyWomensHealthcareManagedMedicaid():
    global RAWDBMattyWomensHealthcare_Managed_Medicaid
    rawDbQuery3 = """    Select regionid,BUID,ME_NO,SRA2 IMSDR_Key,F_NM,L_NM,c.drug_name DrugName,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End as PDRP,
                         SUM(TQTY1+TQTY2+TQTY3+TQTY4+TQTY5+TQTY6+TQTY7+TQTY8+TQTY9+TQTY10+TQTY11+TQTY12) Matty 
                         into #MMRX_Thera_Name5 from EXT_RAW_DATA A  
	                     INNER JOIN DI_MASTER.dbo.MHC_EXT_DRUG_REL B	ON A.PROD_ID=B.EXT_DRUG_ID AND B.CLIENT_ID = 2 AND B.STATUS='A' 
	                     Inner join [B1-124].M1B_DF.DBO.MASTER_THERA_Class H ON B.THERA_ID=H.THERA_ID AND Thera_Name='Bacterial Vaginosis'--Change Thera
	                     INNER JOIN [B1-124].M1B_DF.DBO.MASTER_THERA_DRUG C ON B.DRUG_BRD_ID=C.DRUG_ID  AND C.DRUG_STRENGTH='ALL' 
	                     AND C.DRUG_NAME in  ('Cleocin Vaginal','Cleocin Vaginal Ovules','clindamycin phosphate vaginal cream','Clindesse',
                         'Flagyl','Metrogel-Vaginal','metronidazole','metronidazole vaginal','Nuvessa','Solosec','Tindamax','tinidazole')--Change Drugs as per market 
	                     INNER JOIN DI_MASTER..TMP_ENTITY_IMS_XREF D ON A.PAYER_PLAN_CD=D.PAYER_PLAN_ID 
	                     INNER JOIN [B1-124].[BOTMAster].Dbo.VWLinkageChannelXref G ON D.Channel_id=G.Subchannelid AND G.subchannel='managed Medicaid'--Change Channel
	                     LEFT JOIN DF_PDRP_LIST F ON A.SRA2=F.IMS_NUM  
	                     Inner join M1B_LUPRX.dbo.PrescriberAlignment T on A.SRA2=T.IMSID  and BUID is not null
                         Group by RegionID,BUID,ME_NO,SRA2,F_NM,L_NM,c.drug_name,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End
                 """
    rawDbOutput3 = cursorOn36Db.execute(rawDbQuery3)

    rawDbQuery4 = """   Select ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty
                        into #tmp3 FROM  #MMRX_Thera_Name5 
                        Where  PDRP='N'---- AND RETL_TERR_ID='Unassigned'
                        Group BY ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty
                  """
    rawDbOutput4 = cursorOn36Db.execute(rawDbQuery4)

    rawDbQuery6 = """ SELECT RegionID,SUM(MATTY) FROM #tmp3 GROUP BY RegionID """

    rawDbOutput5 = cursorOn36Db.execute(rawDbQuery6)
    RAWDbMatty3 = rawDbOutput5.fetchall()

    for each in range(list(RAWDbMatty3).__len__()):
        print("-------------------RAW DB OutPut-----------------")
       ## RAWDBMattyWomensHealthcareManagedMedicaid.append("Womens Health Care Market TQTY" + "|" + "Managed Medicaid" + "|" + RAWDbMatty3[each][0] + "|" + str(RAWDbMatty3[each][1]))
        RAWDBMattyWomensHealthcare_Managed_Medicaid.append("Womens Health Care Market TQTY" + "|" + "Managed Medicaid" + "|" + RAWDbMatty3[each][0] + "|" + str(RAWDbMatty3[each][1]))
        ###RAWDbOutputSupraxCapTabManagedMedicaid.append                 ("Suprax Chew MAREKT TRX" + "|" + "Commercial w/o Managed Medicaid" + "|" + RAWDbMatty2[each][0] + "|" + str(RAWDbMatty2[each][1]))
        print(RAWDBMattyWomensHealthcare_Managed_Medicaid)

###     Comparing  The  Matty of Womens' Healthcare TQTY for  Managed medicaid Channel against Report Matty    ###

def CompareRAWDBMattyWomensHealthcareManagedMedicaid():
        RAWDBMattyWomensHealthcareManagedMedicaid()
        count10 = 0
        ##print(ReportOutput)
        for i in range(RAWDBMattyWomensHealthcare_Managed_Medicaid.__len__()):
            item1 = RAWDBMattyWomensHealthcare_Managed_Medicaid[i]
            print(" ")
            for j in range(ReportOutput.__len__()):
                ##print(ReportOutput[j])
                if (ReportOutput[j] == item1):
                    print(" ")
                    count4 = count10 + 1

        return count10

###     Getting  The  Matty of Womens' Healthcare TQTY for  commercial w/o Managed medicaid Channel      ###

def RAWDBMattyWomensHealthcarecommwithoutManagedMedicaid():
    global RAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid
    rawDbQuery4 = """    Select regionid,BUID,ME_NO,SRA2 IMSDR_Key,F_NM,L_NM,c.drug_name DrugName,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End as PDRP,
                         SUM(TQTY1+TQTY2+TQTY3+TQTY4+TQTY5+TQTY6+TQTY7+TQTY8+TQTY9+TQTY10+TQTY11+TQTY12) Matty 
                         into #MMRX_Thera_Name4 from EXT_RAW_DATA A  
	                     INNER JOIN DI_MASTER.dbo.MHC_EXT_DRUG_REL B	ON A.PROD_ID=B.EXT_DRUG_ID AND B.CLIENT_ID = 2 AND B.STATUS='A' 
	                     Inner join [B1-124].M1B_DF.DBO.MASTER_THERA_Class H ON B.THERA_ID=H.THERA_ID AND Thera_Name='Bacterial Vaginosis'--Change Thera
	                     INNER JOIN [B1-124].M1B_DF.DBO.MASTER_THERA_DRUG C ON B.DRUG_BRD_ID=C.DRUG_ID  AND C.DRUG_STRENGTH='ALL' 
	                     AND C.DRUG_NAME in  ('Cleocin Vaginal','Cleocin Vaginal Ovules','clindamycin phosphate vaginal cream','Clindesse',
                         'Flagyl','Metrogel-Vaginal','metronidazole','metronidazole vaginal','Nuvessa','Solosec','Tindamax','tinidazole')--Change Drugs as per market 
	                     INNER JOIN DI_MASTER..TMP_ENTITY_IMS_XREF D ON A.PAYER_PLAN_CD=D.PAYER_PLAN_ID 
	                     INNER JOIN [B1-124].[BOTMAster].Dbo.VWLinkageChannelXref G ON D.Channel_id=G.Subchannelid AND G.subchannel='commercial w/o managed Medicaid'--Change Channel
	                     LEFT JOIN DF_PDRP_LIST F ON A.SRA2=F.IMS_NUM  
	                     Inner join M1B_LUPRX.dbo.PrescriberAlignment T on A.SRA2=T.IMSID  and BUID is not null
                         Group by RegionID,BUID,ME_NO,SRA2,F_NM,L_NM,c.drug_name,Case when F.IMS_NUM IS NULL Then 'N' else 'Y' End
                 """
    rawDbOutput4 = cursorOn36Db.execute(rawDbQuery4)

    rawDbQuery5 = """ Select ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty
                        into #tmp4 FROM  #MMRX_Thera_Name4 
                        Where  PDRP='N'---- AND RETL_TERR_ID='Unassigned'
                        Group BY ME_NO,IMSDR_Key,F_NM,L_NM,DrugName,RegionID,PDRP,Matty
                  """
    rawDbOutput6 = cursorOn36Db.execute(rawDbQuery5)

    rawDbQuery7 = """ SELECT RegionID,SUM(MATTY) FROM #tmp4 GROUP BY RegionID """

    rawDbOutput6 = cursorOn36Db.execute(rawDbQuery7)
    RAWDbMatty4 = rawDbOutput6.fetchall()

    for each in range(list(RAWDbMatty4).__len__()):
        print("-------------------RAW DB OutPut-----------------")
        RAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid.append("Womens Health Care Market TQTY" + "|" + "commercial w/o Managed Medicaid" + "|" + RAWDbMatty4[each][0] + "|" + str(RAWDbMatty4[each][1]))
        ###RAWDbOutputSupraxCapTabManagedMedicaid.append                 ("Suprax Chew MAREKT TRX" + "|" + "Commercial w/o Managed Medicaid" + "|" + RAWDbMatty2[each][0] + "|" + str(RAWDbMatty2[each][1]))
        print(RAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid)

###     Comparing  The  Matty of Womens' Healthcare TQTY for  commercial w/o Managed medicaid Channel against Report Matty    ###

def CompareRAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid():
    RAWDBMattyWomensHealthcarecommwithoutManagedMedicaid()
    count3 = 0
    ##print(ReportOutput)
    for i in range(RAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid.__len__()):
        item1 = RAWDBMattyWomensHealthcarecommercialwithoutManagedMedicaid[i]
        print(" ")
        for j in range(ReportOutput.__len__()):
        ##print(ReportOutput[j])
                if (ReportOutput[j] == item1):
                    print(" ")
                    count3 = count3 + 1

        return count3

