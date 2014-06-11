import urllib, json,sys
id= sys.argv[1]
limit = sys.argv[2]
url = "http://localhost:8000/payments_hdfc/"+id+"/"+limit+"/?format=json"
response = urllib.urlopen(url);
data = json.loads(response.read())
print "data captured"
i=0
for d in data:
	try:
		if str(d['result']).lower() == "captured":
			try:
				udf2 =str(d['udf2'])
			except:
				udf2= "cannot be converted to string"
			url = "http://localhost:8001/crm_data/?email="+str(d['udf1'])+"&id="+str(d['id'])+"&currency="+str(d['currency'])+"&amount="+str(d['amount'])+"&payment_id="+str(d['payment_id'])+"&result="+str(d['result'])+"&tran_id="+str(d['tran_id'])+"&details="+str(d['details'])+"&auth="+str(d['auth'])+"&error="+str(d['error'])+"&error_msg="+str(d['error_msg'])+"&phone="+str(d['phone'])+"&udf1="+str(d['udf1'])+"&udf2="+udf2+"&udf3="+str(d['udf3'])+"&udf4="+str(d['udf4'])+"&udf5="+str(d['udf5'])+"&product_id="+str(d['product_id'])+"&created="+str(d['created'])+"&source="+str(d['source'])+"&format=json";
			response = urllib.urlopen(url)
			print "Done_lead_id : "+str(i)
	except:
		print "some error in lead_id :"+str(i)
	i=i+1
