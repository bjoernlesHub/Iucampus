WebCrawler.py is a app that searching for words in html lists.
This first version is just for ebay-kleinanzeigen.de.
You have to install some Python libs and SQL.
Some important settings (for sql and email) in json format you will find in settings.txt.

----Python libs (type in cmd):----
	---recommended---
pip install json

	---not important---
pip install flask



----SQL----
Columns :

id (int)- autoincrement, primary key
name (varchar 100)
url (varchar 200)
datetimeorig (datetime)
datetime (timestamp)