import sys
import pandas as pd

if len(sys.argv)!=2:
    print("Enter CSV File Name!")
    exit(0)
    
df = pd.read_csv(sys.argv[1])

tMaths = [df.iloc[0]]
tBiology = [df.iloc[0]]
tEnglish = [df.iloc[0]]
tPhysics = [df.iloc[0]]
tChemistry = [df.iloc[0]]
tHindi = [df.iloc[0]]

res = []
for i in list(df.iterrows())[1:]:
    if i[1]['Maths']>tMaths[0]['Maths']:
        tMaths = [i[1]]
    elif i[1]['Maths']==tMaths[0]['Maths']:
        tMaths.append(i[1])
    if i[1]['Biology']>tBiology[0]['Biology']:
        tBiology = [i[1]]
    elif i[1]['Biology']==tBiology[0]['Biology']:
        tBiology.append(i[1])
    if i[1]['English']>tEnglish[0]['English']:
        tEnglish = [i[1]]
    elif i[1]['English']==tEnglish[0]['English']:
        tEnglish.append(i[1])
    if i[1]['Physics']>tPhysics[0]['Physics']:
        tPhysics = [i[1]]
    elif i[1]['Physics']==tPhysics[0]['Physics']:
        tPhysics.append(i[1])
    if i[1]['Chemistry']>tChemistry[0]['Chemistry']:
        tChemistry = [i[1]]
    elif i[1]['Chemistry']==tChemistry[0]['Chemistry']:
        tChemistry.append(i[1])
    if i[1]['Hindi']>tHindi[0]['Hindi']:
        tHindi = [i[1]]
    elif i[1]['Hindi']==tHindi[0]['Hindi']:
        tHindi.append(i[1])

    if len(res)==3:
        res.sort(key=lambda x:x[1])
    if len(res)<3:
        res.append((i[1]['Name'],sum(i[1][1:])))
    else:
        if sum(i[1][1:])>res[0][1]:
            res[0] = (i[1]['Name'],sum(i[1][1:]))
            for i in range(0,2):
                if res[i][1]<res[i+1][1]:
                    break
                res[i],res[i+1]=res[i+1],res[i]

print("Topper in Maths is "+", ".join([i[0] for i in tMaths]))
print("Topper in Biology is "+", ".join([i[0] for i in tBiology]))
print("Topper in English is "+", ".join([i[0] for i in tEnglish]))
print("Topper in Physics is "+", ".join([i[0] for i in tPhysics]))
print("Topper in Chemistry is "+", ".join([i[0] for i in tChemistry]))
print("Topper in Hindi is "+", ".join([i[0] for i in tHindi]))

print("Best Students in the class are "+res[2][0]+", "+res[1][0]+", "+res[0][0]+".")
