Principal Component Analysis is one of the most frequently used concept in data science for dimensionality reduction.

Here is a simple visual explanation of the eigenvalues and eigenvector(first principal component)

Blue dots: the initial data on a 2D space
Red dots: the projection of the blue dots onto lines, that are centered at the mean of the data.
There many, many such lines. Notice how the red dots are dispersed (spread out) on the rotating line in 
different ways depending on the position of the line (=vector): on some lines the red dots have great dispersion 
compared to other positions of the line.First Principal Component - Eigenvector: That particular position of the rotating 
line (=vector)-shown in purple-where the red dots (projection of the original blue data) have the biggest dispersion 
(have the biggest spread out) than any other line i.e. have the greatest variance on the rotating line.

Eigenvalue: the actual variance of the red dots on that line.

Let's say the eigenvalue(explained_variance_ in sklearn) is 80%.
It means that if you project all your data to that line, you will be able to reconstruct the points with 80% of 
accuracy with using only one dimension. Source: bit.ly/2nd1XeP

* by paul

Principal Component Analysis (PCA) is familiar to most analysts. There are many variants of PCA that have been published to-date. NCR-PCA (non-convex robust PCA) is one of those. The authors' paper[1] & Matlab code [2] are available for keen learners to explore. 

PCA :
- removes redundancy by transforming the data into an orthogonal lower dimensional space
- captures as much variation in the data as possible
- retained PCs is equal to or less than number of original variables

The authors of[1] claimed that their NCR-PCA is:
- robust to noise in the data
- has provable global convergence guarantees
- low computational complexity which leads to faster computation & have more accurate recovery against other state of the art baselines

NCR-PCA is dependent on a second package, the PROPACK (https://lnkd.in/gNT_jXN) which contains a set of functions for computing the SVD (singular value decomposition) of large and sparse or structured matrices. The authors of NCR-PCA had already mexed compile PROPACK, but in case there's a problem in running the 3 demos (see files with 'synthetic_vary_...') in your system, then try re-mex compiling the C & Fortran codes in PROPACK.

[1]" Non-Convex Robust PCA " (PDF)
https://lnkd.in/gX2ksfe

[2]" NCR-PCA Matlab Code " (Zip)
https://lnkd.in/grgPgtJ

https://medium.com/@aptrishu/understanding-principle-component-analysis-e32be0253ef0

https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60
