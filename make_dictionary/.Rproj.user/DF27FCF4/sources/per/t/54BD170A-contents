library(stringr)
library(magrittr)
test <- read.csv("dictionary.csv", stringsAsFactors = FALSE)

for (i in 1:nrow(test)) {
  a <- strsplit(test$Word[i], "") %>% as.data.frame() 
  test$Changed[i] <- as.character(a[,1]) %>% sort() %>% str_flatten() %>% tolower()
  print(i)
}

hyoa <- test[order(test$Changed),]
write.csv(hyoa, "master_dictionary.csv", row.names = FALSE)