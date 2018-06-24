setwd("D:/CBA/Practicum/Practicum_1")

Cities <- read.csv("CitySentiment.csv")

anova <- aov(Cities$Compounded_polarity ~ Cities$City)
summary(anova)
anova

plot(Cities$Compounded_polarity ~ Cities$City)

Dhoni <- read.csv("DhoniSentiment.csv")

anova <- aov(Dhoni$Compounded_polarity ~ Dhoni$City)
summary(anova)
anova

plot(Dhoni$Compounded_polarity ~ Dhoni$City)
