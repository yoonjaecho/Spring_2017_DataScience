setwd('/Users/yoonjae/Desktop/DataScience/Week3')
# wd = getwd()
rm(list=ls())

# edit(var)

library(ggplot2)
library(ggmap)
library(extrafont)
library(scales)

tashu <- read.csv('./Data/tashu.csv')
station <- read.csv('./Data/station.csv', encoding = "UTF-8")

tashu$RENT_DATE <- strptime(tashu$RENT_DATE, "%Y%m%d%H%M%S")
tashu$RETURN_DATE <- strptime(tashu$RETURN_DATE, "%Y%m%d%H%M%S")

kiosk_station_map <- station$명칭
names(kiosk_station_map) <- c(station$키오스크번호)

rent_station_cnt <- data.frame(tashu$RENT_STATION)
colnames(rent_station_cnt) <- c("station_cnt")
return_station_cnt <- data.frame(tashu$RETURN_STATION)
colnames(return_station_cnt) <- c("station_cnt")
station_cnt <- data.frame(table(rbind(rent_station_cnt, return_station_cnt)))
colnames(station_cnt) <- c("kiosk","count")

sorted_station_cnt <- station_cnt[order(-station_cnt$count),]
top10_station_cnt <- head(sorted_station_cnt, 10)

top10_df <- data.frame(
  kiosk = c(top10_station_cnt$kiosk),
  usage = c(top10_station_cnt$count),
  name = kiosk_station_map[top10_station_cnt$kiosk]
)
rownames(top10_df) <- 1:nrow(top10_df)

colors = c(
  "#cdbbe0",
  "#c7e5bb",
  "#e6bbcc",
  "#92c7b4",
  "#e5b6a5",
  "#9edce6",
  "#d5c9a0",
  "#a9c4e1",
  "#dbe6d5",
  "#b1beaf")

barplot(top10_df$usage, main="Top 10 Station", xlab="Station #", ylab="Usage", ylim=c(0,350000),
        names.arg=c(top10_df$kiosk), col=colors)

theme_set(theme_bw(base_family = "NanumGothicOTF"))

ggplot(top10_df, aes(x = as.factor(kiosk), y = usage, fill=as.factor(kiosk))) + 
  geom_bar(stat='identity') +
  xlab("Station Number") +
  ylab("Usage") +
  ggtitle("Top 10 Station") +
  scale_fill_discrete(name = "Station Name", labels=top10_df$name) +
  scale_y_continuous(labels=comma)

