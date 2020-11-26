%This program is to find the interpolating polynomial of Lagrange that passes through some given points

function [L,Coef]=Lagrange(X,Y) 
result = fopen('LagrangeResult.txt', 'w');
n=length(X);
L=zeros(n);
fprintf(result, 'Lagrange\n\n');
fprintf(result, 'Results:\n\n');
fprintf(result, "Lagrange's interpolating polynomial:\n\n");

for i=1:n   
    aux0=setdiff(X,X(i));
    aux=[1 -aux0(1)];
    for j=2:n-1
        aux=conv(aux,[1 -aux0(j)]);
        fprintf(result, '\n');
    end
    L(i,:)=aux/polyval(aux,X(i));
end
fprintf(result, '\n');
Coef=Y*L;
fprintf(result, "Polynomial:\n\n");
fprintf(result, [repmat(' %.6f ', 1, n) '\n'], Y);
fclose(result);
open('LagrangeResult.txt');
end

