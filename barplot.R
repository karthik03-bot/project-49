temperature <- c(28, 35, 31, 40, 29, 41, 42)
days <- c("Sun", "Mon", "Tues", "Wed", 
          "Thurs", "Fri", "Sat")
barplot(temperature, main = "Maximum Temperatures 
        in a Week",
        xlab = "Days", 
        ylab = "Degree in Celcius",
        names.arg= days,
        col = "darkred")
