import time

t = time.localtime()
                    


def input_data():
    print('enter 1 for checkin and 2 checkout')
    checkin_checkout = int(input('enter the option'))
    read_write = int(input('press 1 to read and 2 to write'))
    name = int(input('enter 1 for customer1,2 for customer2,3 for customer3,4 for customer4'))
    if name==1:
        if checkin_checkout==1:
            if read_write==1:
                with open('customer1.txt') as sfr:
                    sfr1=sfr.read()
                    print(sfr1)
            elif read_write==2:
                with open('customer1.txt','a') as sfw:
                    sfw.write(str(input('customer1 checking in, add details , name:, contact number:,and all that shit \n '+time.asctime(t))))
                    sfw.write('checking in \n')
                    sfw.write(time.asctime(t))
                    print('succesfully added')
        elif checkin_checkout==2:
                with open('customer1.txt', 'a') as sew:
                    sew.write('review \n')
                    sew.write(str(input('add review and get out \n'+time.asctime(t))))
                    sew.write('\n ckecking out \n')
                    sew.write(time.asctime(t))
                    print('succesfully added')
    

    if name==2:
        if checkin_checkout==1:
            if read_write==1:
                with open('customer2.txt') as sfr:
                    sfr1=sfr.read()
                    print(sfr1)
            elif read_write==2:
                with open('customer2.txt','a') as sfw:
                    sfw.write(str(input('customer2 checking in, add details , name:, contact number:,and all that shit \n'+time.asctime(t))))
                    sfw.write('checking in \n')
                    sfw.write(time.asctime(t))
                    print('succesfully added')
        elif checkin_checkout==2:
                with open('customer2.txt', 'a') as sew:
                    sew.write('review \n')
                    sew.write(str(input('add review and get out \n'+time.asctime(t))))
                    sew.write('\n ckecking out \n')
                    sew.write(time.asctime(t))
                    print('succesfully added')
    
    if name==3:
        if checkin_checkout==1:
            if read_write==1:
                with open('customer3.txt') as sfr:
                    sfr1=sfr.read()
                    print(sfr1)
            elif read_write==2:
                with open('customer3.txt','a') as sfw:
                    sfw.write(str(input('customer3 checking in, add details , name:, contact number:,and all that shit \n'+time.asctime(t))))
                    sfw.write('checking in \n')
                    sfw.write(time.asctime(t))
                    print('succesfully added')
        elif checkin_checkout==2:
                with open('customer3.txt', 'a') as sew:
                    sew.write('review \n' )
                    sew.write(str(input('add review and get out \n'+time.asctime(t))))
                    sew.write('\n ckecking out \n')
                    sew.write(time.asctime(t))
                    print('succesfully added')
    

    if name==4:
        if checkin_checkout==1:
            if read_write==1:
                with open('customer4.txt') as sfr:
                    sfr1=sfr.read()
                    print(sfr1)
            elif read_write==2:
                with open('customer4.txt','a') as sfw:
                    sfw.write(str(input('customer1 checking in, add details , name:, contact number:,and all that shit \n '+time.asctime(t))))
                    sfw.write('checking in \n')
                    sfw.write(time.asctime(t))
                    print('succesfully added')
        elif checkin_checkout==2:
                with open('customer4.txt', 'a') as sew:
                    sew.write('review \n')
                    sew.write(str(input('add review and get out \n'+time.asctime(t))))
                    sew.write('\n ckecking out \n')
                    sew.write(time.asctime(t))
                    print('succesfully added')
   


input_data()

