%This program finds the Vandermonde matrix

function Vandermonde()    
    mx=input("Values x in a file: "); 
    my=input("Values y in column: ") ;
    n=length(mx);
    A=zeros(n); 
    for i=1:n 
        for j=1:n 
            A(i,j)=mx(i)^(n-j);
        end
    end
    b=A\my; 
    b=Gauss_total_pivoting(A,my);
    disp('B: ');
    disp(b);
    polcoef=[]; 
    for i=1:n 
        polcoef(i,1)=(b(i,1)); 
    end
    T=table(A);
    disp(T);
    writetable(T,"VandermondeTable.xlsx")
    T=table(polcoef);
    disp(T);
    P = poly2sym(sym(polcoef));
    disp(P);
    writetable(T,"Vandermonde.xlsx")