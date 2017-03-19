setwd('/Users/yoonjae/Desktop/DataScience/Week3')
# wd = getwd()
rm(list=ls())

# edit(var)



library(ggplot2)
library(ggmap)
library(extrafont)
library(scales)
library(data.table)
library(stringr)

tashu <- read.csv('./Data/tashu.csv')
station <- read.csv('./Data/station.csv', encoding = "UTF-8")

tashu$RENT_DATE <- strptime(tashu$RENT_DATE, "%Y%m%d%H%M%S")
tashu$RETURN_DATE <- strptime(tashu$RETURN_DATE, "%Y%m%d%H%M%S")

kiosk_station_map <- station$명칭
names(kiosk_station_map) <- c(station$키오스크번호)

latlan <- str_split_fixed(station$좌표, ",", 2)
lat_map <- latlan[,1]
names(lat_map) <- c(station$키오스크번호)
lan_map <- latlan[,2]
names(lan_map) <- c(station$키오스크번호)

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

station_df <- data.frame(
  usage = c(station_cnt$count),
  lat = as.numeric(lat_map[station_cnt$kiosk]),
  lon = as.numeric(lan_map[station_cnt$kiosk])
)

theme_set(theme_gray(base_family = "NanumGothicOTF"))

top10_station_bar_graph <- ggplot(top10_df, aes(x = as.factor(kiosk), y = usage, fill=as.factor(kiosk))) + 
  geom_bar(stat='identity') +
  xlab("Station Number") +
  ylab("Usage") +
  ggtitle("Top 10 Station") +
  scale_fill_discrete(name = "Station Name", labels=top10_df$name) +
  scale_y_continuous(labels=comma) +
  theme(plot.title = element_text(hjust = 0.5))

top10_station_bar_graph



daejon_gc <- geocode("Daejon")
daejon_cent <- as.numeric(daejon_gc)

tashu_map <- ggmap(get_googlemap(center = daejon_cent, scale = 1, maptype = "roadmap", zoom = 13)) +
  geom_point(data = station_df, aes(x = lon, y = lat, size = usage), alpha = .7, colour = '#FF3232') +
  theme(legend.position="none") +
  xlab("위도") +
  ylab("경도") + 
  ggtitle("Tashu 정류장 별 사용 빈도(∝점의 크기)") +
  theme(plot.title = element_text(hjust = 0.5))

tashu_map





