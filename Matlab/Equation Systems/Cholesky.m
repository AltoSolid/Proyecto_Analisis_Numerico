% FACTORING CHOLESKY
%This program results in systems of equations
%using Cholesky factorization

A=input('Enter matrix A = \n');
b=input('\nEnter the vector b, corresponding to the independent terms b =\n');
%Matrices A and b should be entered in square brackets, separating the
%Columns by comma ',' and rows by semicolon ';'

[n,m]=size(A);
%C=[A,b];
%Matrix [Ab]
%disp(C)
if n==m    
    for k=1:n
        add1=0;
        for p=1:k-1
            add1=add1+L(k,p)*u(p,k);
        end
        L(k,k)=sqrt(A(k,k)-add1);
        u(k,k)=L(k,k); 
        for i=k+1:n
            add2=0;
            for q=1:k-1
                add2=add2+L(i,q)*u(q,k);
            end
            L(i,k)=(A(i,k)-add2)/L(k,k);
        end
        for j=k+1:n
            add3=0;
            for r=1:k-1
                add3=add3+L(k,r)*u(r,j);
            end
            u(k,j)=(A(k,j)-add3)/L(k,k);
        end
    end
    mult=det(L)*det(u)
    if mult~=0
        for i=1:n
            add=0;
            for p=1:i-1
                add=add+L(i,p)*z(p);
            end
            z(i)=(b(i)-add)/L(i,i); 
        end
        for i=n:-1:1
            add=0;
            for p=i+1:n
                add = add+u(i,p)*x(p);
            end
            x(i)=(z(i)-add)/u(i,i); 
        end   
    else
        fprintf('\nThe determinant is equal to zero\n')
    end
end
    %fprintf('\n Matrix Ab:\n')
    %disp(C)
    fprintf('\n Matrix L:\n')
    disp(L)
    fprintf('\n Matrix U:\n')
    disp(u)
    fprintf('\n Vector Z:\n')
    disp(z)
    
  fprintf('\n\nSolution:\n'); 
for i=1:n
    xi=x(1,i);
    fprintf('\nX%g=',i)
    disp(xi);
end
