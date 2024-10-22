import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        dt = datetime.datetime.now()
        writer.writerow([line, dt.second, dt.microsecond])

time.sleep(0.01)