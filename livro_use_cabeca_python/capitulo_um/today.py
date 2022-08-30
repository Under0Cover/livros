from datetime import datetime

hoje = datetime.today()

if hoje == 'Saturday':
    print ('Party')
elif hoje == 'Sunday':
    print ('Recover')
else:
    print ('Work, work, work')
