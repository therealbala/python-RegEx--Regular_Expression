def reverse_alpha(a):    
    import re   
    out=''    
    s=re.split('([\d]+)',a)   
    print(s) 
    for i in s:   
        if i.isalpha():   
           out+=i[::-1]    
        else:   
            out+=i   
        
    print(out)      
reverse_alpha('0PIKA123CHU456') 
