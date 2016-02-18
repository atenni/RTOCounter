# RTO Counter
A quick Python script to parse available public data in order to generate a time series of current Australian RTOs.

## Steps to raw data (as of 19/Feb/2016):

1.  Go to <http://training.gov.au/Reporting>, expand the *RTO reports* section, and click on *RTO List*.
2.  Select all past and present Regulatory bodies and all Registration status',
    tick *Include Legacy Data*, but leave *Expire Date* blank.
3.  View the report. This will be a list of all historical RTO's in Australia with registration start and end dates.
4.  Save the report as an Excel file via the icons at the top of the page (it should be about 11,000 rows).
5.  Clean up the .xlsx file by unmerging cells, saving as a .csv, and removing superfluous leading rows and empty columns.

You should now have a .csv file in a similar format to:

RCAB | Code | Name | Start Date | End Date | Status
---- | ---- | ---- | ---------- | -------- | ------
TVET | 1 | Office of the Student Identifiers Registrar | 5-Nov-14 | | Current
NSW VETAB | 20 | Tourism Training Australia | 1-Jan-98 | 28-May-02 | Non-Current
ASQA | 22 | Adelaide Training and Employment Centre Inc | 28-Oct-13 | 27-Oct-18 | Current
etc... | | | | |

Then for any given date, if a particular RTO's start and end dates encompass that date, the RTO would have been current
at that time.

The file `CountRTOs.py` iterates through each row checking the start and end dates, and increments a "year-counter"
for each year that particular RTO was current. This creates a list of [year]: [number of current RTOs] for each year, which
is written to an `RTO_yearly_counts.csv` file in the same directory.
