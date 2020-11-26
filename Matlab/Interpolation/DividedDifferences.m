This program is to find the interpolating polynomial that passes through some given points
%with the method of divided differences.

function DividedDifferences
    %load('Test.mat');
    X=vectorx();
    x=X(:,1);
    [n,m]=size(X);
    D=zeros(n,n);
    D(:,1)=X(:,2);
    for  j=2:n
      for i=1:(n-j+1)
        D(i,j)=(D(i+1,j-1)-D(i,j-1))/(x(i+j-1)-x(i));
      end
    end
    disp(D);
end