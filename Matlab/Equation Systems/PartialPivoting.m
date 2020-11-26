%GAUSSIAN ELIMINATION WITH PARTIAL PIVOTING (STEP-BY-STEP SOLUTION)
%This program results in systems of equations
%using the Gaussian elimination method with partial pivoting

A=input('Enter matrix A = \n');
b=input('\nEnter the vector b, corresponding to the independent terms b =\n');
%Matrices A and b should be entered in square brackets, separating the
%Columns by comma ',' and rows by semicolon ';'

[n,m]=size(A);
C=[A,b];
disp(C)
if n==m 
    for k=1:(n-1)
        fprintf('\n Step %g=\n\n',k)
        major=0;
        rowm=k; 
        for p=k:n
            if major<abs(C(p,k))
                major=abs(C(p,k));
                rowm=p; 
            end
        end
        if major ==0
            fprintf('\nThe system has infinite solutions\n')
            break 
        else
            if rowm ~= k 
            for j=1:(n+1)
                aux=C(k,j); 
                C(k,j)=C(rowm,j);
                C(rowm,j)=aux;
            end
            end
        end
        fprintf('\nThe matrix corresponding to this step before the process:\n')
         
         disp(C)
         fprintf('\nThe multipliers at this step are:\n')
         for i=(k+1):n
            m(i,k)=C(i,k)/C(k,k); 
            fprintf('\nm(%g,%g)=',i,k)
            disp(m(i,k));
            for j=k:(n+1)
                C(i,j)= C(i,j) - m(i,k)*C(k,j);
            end
         end
         fprintf('\nThe matrix corresponding to this step after the process:\n')
         
         disp(C)
    end
         for i=n:-1:1
            add=0;
               for p=(i+1):n
                add = add + C(i,p)*X(p);
               end
            X(i)=(C(i,n+1)-add)/C(i,i);
         end
else 
     fprintf('\nERROR: the matrix is not square(nxn)\n');
end
fprintf('\n\n SOLUTION:\n');
fprintf('\n\nMatrix Ab:\n');
disp(C)
fprintf('\n\nSolution:\n');
for i=1:n
    Xi=X(1,i);
    fprintf('\nX%g=',i)
    disp(Xi);
end

       
            
        
               