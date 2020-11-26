% FACTORIZACION DOOLITTLE
%This program results in systems of equations
%using Doolittle factorization

A=input('Enter matrix A = \n');
b=input('\nEnter the vector b, corresponding to the independent terms b =\n');
%Matrices A and b should be entered in square brackets, separating the
%Columns by comma ',' and rows by semicolon ';'

[n,m]=size(A);
%C=[A,b];
%disp(C)
if n==m
    for k=1:n
        L(k,k)=1;
        add=0;
        for p=1:k-1
            add=add+L(k,p)*u(p,k);
        end
        u(k,k)=(A(k,k)-add);
        for i=k+1:n
            add=0;
            for r=1:k-1
                add=add+L(i,r)*u(r,k);
            end
            L(i,k)=(A(i,k)-add)/u(k,k); 
        end
        for j=k+1:n
            add=0;
            for s=1:k-1
                add=add+L(k,s)*u(s,j);
            end
            u(k,j)=(A(k,j)-add);
        end
    end
    mU=1; 
    mL=1;
    for i=1:n
        mU=mU*u(i,i);
    end
    mult=mL*mU;  
    
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
            for p=(i+1):n
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
