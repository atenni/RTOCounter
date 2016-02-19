#!/usr/bin/env python3

from collections import Counter
import csv
import datetime
# from datetime import date
# from datetime import datetime


# PARAMETERS
START_DATE = datetime.date(year=1970, month=1, day=1)
csv_date_format = "%d-%b-%y"


def parse_date(date_string, is_start_date):
    try:
        date = datetime.datetime.strptime(
                date_string,
                csv_date_format).date()
    except ValueError as e:
        # Date is missing in the CSV. Set to a large/small date to preserve
        # desired behaviour in `if start_date <= date < end_date` below.
        if is_start_date:
            year = 9999
        else:
            year = 1900

        date = datetime.date(year, 1, 1)
    return date


def main(csv_file):
    date_range = [START_DATE.replace(year=year)
                  for year
                  in range(START_DATE.year, datetime.date.today().year + 1)]
    year_list = []  # List of years each RTO was active

    reader = csv.DictReader(csv_file)
    for row in reader:
        # Parse date strings
        start_date = parse_date(
                row['Start Date'],
                is_start_date=True)
        end_date = parse_date(
                row['End Date'],
                is_start_date=False)

        for date in date_range:
            if start_date <= date < end_date:
                year_list.append(date.year)

    year_counter = Counter(year_list)

    with open('RTO_yearly_counts.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Year", "Number of current RTOs"])
        for key, count in year_counter.items():
            writer.writerow([key, count])


if __name__ == "__main__":
    with open('RtoList.csv', 'r') as csv_file:
        main(csv_file)
