import re
# mail_pattern=r'[\w\.-]+@[\w\.-]+'
mail_pattern=r'\b[A-Z0-9a-z._%+-]+@[A-Z0-9a-z._-]+\.[A-Za-z]{2,}\b'


#RSPO.html - https://rspo.gov.pl/institutions?q=%7B%22filter%22:%22wielkopolska%22%7D 
# rządowa wyszukiwarka placówek oświatowych w wielkopolskce
with open('RSPO.html','r',encoding='utf-8') as f_input: #encoding - problemy na windowsie z otworzeniem pliku
    with open('B04output.txt','w') as f_output:
        f_content = f_input.read()
        emails = re.findall(mail_pattern,f_content)
        # print(f_content)
        for email in emails:
            print(email)
            f_output.write(email)
            f_output.write('\n')
            

f_input.close()
f_output.close()