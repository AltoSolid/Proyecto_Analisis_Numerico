%GAUSSIAN ELIMINATION WITH TOTAL PIVOTING (STEP-BY-STEP SOLUTION)
%This program results in systems of equations
%using the Gaussian elimination method with total pivoting

A=input('Enter matrix A = \n');
b=input('\nEnter the vector b, corresponding to the independent terms b =\n');
%Matrices A and b should be entered in square brackets, separating the
%Columns by comma ',' and rows by semicolon ';'

[n,m]=size(A);
C=[A,b];
disp(C)
if n==m 
    for i=1:n
        mark(i)=i; 
    end
    for k=1:(n-1)
        fprintf('\n Step %g=\n\n',k)
        major=0; 
        rowm=k; 
        colm=k; 
        for p=k:n
            for r=k:n
                if major<abs(C(p,r)) 
                major=abs(C(p,r)); 
                rowm=p; 
                colm=r;
                end
            end
        end
         if major ==0
            fprintf('\nThe system has infinite solutions\n')
            break
           if rowm ~= k 
            for j=1:(n+1)
                aux=C(k,j);
                C(k,j)=C(rowm,j);
                C(rowm,j)=aux;
            end
           end
            if colm ~= k 
            for i=1:n
                aux=C(i,k);
                C(i,k)=C(i,colm);
                C(i,colm)=aux;
            end
            aux = mark(k);
            mark(k)= mark(colm);
            mark(colm)=aux;
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
     fprintf('\nMarks Vector:\n')
            mark(colm)=aux
     for i=n:-1:1
            add=0;
               for p=(i+1):n
                add = add + C(i,p)*X(p);
               end
            X(i)=(C(i,n+1)-add)/C(i,i);
     end
         for i=1:n
             for j=1:n
                 if mark(j)==i
                     k=j;
                 end
             end
             aux=X(k);
             X(k)=X(i);
             X(i)=aux;
             aux=mark(k);
             mark(k)=mark(i);
             mark(i)=aux;
         end
else
     fprintf('\nERROR: the matrix is not square(nxn)\n');
end
fprintf('\n\n SOLUTION:\n');
fprintf('\n\nMatrix Ab:\n');
C
fprintf('\n\nSolution:\n');
for i=1:n
    Xi=X(1,i);
    fprintf('\nX%g=',i)
    disp(Xi);
end
    
             
    