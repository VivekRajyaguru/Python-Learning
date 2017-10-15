import datetime

class MessageUser():
	User_Details = []
	messsage = []
	
	
	def addUserDetails(self, name, email, message, subject):
		details = {
			"name": name,
			"email": email,
			"message": message,
			"subject": subject
		}
		today = datetime.date.today()
		details['date'] = today
		self.User_Details.append(details)
		
	def getUserDetails(self):
		print(self.User_Details)
		return self.User_Details