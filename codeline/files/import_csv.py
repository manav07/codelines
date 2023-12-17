from datetime import datetime
import json
from numpy import datetime64
import openpyxl
# import pandas lib as pd
import pandas as pd

def excel_to_json():
    # columns = ["Pay Date", "Period Start", "Period End", "Period", "Remote Cutoff Date", "Final Approval"]
    # convert_dict = {'Pay Date': datetime, 'Period Start': datetime, 'Period End': datetime, 'Remote Cutoff Date': datetime, 'Final Approval': datetime, 'Period': int}
    # convert_dict = {'PayDate': datetime, 'PeriodStart': datetime, 'PeriodEnd': datetime, 'RemoteCutoffDate': datetime, 'FinalApprovalDate': datetime, 'Period': int}
    # sheets_dict = pd.read_excel('~/Downloads/2024updated.xlsx', sheet_name="B5-P5-C2-D5 (duplicate)")
    # res = {"year": 2024}
    # calendar=[]
    # for name, sheet in sheets_dict.items():
        
        # if name in ["Holiday Schedule 2024", "B1-P6-C3-D1", "Monthly 1st Advance","Monthly 25th", "SM15EOMPE1025", "NOT USED - Semi 10th & 26th"]:
        #     continue
        #print(f'name : {name}')
        # if "duplicate" in name or "Duplicate" in name:
        #     name = name.split(" ")[0]
        columns = ["Pay Date", "Period Start", "Period End", "Period Number", "Remote Cutoff Date", "Final Approval"]
        df = pd.read_excel('~/Downloads/2024updated.xlsx', engine='openpyxl', sheet_name="B5-P5-C2-D5 (duplicate)").reindex(columns=columns)
        # df.fillna('', inplace=True)
        print(df)
        df = df.dropna()
        df = df.reset_index(drop=True)
        #print(f'data frame : {df}')
        column_name = {'Pay Date': 'PayDate', 'Period Start': 'PeriodStart', 'Period End': 'PeriodEnd', 'Remote Cutoff Date': 'RemoteCutoffDate', 'Final Approval': 'FinalApprovalDate'}
        df.rename(columns=column_name, inplace=True)
        
        # if name in ["B5-P7-C2-D5", "B5-P5-C2-D5-PD5", "B5-P7-C3-D5", "B5-P6-C2-D5", "B4-P5-C1-D4", "M5", "MP15", "MP20", "MP26", "MPEOM", "SM15EM1WL", "Semi-Monthly", "SMP116", "SMP520", "SMP622", "SM722", "W5-C4-P6-D5", "W5-C3-P7-D4"]:
        #     print(f'name : {name}')
        #     df['PayDate'] = df['PayDate'].astype('datetime64[Y]')
        #     df['PeriodStart'] = df['PeriodStart'].astype('datetime64[Y]')
        #     df['PeriodEnd'] = df['PeriodEnd'].astype('datetime64[Y]')
        #     df['RemoteCutoffDate'] = df['RemoteCutoffDate'].astype('datetime64[Y]')
        #     df['FinalApprovalDate'] = df['FinalApprovalDate'].astype('datetime64[Y]')
        #     # df['PayDate'] = df['PayDate'].map(lambda x: x.isoformat())
        #     # df['PeriodStart'] = df['PeriodStart'].map(lambda x: x.isoformat())
        #     # df['PeriodEnd'] = df['PeriodEnd'].map(lambda x: x.isoformat())
        #     # df['RemoteCutoffDate'] = df['RemoteCutoffDate'].map(lambda x: x.isoformat())
        #     # df['FinalApprovalDate'] = df['FinalApprovalDate'].map(lambda x: x.isoformat())
        #     #df['timestamp'].map(lambda x: x.isoformat())
        #     df['Period'] = df['Period'].astype(str)
        
        
        #df = df.astype(convert_dict)
        #print(sn.sheet_names)
        # a = df.to_dict(orient = "records")
        #print(a)
        #df = df.astype(str)
        #a = df.to_json(orient = "records",date_format='iso')
        a = df.to_dict(orient="records")
        ans = {}
        ans['SceduleId'] = "B5-P5-C2-D5 (duplicate)"
        ans['ScheduleData'] = a
        # for i in ans['ScheduleData']:
        #     for j in i:
        #         ans['ScheduleData'][i][j] = int(round(ans['ScheduleData'][i][j]))
        print(ans)

    #     calendar.append(ans)
    #     #res = json.dumps(ans)

    #     #print(ans)
    # print(calendar)
    # res["YearCalendar"] = calendar
    #print(res)
    # final = json.dumps(res)
    # print(final)
    # print(a)
    # print(df)
    # for i in df:
    #     print('loop going on.....')
    #     print(i)
    # all_data  = pd.concat(l, ignore_index=True) # concat all data
    # print(all_data)
    # dataframe1 = pd.read_excel('~/Downloads/Revised-Payroll.xlsx',engine='openpyxl')
    # print(dataframe1)

excel_to_json()