* https://www.analyticsvidhya.com/blog/2016/01/guide-data-exploration/?utm_content=bufferfde7a&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer

# Below are the steps involved to understand, clean and prepare your data for building your predictive model:

Variable Identification
Univariate Analysis
Bi-variate Analysis
Missing values treatment
Outlier treatment
Variable transformation
Variable creation
 and then iteration 4 to 7 times
 
 Variable identification 
 
 * Type of variable---predector & targets 
 * Data type--- character or numeric           
 * Variable category --- catogrical or continous 
 
# Univariate Analysis

methods and statistical measures for categorical and continuous variables individually:
 
Continuous Variables:- central tendency (mean,mode,median) or spread  of variable or dispersion (Range,IQR,Variance,sd,kurtossis & skweness) vizualisation (box,histogram)

 used to highlight missing and outlier values.
 
 # Bi-variate Analysis
 
 relationship between two variables
Here, we look for association and disassociation between variables at a pre-defined significance level. We can perform bi-variate analysis for any combination of categorical and continuous variables. The combination can be: Categorical & Categorical, Categorical & Continuous and Continuous & Continuous. Different methods are used to tackle these combinations during analysis process.
* Continuous & Continuous: 
Scatter plot shows the relationship between two variable but does not indicates the strength of relationship amongst them. To find the strength of the relationship, we use Correlation. Correlation varies between -1 and +1.

-1: perfect negative linear correlation
+1:perfect positive linear correlation and 
0: No correlation
Correlation can be derived using following formula:

Correlation = Covariance(X,Y) / SQRT( Var(X)* Var(Y))

* Categorical & Categorical:
To find the relationship between two categorical variables, we can use following methods:

Two-way table: 

Stacked Column Chart:

Chi-Square Test: used to derive the statistical significance of relationship between the variables. 

Chi-square is based on the difference between the expected and observed frequencies in one or more categories in the two-way table.

It returns probability for the computed chi-square distribution with the degree of freedom.

Probability of 0: It indicates that both categorical variable are dependent

Probability of 1: It shows that both variables are independent.

Probability less than 0.05: It indicates that the relationship between the variables is significant at 95% confidence. 

Statistical Measures used to analyze the power of relationship are:

Cramer’s V for Nominal Categorical Variable
Mantel-Haenszed Chi-Square for ordinal categorical variable.

* Categorical & Continuous:
While exploring relation between categorical and continuous variables, we can draw box plots for each level of categorical variables. If levels are small in number, it will not show the statistical significance. To look at the statistical significance we can perform Z-test, T-test or ANOVA.

Z-Test/ T-Test:- Either test assess whether mean of two groups are statistically different from each other or not.

If the probability of Z is small then the difference of two averages is more significant. The T-test is very similar to Z-test but it is used when number of observation for both categories is less than 30

ANOVA:- It assesses whether the average of more than two groups is statistically different.

# Missing Value Treatment

Why missing values treatment is required?

Missing data in the training data set can reduce the power / fit of a model or can lead to a biased model because we have not analysed the behavior and relationship with other variables correctly. It can lead to wrong prediction or classification.

methods to treat missing values ?

deletion :  two types: List Wise Deletion and Pair Wise Deletion.

In list wise deletion, we delete observations where any of the variable is missing. Simplicity is one of the major advantage of this method, but this method reduces the power of model because it reduces the sample size.

In pair wise deletion, we perform analysis with all cases in which the variables of interest are present. Advantage of this method is, it keeps as many cases available for analysis. One of the disadvantage of this method, it uses different sample size for different variables.

Mean/ Mode/ Median Imputation: 
It consists of replacing the missing data for a given attribute by the mean or median (quantitative attribute) or mode (qualitative attribute) of all known values of that variable. It can be of two types:-
Generalized Imputation: In this case, we calculate the mean or median for all non missing values of that variable then replace missing value with mean or median. Like in above table, variable “Manpower” is missing so we take average of all non missing values of “Manpower”  (28.33) and then replace missing value with it.

Similar case Imputation: In this case, we calculate average for gender “Male” (29.75) and “Female” (25) individually of non missing values then replace the missing value based on gender. For “Male“, we will replace missing values of manpower with 29.75 and for “Female” with 25.

Prediction Model:



