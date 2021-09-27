
from flask import Flask,jsonify,request,make_response,url_for,redirect
#import requests, json
#import pandas as pd
#import os
# from google.cloud import bigquery

app = Flask(__name__)

# url = 'https://hooks.zapier.com/hooks/catch/xxxxx/yyyyy/'

@app.route('/')
def home():
    return '''<h1>Test API for Dynamic Vocher</h1>
<p>A smaple api application which gets response and gives back voucher details.</p>'''


@app.route('/create', methods=['POST'])
def create_row_in_gs():
    if request.method == 'POST':
        #TransId = request.json["TransId"]
        #AmountUsed = request.json["AmountUsed"]
        #MembershipId = request.json["MembershipId"]
        MemberPhone = request.json["MemberPhone"]
        print("Received_Input")
        #Sequence = request.json["Sequence"] 
        #BalanceType = request.json["BalanceType"] 
        #RecognitionId = request.json["RecognitionId"]
        #MemberEmail = request.json["MemberEmail"]
        #SchemeId = request.json["SchemeId"]
        #VoucherExpiry = request.json["VoucherExpiry"]
        #BalancePoints = request.json["BalancePoints"]
        #IsEnrollment = request.json["IsEnrollment"]
        #MemberType = request.json["MemberType"]
        #TransactionDate = request.json["TransactionDate"]
        #TransAmount = request.json["TransAmount"]  
        #ComplexName = request.json["ComplexName"]

#         create_row_data = {'TransId': TransId,'AmountUsed':AmountUsed,
#                            'MembershipId':str(MembershipId),'MemberPhone':str(MemberPhone),
#                            'Sequence':(Sequence), 'BalanceType' : (BalanceType),
#                            'RecognitionId':(RecognitionId), 'MemberEmail':str(MemberEmail),
#                            'SchemeId':(SchemeId),'VoucherExpiry':str(VoucherExpiry),
#                            'BalancePoints':(BalancePoints),'IsEnrollment':str(IsEnrollment),
#                            'MemberType':str(MemberType),'TransactionDate':str(TransactionDate),
#                            'TransAmount':TransAmount,'ComplexName':ComplexName}


        # df = pd.DataFrame([create_row_data], columns=create_row_data.keys())
        # df['Voucher'] = str('VCO'+str(MemberPhone))
        # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'C:\Users\I2103\Desktop\venv\first-energy-305211-b9163fe4fff3.json'
        # bigqueryClient = bigquery.Client()
        # job_config = bigquery.LoadJobConfig( 
        #     write_disposition="WRITE_APPEND",
        # )
        # table_id = 'test_dataset.voucher_logs'
        # job = bigqueryClient.load_table_from_dataframe(df, table_id, job_config=job_config)  # Make an API request.
        # job.result()          

        # response = requests.post(
        #     url, data=json.dumps(create_row_data),
        #     headers={'Content-Type': 'application/json'}
        # )
        # return response.content
        print(str('VCO'+str(MemberPhone)))
        return str('VCO'+str(MemberPhone))
        
        


if __name__=='__main__':
    app.run(debug=False)
    

