

def investmentCalc(principal,div,growth,ann_cont,time):
   annual_bal=[]

   for i in range(time):
       principal=((principal*(1+(growth*.01)))+(principal*div*.01)+ann_cont*(1.03**i))
       annual_bal.append(principal)


    

   return annual_bal[-1]

print("new balance ",investmentCalc(16000,3.5,10.7,29000,3))
