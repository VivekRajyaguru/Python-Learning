from Classes import MessageUser
import json
import smtplib


addFlag = 'Y'
to_List = []
while ((addFlag == 'Y' or addFlag == 'y') and len(to_List) < 3):
	temp_To = raw_input("Enter Recipients Address: ")
	if(temp_To != ''):
		to_List.append(temp_To)
		addFlag = raw_input("Do you want to add more Recipients?(Y/N) ")
	else:
		addFlag = 'N'
		pass

print(to_List)

#obj = MessageUser()

#obj.addUserDetails('Vivek', 'vivekrajyaguru1993@gmail.com', 'This is Sample Message', 'Sample Subject')
#obj.addUserDetails('Test', 'test@gmail.com', 'This is Sample Message2', 'Sample Subject2')
#obj.addUserDetails('Admin', 'admin@gmail.com', 'This is Sample Message3', 'Sample Subject3')

#obj.getUserDetails()

with open('Configuration.json') as json_data:
		data = json.load(json_data)

email_conn = smtplib.SMTP(data['host'], data['port'])
email_conn.ehlo()
email_conn.starttls()
try:
	email_conn.login(data['userName'], data['password'])
	email_conn.sendmail(data['userName'], to_List, 'MessageBody Example.')
except SMTPAuthenticationError:
		print('Error Occured while Login')
except:
		print('Error Occured')
		
email_conn.quit()
