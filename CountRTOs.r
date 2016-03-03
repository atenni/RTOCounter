library("ggplot2")

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
plot(rcabs)  # TODO: find built-in or library for this

# Create histogram of start and end dates
startplot = hist(RtoList$Start.Date, "years", freq=TRUE)
endplot = hist(RtoList$End.Date, "years", freq=TRUE)
plot(startplot, col=rgb(0,0,1,1/4))
plot(endplot, col=rgb(1,0,0,1/4), add=TRUE)

# Get number of current RTOs
current_RTOs <- function(rto_frame)
{
        # do the count here
        '
        histogram of RTOs where status is current
        apply a mask or filter to:
        hist(RtoList$Start.Date)
        subset(rto_frame, rto_frame$Status == "Current")
        OR
        qplot(rto_frame.Start$Date - rto_frame.End$Date, geom="histogram")
        '
        qplot(rto_frame$Start.Date, geom="histogram", binwidth=250,
            fill=I("blue"), alpha=I(0.25))
}
