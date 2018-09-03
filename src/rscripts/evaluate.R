library(lubridate)
library(dplyr)
library(ggplot2)
library(forecast)
library(prophet)

setwd('/Users/matbrunt/sandbox/time-series-sandbox/src/rscripts')

fetch_data <- function(filename) {
  path <- paste('../data/external/', filename, sep = "")
  data <- read.csv(path, stringsAsFactors = FALSE)
  data$Month <- parse_date_time(data$Month, orders = "ym")
  df <- ts(data$X.Passengers, frequency = 12, start=c(1949,1))
  return(df)
}
df <- fetch_data('AirPassengers.csv')
train <- window(df, end=c(1959,12))
test <- window(df, start=c(1960, 1))

models = list(
  mod_arima = auto.arima(train, ic='aicc', stepwise = FALSE),
  mod_exp = ets(train, ic='aicc', restrict = FALSE),
  mod_naive = naive(train, 12)
)

forecasts <- lapply(models, forecast, 12)
par(mfrow=c(4, 2))
for(f in forecasts) {
  plot(f)
  lines(test, col='red')
}

acc <- lapply(forecasts, function(f) {
  accuracy(f, test)[2,,drop=FALSE]
})
acc <- Reduce(rbind, acc)
row.names(acc) <- names(forecasts)
acc <- acc[order(acc[,'MASE']),]
round(acc, 2)
