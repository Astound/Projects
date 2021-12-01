from plyer import notification
import pandas as pd
import time
f1='Vocab_advanced_2010.xlsx'

read1=pd.read_excel(f1,sheet_name='Sheet1')
words=list(read1['FORMS'])
ex=list(read1['EXAMPLES'])

while True:
    for i in range(1,420):
        notification.notify(
            title= "Word today: "+words[i],
            message= ex[i],
            app_icon="book.ico",
            timeout=2
        )
        time.sleep(60)


