import csv
from datetime import datetime

import matplotlib.pyplot as plt

FILENAME = 'data/new_york.csv'

with open(FILENAME) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            high = int(row[20])
            low = int(row[22])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    plt.style.use(style='default')
    fig, ax = plt.subplots(figsize=(24,16), dpi=128)
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    title = 'Daily highs and lows\nNew York, US'
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=16)
    plt.xlim(datetime(2014, 1, 1), datetime(2023, 12, 31))
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.savefig('img/new_york_highs_lows.png', bbox_inches='tight')

with open(FILENAME) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, avgs = [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            avg = int(row[18])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            avgs.append(avg)

    plt.style.use(style='default')
    fig, ax = plt.subplots(figsize=(24,16), dpi=128)
    ax.bar(dates, avgs)

    title = 'Avarage Temperature\nNew York, US'
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=16)
    plt.xlim(datetime(2000, 1, 1), datetime(2005, 6, 1))
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.savefig('img/new_york_avarage.png', bbox_inches='tight')
    