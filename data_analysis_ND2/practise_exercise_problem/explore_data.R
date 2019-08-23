install.packages('ggplot2')
library('ggplot2')
qplot(data=diamonds,x=carat,y=price,xlim=c(0,diamonds$carat,0.99),ylim = c(0,quantile(diamonds$price,0.99)))+geom_point(fill=I('#F79420'),color=I('black'),shape=21)
