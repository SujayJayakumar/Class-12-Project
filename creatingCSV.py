import csv
products=open('products.csv','w',newline='')
l=[]
l2=['laptop',900,55]
l1=['Phone',200,77]
l3=['HDD',200,44]
l.append(l1)
l.append(l2)
l.append(l3)
w=csv.writer(products)
w.writerows(l)
products.close()
    
    
    
    
