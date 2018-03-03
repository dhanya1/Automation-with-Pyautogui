from invoice2data import extract_data
import json,pandas
import csv,os
import sys, subprocess

HOME = os.environ['HOME']
template_folder = sys.argv[2].strip()
invoices_folder = sys.argv[1].strip()
invoice_files = [os.path.join(invoices_folder,f) for f in os.listdir(invoices_folder) if os.path.isfile(os.path.join(invoices_folder, f))]
print('Template:',template_folder)
for each in invoice_files:
    if not '.pdf' in each:
        continue
    result = extract_data(each)
    if not result:
        cmd =['invoice2data','--template-folder', template_folder, each]
        session = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        result = session.communicate()[0].decode('UTF-8')
        print(result)
        result_json = json.loads(result)
        print(result_json) 
    #result = extract_data('/Users/hithyshikrishnamurthy/Downloads/Pearson_Converted_3.split/Pearson_Converted_3.1.pdf')
    csvfile_name = HOME+'/Desktop/invoice_details.csv'
    first_write = True

    if os.path.exists(csvfile_name):
        first_write = False

    with open(csvfile_name,'a') as csvfile:
        fields = ['Invoice Number', 'Supplier Name','Invoice Date','VAT','Net Amount','Gross Amount']
        writer = csv.DictWriter(csvfile, fields)
        if first_write:
            writer.writerow({'Invoice Number':'Invoice Number','Supplier Name':'Supplier Name','Invoice Date':'Invoice Date','VAT':'VAT','Gross Amount':'Gross Amount','Net Amount':'Net Amount'})
        writer.writerow({'Invoice Number':result['invoice_number'],'Supplier Name':result.get('issuer','default'),'Invoice Date':result['date'],'VAT':result.get('vat','0'),'Gross Amount':result['amount'],'Net Amount':result['amount_untaxed']})


