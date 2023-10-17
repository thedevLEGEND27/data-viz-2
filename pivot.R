library(readr)
library(tidyverse)
library(tidyr)
country_temp <- read_csv("country temp.csv")
View(country_temp)

temps <- t(country_temp)
View(temps)

write.csv(temps, "correct temps.csv", row.names=TRUE)


