data = read.csv("new.csv")
data = data[-7]
write.csv(data, "data.csv", row.names = FALSE)