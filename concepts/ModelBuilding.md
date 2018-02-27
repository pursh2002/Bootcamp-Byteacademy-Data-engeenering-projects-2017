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
