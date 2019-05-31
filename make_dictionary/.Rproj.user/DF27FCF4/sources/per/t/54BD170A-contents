library(stringr)
library(magrittr)
test <- read.csv("dictionary.csv", stringsAsFactors = FALSE)
hyoa_test <- read.csv("master_dictionary_nonU.csv", stringsAsFactors = FALSE)
score <- read.csv("some.csv", stringsAsFactors = FALSE, header = FALSE)

for (i in 1:nrow(test)) {
  a <- strsplit(test$Word[i], "") %>% as.data.frame() 
  test$Changed[i] <- as.character(a[,1]) %>% sort() %>% str_flatten() %>% tolower()
  print(i)
}

hyoa <- test[order(test$Changed),]
write.csv(hyoa, "master_dictionary_nonU.csv", row.names = FALSE)

score_test <- gather(score)
score_test <- score_test$value
master <- cbind(hyoa_test, score_test)
write.csv("comp_dictionary.csv", master, row.names=false)