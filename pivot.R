library(readr)
library(tidyverse)
library(tidyr)
country_temp <- read_csv("temp_long.csv")
View(country_temp)
temps <- pivot_longer(country_temp, 2:14 ,names_to="Observations", values_to="Temp")
View(temps)

write.csv(temps,"final_temps.csv")


