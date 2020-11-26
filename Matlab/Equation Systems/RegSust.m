%The following program performs regressive substitution to the matrix
%Increased M=[U,b]

function x=sustregr(M)
n=size(M,1);
x=zeros(n,1);
x(n)=M(n,n+1)/M(n,n);
for i=n-1:-1:1
    aux=[1 x(i+1:n)];
    aux1=[M(i,n+1) -M(i,i+1:n)];
    x(i)=dot(aux,aux1)/M(i,i);
end
end