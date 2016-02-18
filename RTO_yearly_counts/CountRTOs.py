#!/usr/bin/env python3

from collections import Counter
import csv
import datetime
# from datetime import date
# from datetime import datetime


# PARAMETERS
START_DATE = datetime.date(year=1970, month=1, day=1)
csv_date_format = "%d-%b-%y"


def main(csv_file):
    date_range = [START_DATE.replace(year=year)
                  for year
                  in range(START_DATE.year, datetime.date.today().year + 1)]
    year_list = []  # List of years each RTO was active

    reader = csv.DictReader(csv_file)
    for row in reader:
        # Parse date strings
        try:
            start_date = datetime.datetime.strptime(row['Start Date'], csv_date_format)
            start_date = start_date.date()
        except ValueError as e:
            # Start date is missing in the CSV. Set to a large date to preserve
            # desired behaviour in `if start_date <= date < end_date` below.
            start_date = datetime.date(9999, 1, 1)

        try:
            end_date = datetime.datetime.strptime(row['End Date'], csv_date_format)
            end_date = end_date.date()
        except ValueError as e:
            # End date is missing in the CSV. Set to a low date to preserve
            # desired behaviour in `if start_date <= date < end_date` below.
            end_date = datetime.date(1900, 1, 1)

        for date in date_range:
            if start_date <= date < end_date:
                year_list.append(date.year)

    year_counter = Counter(year_list)

    with open('RTO_yearly_counts.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Year", "Number of current RTOs"])
        for key, count in year_counter.items():
            writer.writerow([key, count])


if __name__ == "__main__":
    with open('RtoList.csv', 'r') as csv_file:
        main(csv_file)
