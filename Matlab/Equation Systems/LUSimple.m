%LU factorization method with Gaussian elimination
%to solve systems of equations.

function LU_SIMPLE(A,b)
fileID = fopen('LUsimple.txt','w');
[n,m]=size(A);
[N,H]=size(b);
if m~=n
    error1=["Error","the matrix is not square(nxn)"];
    Error1=table(error1);
    writetable(Error1,"LU_SIMPLE.xlsx")
    return
end
if det(A)==0
    error1=["Error","det(a) =  0"];
    Error1=table(error1);
    writetable(Error1,"LU_SIMPLE.xlsx")
    return
end
if m~=N
    error1=["Error", "A and b do not match"];
    Error1=table(error1);
    writetable(Error1,"LU_SIMPLE.xlsx")
    return
end
xlswrite('LU_SIMPLE.xlsx',b,'hoja1','A1');
xlswrite('LU_SIMPLE.xlsx',A,'hoja1','c1');
C=[A,b];
L=eye(n);
fprintf(fileID,'SOLUTION\n');
fprintf(fileID,'%d %d %d %d\n', A);
if n==m
    d=diag(C);
    for k=1: n-1
        for i=1:m
            if (d(i) == 0)
                return
            end
        end
        if A(k,k)~=0
            for i=(k+1):n
                m(i,k)=A(i,k)/A(k,k);
                for j=k:n
                    A(i,j)= A(i,j) - m(i,k)*A(k,j);
                    if i>j
                        L(i,j)= m(i,k);
                    end
                    if i==j
                        L(i,j)= 1;
                    end
                    if i<j
                        L(i,j)= 0;
                    end
                    
                end
                
            end
        end
        fprintf(fileID,'Stage ');
        fprintf(fileID,'\n',i);
        fprintf(fileID,'%d %d %d %d\n', m);
        fprintf(fileID,'L:\n');
        fprintf(fileID,'%d %d %d %d\n', L);
        fprintf(fileID,'U:\n');
        fprintf(fileID,'%d %d %d %d\n', m);
    end
end
xlswrite('LU_SIMPLE.xlsx',L,'L','A1');
xlswrite('LU_SIMPLE.xlsx',A,'U','A1');
fclose(fileID)
end