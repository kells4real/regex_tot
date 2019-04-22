import re 


pattern_phone = re.compile(r'\d{3}[-.]\d{3}[-.]\d{3}[-.]\d{2}')
pattern_name = re.compile(r'[A-Z][a-z\']+\s[A-Z][a-z\']+')
pattern_website = re.compile(r'http[s]?://(www.)?([a-zA-Z-.]+\.\w+\.?\w+)')
pattern_email = re.compile(r'[A-Za-z0-9-._]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
pattern_id = re.compile(r'(RE[0-9]{6}r)|(EU[0-9]{6}e)|(NG[0-9]{6}n)')
pattern_cc_master = re.compile(r'(51|52|53|54|55)[0-9]{2}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}')
pattern_cc_visa = re.compile(r'(41|44|43|42)[0-9]{2}\-[0-9]{4}\-[0-9]{4}\-[0-9]{2}')
pattern_cc_discovery = re.compile(r'600[0-9]{3}\-[0-9]{6}\-[0-9]{6}')

with open('Your_data-file.txt', 'r') as f:
    content = f.read()



phone_nos = pattern_phone.finditer(content) 
names = pattern_name.finditer(content)
website = pattern_website.finditer(content)
email = pattern_email.finditer(content)
id = pattern_id.finditer(content)
master = pattern_cc_master.finditer(content)
visa = pattern_cc_visa.finditer(content)
discovery = pattern_cc_discovery.finditer(content)

file = open('filtered_file.txt', 'a+')


print("*****************************************PHONE NOS*********************************************")
file.write("*****************************************PHONE NOS*********************************************")
file.write('\n')
for match in phone_nos:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
    file.write('\n')

print()


print('*******************************************NAMES**********************************************')
file.write("*****************************************NAMES*********************************************")
file.write('\n')
for match in names:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
print()
print("*******************************************DOMAINS**********************************************")
file.write("*****************************************DOMAINS*********************************************")
file.write('\n')
for match in website:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
print()
print("********************************************ID**************************************************")
file.write("******************************************ID***********************************************")
file.write('\n')
for match in id:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
print()
print("*********************************************EMAILS******************************************")
file.write("*****************************************EMAILS*********************************************")
file.write('\n')
for match in email:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
print()
print("**********************************************MASTER CARD*************************************")
file.write("*****************************************MASTER CARD*********************************************")
file.write('\n')
for match in master:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
print()
print("************************************************VISA CARD*********************************************")
file.write("*****************************************VISA CARD*********************************************")
file.write('\n')
for match in visa:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
print()
print("**********************************************DISCOVERY CARD*************************************")
file.write("*****************************************DISCOVERY CARD*********************************************")
file.write('\n')
for match in discovery:
    matches = match.group(0)
    print(matches)
    file.write(matches)
    file.write('\n')
print()



file.close()