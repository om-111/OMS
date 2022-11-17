import re
import PyPDF2
file=r"/home/om/Downloads/1S00155 (1).pdf"
p=open(file,"rb")
pr=PyPDF2.PdfFileReader(p)
pr.getNumPages()
po=pr.getPage(262)
e=po.extractText()
e="".join(e.split())
#print(e)
q=re.sub("PAGE.*?(?=\d{7})","",e)
q2=re.sub("\-{20}.*\-{20}","",q)
q=re.sub("50:COMPUTER.*\-*","",q2)
q2=re.sub("@\d","",q)
q=re.compile("(\d{7}.*?[05\-](?=\d{7}|.?))")
q2=re.split(q,q2)
print(q2)

