
'''

     delay - ваше время (от и до) перерыва между кошельками
     mode  -  0 - ваши сети (из и в какую) ; 1 - поиск нфт по наличию в сети и отправка в выбранную вами сеть

     avax   /   bsc   /   polygon

     chain - из какой сети
     to - в какую из сетей (выбирается рандомно) - random.choice(['avax','polygon']) либо в конккретную сеть - просто имя сети 'avax'

    '''

delay = (10, 600)
mode = 1
chain = 'bsc'          #   avax   /   bsc   /   polygon
to = 'avax'     #random.choice(['ваша сеть','ваша сеть'])

info = {'avax':('https://snowtrace.io/tx/','https://rpc.ankr.com/avalanche'),
        'polygon':('https://polygonscan.com/tx/','https://polygon-rpc.com'),
        'bsc':('https://bscscan.com/tx/','https://bscrpc.com')}