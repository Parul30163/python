# Gradient Descent in ML

#Gradient Descent in ML

#we know that  equation of simple line =y=mx+b

#we know that 

#loss function =Actual_ valur - Predicted_value

#loss with respect to mean squared error

#l=1/n(y_actual_y_predicted)**2

#if n(features)=1

#l=(y-mx-b)**2

#Case-1 loss w.r.t. intercept(b)


#dl/db= 2(y-mx-b)(d(y)/db - d(mx)/db - db/db)

#dl/db= 2(y-mx-b) (0-0-1)

#dl/db = -2(y-mx-b)..............(1)


#b_new =b_old -learning_rate * (dl/db).....(3)

#m_new=m_old -learning_ rate *(dl/dm).......(4)

#from equation(3,4) newline will bw

#y= m_new*X =b_new .......(5)

#if learning_rate >>>>0 then it will be GradientExploading

#if learning_rate <<<<0 then it will be Vanishing Gradient



import numpy as np

from sklearn.datasets import make_regression
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.model_selection import cross_val_score

X,y =make_regression(n_samples=100 ,n_features=1,
                    n_informative =1 ,n_targets=1 , noise =20 ,random_state=13)

plt.scatter(X,y)

from sklearn.model_selection import train_test_split
X_train,X_test ,y_train, y_test =train_test_split(X,y,test_size =0.2 , random_state=42)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(X_train,y_train)
print(lr.coef_)
print(lr.intercept_)


# np.mean(cross_val_score(lr,X,y,scoring ='r2',cv=10))
y_pred =lr.predict(X_test)
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

class GDRegressor:
    def __init__ (self,learning_rate,epochs):
        self.m=100 # we ca start any no. as  like m=0
        self.b=-120 # we ca start any no. as  like b=0
        self.lr =learning_rate
        self.epochs=epochs
            
    def fit (self,X,y):
        #calculate the b using GD
        for i in range (self.epochs):
            loss_slope_b =-2*np.sum(y-self.m*X.ravel()-self.b)
            loss_slope_m =-2*np.sum((y-self.m*X.ravel()-self.b) *X.ravel() )
            
            self.b=self.b -(self.lr *loss_slope_b)
            self.m=self.m -(self.lr *loss_slope_m)
        print(self.b ,self.m)
    def predict (self,X):
        return self.m *X+ self.b
        

gd =GDRegressor(0.001,100)

gd.fit(X_train,y_train)

#gd.predict

y_pred=gd.predict (X_test)
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

# gradient(stocastic)decent `

from  sklearn.datasets import load_diabetes
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

X,y=load_diabetes (return_X_y =True)
print(X.shape)
print(y.shape)


X_train,X_test ,y_train ,y_test =train_test_split(X,y,test_size =0.2,random_state=42)

reg=LinearRegression()
reg.fit(X_train,y_train)

y_pred=reg.predict(X_test)
r2_score(y_test,y_pred)

#now we create our own class
class SGDRegressor:
    def __init__ (self,learning_rate =0.01 ,epochs=100):
        self.coef_= None
        self.intercept_ =None
        self.lr =learning_rate
        self.epochs=epochs
        
    def fit(self ,X_train ,y_train):
        #init our coef
        self.intercept_ =0
        self.coef_ =np.ones(X_train.shape[1])
        
        for i in range( self .epochs):
            for j in range (X_train.shape[0]):
                idx=np.random.randint(0,X_train.shape[0])
                
                y_hat =np.dot (X_train[idx],self.coef_)+self.intercept_
                
                intercept_der =-2*(y_train[idx]-y_hat)
                self.intercept_=self.intercept_-(self.lr*intercept_der)
                
                coef_der =-2*np.dot((y_train[idx]-y_hat),X_train[idx])
                self.coef_=self.coef_ -(self.lr*coef_der)
                
        print(self.intercept_ ,self.coef_)
    def predict (self ,X_test)    :
        return np.dot(X_test,self.coef_)+self.intercept_

sgd=SGDRegressor (learning_rate =0.01,epochs=50)


sgd.fit(X_train,y_train)

y_pred =sgd.predict(X_test)

r2_score(y_test,y_pred)

