import PyPDF2,re
preader=PyPDF2.PdfFileReader(r"/home/om/Downloads/1S00155 (1).pdf")
#print(preader.getNumPages())
po=preader.getPage(262)
e=po.extractText()
e=" ".join(e.split())
#print(e)
string=e
li=re.split("(\d{7}.*?(?=\d{7})|(?=50: COMPU[\-]*))",string)
##for i in li:
##    count=0
##    print("leni",len(i))
##    for j in range(len(i)):
##        if i[j]==r"-" or i[j]==r"=":
##            count+=1
##    print(count,i)
##    if count>86:
##        li.remove(i)
##    elif i=="":
##        li.remove(i)
####for i in li:
####    print(i)
##print(li)
for i in li:
    print(i.count(r"-"))
    if((i.count("-")+i.count("="))>86):
        li.remove(i)
    elif(i==""):
        li.remove(i)
print(li)

    
