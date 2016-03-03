# Create dataframe of RTO data, sort by start date from oldest to newest
RtoList <- read.csv("RtoList.csv")
RtoList$Start.Date = as.Date(RtoList$Start.Date, "%d-%b-%y")
RtoList$End.Date = as.Date(RtoList$End.Date, "%d-%b-%y")
RtoList = RtoList[order(RtoList[,4],decreasing=FALSE),)]
RtoList$Name = tolower(RtoList$Name)

# See what we've got
summary(RtoList)

# Calc relative frequency of RTOs by RCAB code
rcabs <- RtoList$RCAB
rcabs.freq=table(rcabs)
rcabs.relfreq=rcabs.freq/nrow(RtoList)
plot(rcabs)

# Create histogram of start and end dates
hist(RtoList$Start.Date, "years", freq=TRUE)
hist(RtoList$End.Date, "years", freq=TRUE)

# Get number of current RTOs
current_RTOs <- function(rto_frame)
{
    rto_frame$Start.Date
    rto_frame$End.Date
    rto_frame$Status
}
