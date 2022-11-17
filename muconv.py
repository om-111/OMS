import regex as r1
import re
def seperate_records(string):

    string=" ".join(string.split())
    #Changes Done 5 March
    string=re.sub("PAGE.*?(?=\d{7})","",string)
    string=re.sub("50: COMPUTER .*?TATION","",string)
    string=re.sub("\-{6}\s\-{6}",r"------------",string)
    string=re.sub("\-{215} \/.*\-{215}$","",string)
    string=re.sub("\-{215}","",string)
    
    #
    char_rems=["@1","@2","@3","="]
    for c in char_rems:
        string=string.replace(c,"")
    print(string)
    q=re.split("(\d{7})",string)
    
    q1=[]
    print(q)
    #print(len(q))
    while "" in q:
        q.remove("")
    #print(len(q))
    for i in q:
        i="".join(i.split())
        q1.append(i)
    
    print(q1)
    return q1
def rec_merge(li):
    mrec=[]
    #print(li)
    for i in range(len(li)):
        if i%2!=0:
            mrec.append(li[i-1]+li[i])
    #print(mrec)
    return mrec
def rev_space(t):
    t="".join(t.split())
    return t[::-1]
def rev_list(l):
    temp=[]
    for i in l:
        temp.append(i[::-1])
    temp.reverse()
    return temp


dummypage=r"""
PAGE : 268
OFFICE REGISTER FOR B.Sc. (COMPUTER SCIENCE)(SEM V)(CBCGS) EXAMINATION - DECEMBER 2020
DATE : FEBRUARY 26, 2021
CENTRE :
8 KALYAN
=======================================================================================================================================================================================================================
CREDITS
COURSE I - 3
COURSE II - 3
COURSE III - 2 COURSE IV - 3 COURSE V - 3 COURSE VI - 2 COURSE VII - 2 COURSE VIII - 1 COURSE IX - 1
TOTAL -20
SEAT NO
NAME
<------------ COURSE-I ----------><------------ COURSE-II -------------> <------------ COURSE-III-------------><------------ COURSE-IV ---------->
MARKS
75/30 25/10 100 C
G GP C*GP
75/30 25/10
100 C
G GP
C*GP
100/40
C G GP C*GP
75/30 25/10 100 C G
GP C*GPäC äCG RSLT
<------------ COURSE-V ----------><------ COURSE-VI -------> <------------ COURSE-VII-------------><---- COURSE-VIII ----><----- COURSE-IX ----->
COLLEGE
MARKS
75/30 25/10 100 C G GP
C*GP
100/40 C G GP C*GP
75/30 25/10 100 C G
GP
C*GP
50/20 C G
GP C*GP
50/20 C G
GP C*GP äC
äCG
GPA GRADE
=======================================================================================================================================================================================================================
50: COMPUTER SCIENCE
COURSE I :USCS501
:ARTIFICIAL INTELLIGENCE
COURSE II :USCS503
:SOFTWARE TESTING AND QUALITY ASSURANCE
COURSE III:USCSP501 :PRACTICAL OF ELECTIVE-I
COURSE IV :USCS504
:INFORMATION AND NETWORK SECURITY
COURSE V :USCS505
:ARCHITECTING OF IoT
COURSE VI :USCSP502 :PRACTICAL OF ELECTIVE-II
1: SKILL ENHANCEMENT
COURSE VII:USCS507
:GAME PROGRAMMING
COURSE VIII :USCSP504 :PRACTICAL OF SKILL ENHANCEMENT : USCS507
COURSE IX :USCSP503 PROJECT IMPLEMENTATION
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2132147
YADAV SATISH HARISHANKAR URMILA
70 O 19 A+ 89 3 O 10 30.00 69
O 22
O
91 3
O 10
30.00
82
2 O
10
20 60 O
23 O
83
3 O
10
30.00
P
L.D.SONAWANE AS
69 O 22 O
91 3 O 10 30.00 76 2 A+ 9
18
44
B+ 18
A+ 62 2 A
8
16.00
39
1 O
10
10
37 1
O
10
10
20.00 194.00 9.70
@1
@3
2132148
SIDDIQUI AARIF HUSSAIN ISHTIYAQU
65 O 19 A+ 84 3 O 10 30.00 70
O 23
O
93 3
O 10
30.00
89
2 O
10
20 53 A+ 19 A+ 72
3 A+
9
27.00
P
E HUSSAIN SUFIYA B
L.D.SONAWANE AS
72 O 23 O
95 3 O 10 30.00 84 2 O 10
20
45
A 19
A+ 64 2 A
8
16.00
38
1 O
10
10
38 1
O
10
10
20.00 193.00 9.65
@2
@2
50: COMPUTER SCIENCE
COURSE I :USCS502
:LINUX SERVER ADMINISTRATION
COURSE II :USCS503
:SOFTWARE TESTING AND QUALITY ASSURANCE
COURSE III:USCSP501 :PRACTICAL OF ELECTIVE-I
COURSE IV :USCS504
:INFORMATION AND NETWORK SECURITY
COURSE V :USCS506
:WEB SERVICES
COURSE VI :USCSP502 :PRACTICAL OF ELECTIVE-II
1: SKILL ENHANCEMENT
COURSE VII:USCS507
:GAME PROGRAMMING
COURSE VIII :USCSP504 :PRACTICAL OF SKILL ENHANCEMENT : USCS507
COURSE IX :USCSP503 PROJECT IMPLEMENTATION
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2132149
VIJAY ACHARI CHITRA
75 O 25 O 100 3 O 10 30.00 75
O 25
O 100 3
O 10
30.00
80
2 O
10
20 32 D
12 C
44
3 D
4
12.00
P
MODEL COL. KALY
66 O 23 O
89 3 O 10 30.00 85 2 O 10
20
43
B+ 12
C
55 2 B+
7
14.00
42
1 O
10
10
39 1
O
10
10
20.00 176.00 8.80
@1
2132150
AHER ASHISH RAJENDRA SANDHYA
75 O 22 O
97 3 O 10 30.00 75
O 25
O 100 3
O 10
30.00
83
2 O
10
20 58 A+ 18 A+ 76
3 A+
9
27.00
P
MODEL COL. KALY
75 O 22 O
97 3 O 10 30.00 87 2 O 10
20
66
O 18
A+ 84 2 O
10
20.00
45
1 O
10
10
47 1
O
10
10
20.00 197.00 9.85
2132151
DESHMUKH SOURABH MANGESH MINAL
75 O 25 O 100 3 O 10 30.00 75
O 25
O 100 3
O 10
30.00
79
2 O
10
20 64 O
20 O
84
3 O
10
30.00
P
MODEL COL. KALY
@1
58 A+ 17 A
75 3 A+ 9 27.00 79 2 O 10
20
64
O 17
A
81 2 O
10
20.00
40
1 O
10
10
38 1
A+
9
9
20.00 196.00 9.80
@1
2132152
DEVLEKAR ANKIT ARUN ARCHANA
56 A+ 19 A+ 75 3 A+ 9 27.00 60
O 23
O
83 3
O 10
30.00
84
2 O
10
20 60 O
19 A+ 79
3 O
10
30.00
P
MODEL COL. KALY
@1
73 O 16 A
89 3 O 10 30.00 78 2 O 10
20
68
O 19
A+ 87 2 O
10
20.00
40
1 O
10
10
35 1
A+
9
9
20.00 196.00 9.80
@2
2132153 /DEWRE KIRAN SANTOSH JYOTI
75 O 25 O 100 3 O 10 30.00 75
O 25
O 100 3
O 10
30.00
85
2 O
10
20 69 O
21 O
90
3 O
10
30.00
P
MODEL COL. KALY
75 O 19 A+ 94 3 O 10 30.00 91 2 O 10
20
66
O 18
A+ 84 2 O
10
20.00
45
1 O
10
10
36 1
A+
9
9
20.00 199.00 9.95
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/ - FEMALE, # - 0.229 ,@ - O.5042,@ - O.5044A ,* - 5045 , ADC - ADMISSION CANCELLED, RR-RESERVED, --:Fails in Theory or Practical,RPV - PROVISIONAL, RCC - O.5050, A,ABS - ABSENT , F - UNSUCCESSFUL, P - SUCCESSFUL;
NULL-NULL & VOID, G:grade GP:gradepoints C:credits CP:credit points
äCG:sum of product of credits & grades, Internal Marks are Provisional as per R.8668
äC:sum of credit points
GPA: äCG
/äC
MARKS
: >=80
>=70 and <80
>=60 and <70
>=55 and <60
>=50 and <55
>=45 and <50
>=40 and <45
<40
GRADE
:
O
A+
A
B+
B
C
D
F
GRADE POINT : 10
9
8
7
6
5
4
0
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""



a=seperate_records(dummypage)
b=rec_merge(a)

D="2131427GOPALENIKHILDASHRATHVANDANA47A13B603A824.0049A11D603A824.00672A81662O16A783O1030.00PMENONBHANDUP-62O16A783O1030.00672A81654A+11D652A816.00401O1010351A+9920.00175.008.75"
o1="2132033  /KUNWAR NARAYANI SHIVBAHADUR BHAG    53  A+ 23  O   76  3  A+ 9 27.00  41   B+23    O   64  3   A  8   24.00        87   2  O     10     20  75  O 20  O   95   3  O   10   30.00           P   AWATI                K.M.AGRAWAL-KAL56  A+ 23  O   79  3  O 10 30.00  81  2 O  10   20     58   A+ 16   A   74  2  A+     9    18.00     28   1  B+    7   7   40 1   O    10    10   20.00  186.00  9.30@12132034  /KUREEL PRATIBHA CHHUNNULAL NEELA    71  O  24  O   95  3  O 10 30.00  69   O 24    O   93  3   O 10   30.00        88   2  O 10     20  75  O   24  O   99   3  O   10   30.00           P   M                    K.M.AGRAWAL-KAL56  A+ 24  O   80  3  O 10 30.00  88  2 O  10   20     56   A+ 23   O   79  2O     10    20.00     42   1  O    10     10   43 1   O    10    10   20.00  200.00 10.00@12132035   LAKISARE CHAITANYA SANDIP SANGEE 71  O  22  O   93  3  O 10 30.00  56   A+20    O   76  3   A+ 9   27.00               82   2  O     10     20  66  O   20  O 86   3  O   10   30.00           P   TA                   K.M.AGRAWAL-KAL60  O  20  O   80  3  O 10 30.00  79  2 O  10   20     69   O  16   A   85  2  O     10    20.00     25   1  B     6      6  42 1   O    10    10   20.00  193.00  9.65@12132036  /LODHI KIRAN CHANDRAKISHOR GUDIYA    68  O  23  O   91  3  O 10 30.00  75   O 23    O   98  3   O 10   30.00           79   2  O     10     20  75  O   19  A+  94   3  O   10   30.00           P   K.M.AGRAWAL-KAL      @156  A+ 23  O   79  3  O 10 30.00  89  2 O  10   20     75   O  23   O   98  2  O     10    20.00     41   1  O    10     1040 1   O    10    10   20.00  200.00 10.00@12132037  /MANDAVE NEHA SHASHIKANT SANGITA     56  A+ 22  O   78  3  O 10 30.00  69   O 22    O   91  3   O 10   30.00        83   2  O     10     20  69  O   24  O   93   3  O   10   30.00           P   K.M.AGRAWAL-KAL                   @245  A  21  O   66  3  A  8 24.00  86  2 O  10   20     30   D  20   O   50  2  B 6    12.00     40   1  O    10     10   40 1   O    10    10   20.00  186.00  9.302132038   MANDEKAR AQUEB ASMAT ANIKA          75  O  21  O   96  3  O 10 30.00  75   O 20    O   95  3   O 10   30.00        80   2  O     10     20  75  O   24 O   99   3  O   10   30.00           P   K.M.AGRAWAL-KAL73  O  20  O   93  3  O 10 30.00  84  2 O  10   20     75   O  16   A   91  2  O     10    20.00     25   1  B     6      6 38 1   O    10    10   20.00  196.00  9.80@22132039  /MHASE JAGRUTI SURESH SUVARNA        66  O  20  O   86  3  O 10 30.00  69   O 21    O   90  3   O 10   30.00               82   2  O     10     20  62  O20  O   82   3  O   10   30.00           P RPV  K.M.AGRAWAL-KAL58  A+ 22  O   80  3  O 10 30.00  80  2 O  10   20     54   A+ 18   A+  72  2  A+     9    18.00     30   1  A     8      8  35 1   A+    9     9   20.00  195.00  9.752132040   MISTARI DEEPAK CHATUR YOJANA        64  O  20  O   84  3  O 10 30.00  66   O 20    O   86  3   O 10   30.00               86   2  O     10     20  75  O   21  O   96   3  O   10   30.00       P   K.M.AGRAWAL-KAL69  O  21  O   90  3  O 10 30.00 77  2 O  10   20     64   O  17   A   81  2  O     10    20.00     28   1  B+    7      7   30 1   A     8     8   20.00  195.00  9.75@32132041   NAGLEKAR SIDDHANT BALKRISHNA NET    75  O  22  O   97  3  O 10 30.00  75   O 22    O   97  3   O 10   30.00               84   2  O     10     20  75  O19  A+  94   3  O   10   30.00           P   RA                   K.M.AGRAWAL-KAL49  A  22  O   71  3  A+ 9 27.00  77  2 O  10   20     56   A+ 19   A+  75  2  A+     9    18.00     35   1  A+    9      9  35 1   A+    9     9   20.00  193.00  9.65"
rx_lt10=r1.compile(r"""(\d{7})(\/?)([a-zA-Z]*)"""+
                   r"""(\d{1,2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{1,3})(3)(\D{1,2})([1]?[0456789])(\d{1,2}[.]{1}00)"""+
                   r"""(\d{1,2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{1,3})(3)(\D{1,2})([1]?[0456789])(\d{1,2}[.]{1}00)"""+
                   r"""(\d{1,2})(2)(\D{1,2})([1]?[0456789])(\d{1,2})"""+
                   r"""(\d{1,2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{1,3})(3)(\D{1,2})([1]?[0456789])(\d{1,2}[.]{1}00)"""+
                   r"""([P|A])"""+#(RPV|.{0})(ABS|.{0})
                   r"""(\D*)"""+
                   r"""(\d{1,2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{1,3})(3)(\D{1,2})([1]?[0456789])(\d{1,2}[.]{1}00)"""+
                   r"""(\d{1,3})(2)(\D{1,2})([1]?[0-9])([12]?[0-9])"""+
                   r"""(\d{1,2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{1,3})(2)(\D{1,2})([1]?[0456789])(\d{1,2}[.]{1}00)"""+
                   r"""(\d{1,2})(1)(\D{1,2})([1]?[0456789])([1]?[0456789])(\d{1,2})(1)(\D{1,2})([1]?[0456789])([1]?[0456789])(\d{1,2}[.]{1}00)"""+
                   r"""(\d{1,3}\.00)"""+
                   r"""(\d{1}\.[\d]{2})"""
                  )
rx_eq10=r1.compile(r"""(\d{7})(\/?)([a-zA-Z]*)"""+
              r"""(\d{2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{2,3})(3)(O)(10)(30.00)"""+
              r"""(\d{2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{2,3})(3)(O)(10)(30.00)"""+
              r"""(\d{2,3})(2)(O)(10)(20)"""+
              r"""(\d{2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{2,3})(3)(O)(10)(30.00)"""+
              r"""([P|A])"""+#(RPV|.{0})(ABS|.{0})
              r"""(\D*)"""+
              r"""(\d{2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{2,3})(3)(O)(10)(30.00)"""+
              r"""(\d{2,3})(2)(O)(10)(20)"""+
              r"""(\d{2})(\D{1,2})(\d{1,2})(\D{1,2})(\d{2,3})(2)(O)(10)(20.00)"""+
              r"""(\d{2})(1)(O)(10)(10)"""+
              r"""(\d{2})(1)(O)(10)(10)"""+
              r"""(20.00)(200.00)(10.00)"""
              )
rx_fail=r1.compile(r"""(--)(\d{2}\.\d{1,3})(00\.[0-9][1]?|\-\-)"""+#'--', '00.161', '00.71'
               r"""([0-9][1]?|\-\-)([0-9][1]?|\-\-)([\+]?[ABCDFO]|\-\-)(1|\-\-)([EAF]?\d{0,2}|\-{2})"""+#'9', '9', '+A', '1', 'E83'
               r"""([0-9][1]?|\-\-)([0-9][1]?|\-\-)([\+]?[ABCDFO]|\-\-)(1|\-\-)([EAF]?\d{0,2}|\-{2})"""+#'01', '01', 'O', '1', 'E04'
               r"""(\d{2}\.[0-9][12]?|\-\-)([0-9][1]?|\-\-)"""+#'00.02', '01'
               r"""([\+]?[ABCDFO]0?|\-\-)(2|\-{2})([E]?\d{1,2}|A0?|E|F)([\+]?[ABCDFO]|\-\-)([EAF]?\d{0,2}|A0?|F)([\+]?[A-FO]|\-\-)([EAF]?\d{0,2}|A0?|F)"""+#'O', '2', '38', '+A','E91', 'O', 'E46'
               r"""([0-9][12]?|\-{2})([0-9][1]?|\-{2})([\+]?[ABCDFO]0?|\-\-)(2|\-{2})([E]?\d{1,3}|A0?|E|F)"""+
               r"""(\d{2}\.[0-9][123]?|\-\-)([0-9][1]?|\-\-)"""+
               r"""([\+]?[ABCDFO]0?|\-\-)(3|\-{2})([E]?\d{1,2}|A0?|E|F)([\+]?[ABCDFO]|\-\-)([EAF]?\d{0,2}|A0?|F)([\+]?[A-FO]|\-\-)([EAF]?\d{0,2}|A0?|F)"""+
               r"""(\D*)"""+
               r"""(F|A)"""+
               r"""(\d{2}\.[0-9][123]?|\-\-)([0-9][1]?|\-\-)"""+
               r"""([\+]?[ABCDFO]0?|\-\-)(3|\-{2})([E]?\d{1,2}|A0?|E|F)([\+]?[ABCDFO]|\-\-)([EAF]?\d{0,2}|A0?|F)([\+]?[A-FO]|\-\-)([EAF]?\d{0,2}|A0?|F)"""+
               r"""([0-9][12]?|\-{2})([0-9][1]?|\-{2})([\+]?[ABCDFO]0?|\-\-)(2|\-{2})([E]?\d{1,3}|A0?|E|F)"""+
               r"""(\d{2}\.[0-9][123]?|\-\-)([0-9][1]?|\-\-)"""+
               r"""([\+]?[ABCDFO]0?|\-\-)(3|\-{2})([E]?\d{1,2}|A0?|E|F)([\+]?[ABCDFO]|\-\-)([EAF]?\d{0,2}|A0?|F)([\+]?[A-FO]|\-\-)([EAF]?\d{0,2}|A0?|F)"""+
               r"""(\d{2}\.[0-9][123]?|\-\-)([0-9][1]?|\-\-)"""+
               r"""([\+]?[ABCDFO]0?|\-\-)(3|\-{2})([E]?\d{1,2}|A0?|E|F)([\+]?[ABCDFO]|\-\-)([EAF]?\d{0,2}|A0?|F)([\+]?[A-FO]|\-\-)([EAF]?\d{0,2}|A0?|F)"""+
               r"""(\D*)(\/?)(\d{7})"""
              )


#D2=rx_lt10.split(D)
#print(D2)
slist=[]
for i in b:
    if i[-11:]=='200.0010.00':
        templi=rx_eq10.split(i)
        pass
    elif i[-2:]=="--":
        temp=rev_space(i)
        tempo=rx_fail.split(temp)
        templi=rev_list(tempo)
        pass
    else:
        #print("running else")
        templi=rx_lt10.split(i)
        
        pass
    try:
        templi.pop(0)
        templi.pop(-1)
    except:
        pass
    if templi[1]==r"/":
        templi[1]="F"
    elif templi[1]==r"":
        templi[1]="M"
    slist.append(templi)
    #print(len(templi))
#print(len(slist))

HDR_ROW=(r"""SEATNO,GENDER,NAME,"""+
        r"""C1_75,C1_75_G,C1_25,C1_75_G,C1_Total,C1_C,C1_G,C1_GP,C1_CxGP,"""+
        r"""C2_75,C2_75_G,C2_25,C2_75_G,C2_Total,C2_C,C2_G,C2_GP,C2_CxGP,"""+
        r"""E1_100,E1_C,E1_G,E1_GP,E1_CxGP,"""+
        r"""C3_75,C3_75_G,C3_25,C3_75_G,C3_Total,C3_C,C3_G,C3_GP,C3_CxGP,"""+
        r"""Pass_Status,Extra_Chars_College_Name,"""+
        r"""C4_75,C4_75_G,C4_25,C4_75_G,C4_Total,C4_C,C4_G,C4_GP,C4_CxGP,"""+
        r"""E2_100,E2_C,E2_G,E2_GP,E2_CxGP,"""+
        r"""C5_75,C5_75_G,C5_25,C5_75_G,C5_Total,C5_C,C5_G,C5_GP,C5_CxGP,"""+
        r"""E3_50,E3_C,E3_G,E3_GP,E3_CxGP,"""+
        r"""Prj_50,Prj_C,Prj_G,Prj_GP,Prj_CxGP,"""+
        r"""Total_CP,GPA,GRADE"""+"\n")
tempstr=HDR_ROW
for i in slist:
    for field in i:
        tempstr=tempstr+field+","
    tempstr=tempstr+"\n"
#print(tempstr)

def create_data(raw_data):
    temp=seperate_records(raw_data)
    t=rec_merge(temp)
    #print(t)
    return t
##    for i in t:
##        if i[-11:]=='200.0010.00':
##            templi=rx_eq10.split(i)
##            pass
##        elif i[-2:]=="--":
##            print(i)
##            print("Failed")
##            pass
##        else:
##            templi=rx_lt10.split(i)
##            pass
##        templi.remove("")
##        templi.remove("")
##    templist.append(templi)
##    for i in templist:
##        for field in i:
##            tempstr=tempstr+field+","
##        tempstr=tempstr+"\n"
##    print(HDR_ROW+tempstr)

def raw2csv(data,HDRROW):
    tdata=create_data(data)
    tlist=[]
    tstr=HDRROW
    templi=[]
    for i in tdata:
        if i[-11:]=='200.0010.00':
            templi=rx_eq10.split(i)
            pass
        elif i[-2:]=="--":
            temp=rev_space(i)
            tempo=rx_fail.split(temp)
            templi=rev_list(tempo)
            pass
        else:
            #print("running else")
            templi=rx_lt10.split(i)
            pass
        try:
            templi.pop(0)
            templi.pop(-1)
        except:
            pass
        #print("E1")
        print(len(templi))
        print(templi)
        if templi[1]==r"/":
            templi[1]="F"
            #print("F")
        elif templi[1]=="":
            templi[1]="M"
            #print("M")
        #print("E2")
        tlist.append(templi)
    #print(tlist)
    #print("E3")
    for i in tlist:
        for field in i:
            tstr=tstr+field+","
        tstr=tstr+"\n"
    #print(tstr)
    return tstr
#raw2csv(dummypage,HDR_ROW)
    
