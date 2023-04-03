def reverse_number(a):    
    import re   
    out=''    
    s=re.split('([\d]+)',a)   
    print(s) 
    for i in s:   
        if i.isnumeric(): 
           out+=i[::-1] 
        else:      
           out+=i 
    print(out)      
reverse_number('0PIKA123CHU456')


