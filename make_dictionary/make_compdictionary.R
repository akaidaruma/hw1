df <- read.csv("comp_dictionary.csv", stringsAsFactors = FALSE) 
df <- df[order(df$score_test, decreasing=T),]
write.csv(df, "dictionary_forhw.csv", row.names = FALSE)