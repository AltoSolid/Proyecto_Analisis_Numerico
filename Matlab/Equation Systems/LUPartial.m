%LU factorization method with Gaussian elimination with 
%partial pivoting to solve systems of equations.

function [x,L,U,P]=LUpar(A,b)

format long
result = fopen('LUpar_result.txt', 'w');

[m,n] = size(A);

% Errores
if det(A)==0
    fprintf(result, 'Error \nMatrix must be nonsingular');
    fclose(result);
    open('LUpar_result.txt');
    return;
end
if m~=n
    fprintf(result, 'Error \nMatrix must be square (nxn)');
    fclose(result);
    open('LUpar_result.txt');
    return;
end
if m~=length(b)
    fprintf(result, 'Error \nVector b must have length %n', n);
    fclose(result);
    open('LUpar_result.txt');
    return;
end

M = A;
L = eye(n);
P = eye(n);
U = zeros(n);  

fprintf(result, 'LU Parcial\n\n');
fprintf(result, 'Results:\n\n');
fprintf(result, 'Iteration 0\n\n');
fprintf(result, '\n');

%LUpar
for i=1:n-1
    [gr, pos] = max(abs(M(i+1:n,i)));
    
    if gr>abs(M(i,i))
        auxM = M(pos+i, i:n);
        auxP = P(pos+i, :);
        M(pos+i, i:n) = M(i, i:n);
        P(pos+i, :) = P(i, :);
        M(i, i:n) = auxM;
        P(i, :) = auxP;
        if i>1
           auxL = L(pos+i, 1:i-1);
           L(pos+i, 1:i-1) = L(i, 1:i-1);
           L(i, 1:i-1) = auxL;
        end
    end 
    for j=i+1:n
        if M(j,i)~=0
            L(j,i) = M(j,i)/M(i,i); 
            M(j,i:n) = M(j,i:n)-(M(j,i)/M(i,i))*M(i,i:n);
        end
    end
    
    U(i,i:n) = M(i,i:n);
    U(i+1,i+1:n) = M(i+1,i+1:n);
    fprintf(result, '\n');
end
U(n,n)=M(n,n);

%Results
z=sustprgr([L P*b]);
x = [L P*b];
%x=sustregr([U z]);
fprintf(result, 'x:\n');
fprintf(result, '%.6f\n', x);

fclose(result);
open('LUpar_result.txt');

end