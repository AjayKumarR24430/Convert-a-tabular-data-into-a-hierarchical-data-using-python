import pandas
df1=pandas.read_excel('hierarchy_case_20May2020.xlsx').fillna("@Null$tring").sort_values(by=['NAME', 'EMPLOYEE_ID', 'MANAGER EMPLOYEE_ID'])
headers1 = list(df1.loc[:,"NAME"])
headers2 = list(df1.loc[:,"EMPLOYEE_ID"])
headers3= list(df1.loc[:, "MANAGER EMPLOYEE_ID"])
designation = list(df1.loc[:,"DESIGNATION"])
dept = list(df1.loc[:,"DEPARTMENT"])
messageList=[]
messageList.extend(['<!DOCTYPE html>','<html lang=\"en\">','<head>','<meta charset=\"UTF-8\">','<title>\"Excel to Treeview using Python\"</title>','<link rel=Stylesheet type=\"text/css\" media=all>','</head>','<body>','<div>','<ul>'])
for i in range(len(headers1)):
    if headers1[i] != '@Null$tring' and (i==0 or headers1[i] != headers1[i-1]):
        messageList.append('<li><input type=\"checkbox\" /><label>%s</label><ul>' % (headers1[i]))
    if headers2[i] != "@Null$tring" and (i== 0 or headers2[i] != headers2[i-1]):
        messageList.append('<li><input type=\"checkbox\"/><label>%s</label><ul>' % (headers2[i]))
    messageList.append('<li>%s</li>' % ( dept[i]))
    if i+1!=len(headers1):
        if headers1[i+1]!=headers1[i]:
            messageList.append('</ul></li>')
            if headers2[i]!='@Null$tring':
                messageList.append('</ul></li>')
        elif headers2[i+1] != headers2[i] and headers2[i]!='@Null$tring':
            messageList.append('</ul></li>')
messageList.append('</ul></div></body></html>')
f = open('output.html', 'w')
for msg in messageList:
    f.write(msg)
    f.write("\n")
f.close()