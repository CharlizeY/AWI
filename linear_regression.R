library(readxl)
Model_1_Database <- read_excel("Desktop/Model_1_Database.xlsx")
View(Model_1_Database) 


# model0-three parameters 
attach(Model_1_Database)
model0<-lm(logprice~database+logdim+medium)
summary(model0)


# model1-seven parameters (with two Instagram parameters, two indicator variables)
logFPP<-Model_1_Database$logFPP
model1<-lm(logprice~database+logdim+medium+logFPP+logIP+ArtfactsPresence+InsPresence)
summary(model1)


# model1.1-remove ourliers with extreme values of price/dimension
data<-subset(Model_1_Database, logdim>=5.99146454711 & logdim<=12.6115377536 & logprice>=4.60517018599 & logprice<=12.2060726455)
attach(data)
logFPP<-data$logFPP
model1.1<-lm(logprice~database+logdim+medium+logFPP+logIP+ArtfactsPresence+InsPresence)
summary(model1.1)


# model2.1-remove outliers with DFFITS outside the range of the cut-off points
plot(dffits(model1.1), 
     ylab = "Standardized dfFits", xlab = "Index", 
     main = paste("Standardized DfFits, \n critical value = 2*sqrt(7+1/87290) = +/-",
                  round(0.1,3))) 
# Critical Value divided by horizontal lines
abline(h = 0.01914665, col = "red", lty = 2)
abline(h = -0.01914665, col = "red", lty = 2)

# Select a reasonable cut-off point: e.g. set at 50%
# Build the model
Rdata <-subset(data,dffits > -0.02328588 & dffits < 0.02529570)
attach(Rdata)
logFPP<-Rdata$logFPP
model2.1<-lm(logprice~database+logdim+medium+logFPP+logIP+ArtfactsPresence+InsPresence)
summary(model2.1)

# Plot the Influential Obs by DFFIT
df<-dffits(model1.1)
plot(dffits(model1.1), pch="*", cex=2, main="Influential Obs by DFFIT")  
abline(h = 0.02192915, col="red")   
abline(h = -0.02047106, col="red")  
text(x=1:length(df), y=df, labels=ifelse(df>0.02192915, names(df),""), col="red", pos = 4)
text(x=1:length(df), y=df, labels=ifelse(df<(-0.02047106), names(df),""), col="red", pos = 4) 


# model2.2-remove outliers with Cook's distance greater than 4 times of the mean
cooksd <- cooks.distance(model1.1)
influential <- as.numeric(names(cooksd)[(cooksd > 4*mean(cooksd, na.rm=T))])
View(data[influential,])
Idata<-data[-influential,]
attach(Idata)
logFPP<-Idata$logFPP
model2.2<-lm(logprice~database+logdim+medium+logFPP+logIP+ArtfactsPresence+InsPresence)
summary(model2.2)


# model2.3-remove outliers with price per dimension outside the 1.5*IQR range
attach(Model_1_Database)
ppz<-price/dimensions
ppz[!is.finite(ppz)]<-0
summary(ppz)
FullData<-cbind(Model_1_Database,ppz)
NewData<-subset(FullData,ppz<0.6135+1.5*(0.6135-0.2169),ppz>0.2169-1.5*(0.6135-0.2169))
attach(NewData)
logFPP<-NewData$logFPP
model2.3<-lm(logprice~database+logdim+medium+logFPP+logIP+ArtfactsPresence+InsPresence)
summary(model2.3)                                 


# Cross Validation-split the data into training (80%) and test set (20%)
library(tidyverse)
library(caret)
set.seed(123)
training.samples <- Model_1_Database$price %>%
  createDataPartition(p = 0.8, list = FALSE)
train.data  <- Model_1_Database[training.samples, ]
test.data <- Model_1_Database[-training.samples, ]

# Build the model
model.Train <- lm(logprice~database+logdim+medium+logFPP+logIP+ArtfactsPresence+InsPresence, data = train.data)
summary(model.Train)

# Make predictions and compute the R2, Root Mean Square Error (RMSE) and Meam Absolute Error (MAE)
predictions <- model.Train %>% predict(test.data)
data.frame( R2 = R2(predictions, test.data$logprice),
            RMSE = RMSE(predictions, test.data$logprice),
            MAE = MAE(predictions, test.data$logprice))



# K-fold Cross Validation
set.seed(123)
train.control <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
# Train the model
model.Train2 <- train(logprice~database+logdim+medium+logFPP+logIP+ArtfactsPresence+InsPresence, data = Model_1_Database, method = "lm",
               trControl = train.control)
print(model.Train2)


## Neural Networks
# install.packages("neuralnet")
# Data<-as.data.frame(Model_1_Database,na.rm=TRUE)

# library(dplyr)
# data<-select(Data,logprice,logdim,ArtfactsPresence,InsPresence,logFPP,logIP)

## Apply min-max scale method to normalize the data before NN
# maxs <- apply(data, 2, max) 
# mins <- apply(data, 2, min)
# scaled <- as.data.frame(scale(data, center = mins, scale = maxs - mins))

## train-test split
# library(tidyverse)
# library(caret)
# set.seed(123)
# index <- scaled$logprice %>%
  # createDataPartition(p = 0.8, list = FALSE)
# train_<-scaled[index,]
# test_<-scaled[-index,]

## Run neuralnet with only quantitative variables
# library(neuralnet)
# f <- as.formula(paste("logprice ~ logdim + ArtfactsPresence + InsPresence + logFPP + logIP"))
# nn <- neuralnet(f,data=train_,hidden=10,linear.output=T,threshold=0.3)

## Predict values for test data and calculate the MSE
# predictions <- nn %>% predict(test_)
# pr.nn_<-predictions*(max(data$logprice)-min(data$logprice))+min(data$logprice)
# test.r<-(test_$logprice)*(max(data$logprice)-min(data$logprice))+min(data$logprice)
# data.frame( R2 = R2(pr.nn_, test.r),
            # RMSE = RMSE(pr.nn_, test.r),
            # MAE = MAE(pr.nn_, test.r))

# MSE.nn<-sum((test.r-pr.nn_))^2/nrow(test_)

