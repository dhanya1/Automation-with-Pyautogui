#!/usr/bin/python
import sqlite3
import cgi
import logging,sys
'''
print "Location: file:///Users/hithyshikrishnamurthy/Desktop/dummyap_system.html"
print 
print

print "Content-type: text/html\n\n"
print "<html><body>\n"
print "<meta http-equiv=\"refresh\" content=\"0; url = file:///Users/hithyshikrishnamurthy/Desktop/dummyap_system.html\" />"
print "</body></html>"
'''
logging.basicConfig(filename='/Users/hithyshikrishnamurthy/cgi-bin/server_script.log',level=logging.DEBUG, format='%(asctime)s %(level)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
form = cgi.FieldStorage()
print(form)


day = form['day'].value
month = form['month'].value
year = form['year'].value
supplier_name =  form['Supplier Name'].value
invoice_number = form['Invoice Number'].value
net_amount = form['Net amount'].value
VAT = form['VAT'].value
gross_amount = form['Gross Amount'].value
invoice_date = '-'.join([year,month,day])

if day and month and year and supplier_name and invoice_number and net_amount and VAT and gross_amount and invoice_date:
    logging.debug('Successfully received the information with post')
else:
    logging.warning('SOME NULL VALUES FOUND!!')

try:
    conn = sqlite3.connect('/Users/hithyshikrishnamurthy/cgi-bin/ap_system')
except:
    print "Unable to connect"
    logging.error('Error')
sql = '''INSERT INTO invoice_details(invoice_date,invoice_number,supplier_name,net_amount,VAT,gross_amount) VALUES (?,?,?,?,?,?)'''

values = (str(invoice_date),int(invoice_number),str(supplier_name),int(net_amount),int(VAT),int(gross_amount))
a = open('/Users/hithyshikrishnamurthy/cgi-bin/in_file','w')
for i in values:
	a.write(str(i))
a.close()

#values = ('1999-12-12',53456,'Dhana',3256457,43,8909)
cur = conn.cursor()
try:
    cur.execute(sql,values)
except:
    print sys.exc_info()[0]
    logging.error(sys.exc_info()[0])
conn.commit()
conn.close()

