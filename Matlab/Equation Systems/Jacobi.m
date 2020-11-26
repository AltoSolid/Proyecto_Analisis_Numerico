%This program results in systems of equations
%using the iterative method of Jacobi

A=input('Enter matrix A = ');
b=input('Enter matrix b = ');
x0=input('Enter the initial vector x0 = ');
Tol=input('Enter the tolerance Tol = ');

[n,m]=size(A);
detA=det(A);
if detA==0
    disp('The determinant is zero')
end
D=diag(diag(A));
L=-tril(A,-1);
U=-triu(A,1);
disp(' ');
disp(L)
disp(' ');
disp(U)
disp(' ');
fprintf('\n A= \n');
disp(' ');
disp(A)
disp(' ');
fprintf('\n Matrix D: \n')
disp(' ');
fprintf('\n D= \n');
disp(' ');
disp(D)
fprintf('\n Matrix L: \n')
disp(' ');
fprintf('\n L= \n');
disp(' ');
disp(L)
disp(' ');
fprintf('\n Matrix U: \n')

disp(' ');
fprintf('\n U= \n');
disp(' ');
disp(U)
disp(' ');
fprintf('\n SOLUTION: \n')
fprintf('\n TRANSITION MATRIX:\n')
Tj=(D^(-1))*(L+U);
disp(' ');
fprintf('\n Tj \n');
disp(' ');
disp(Tj);
disp(eig(Tj))
respec=max(abs(eig(Tj)));
disp(' ');
fprintf(' Spectral Radio %g \n',respec)
disp(' ');
if respec>1
    disp(' THE SPECTRAL RADIUS IS GREATER THAN 1 ')
    disp(' METHOND FAILED ')
    return
end
fprintf('\n VECTOR : \n')
Cj=(D^(-1))*b;
disp(' ');
fprintf('\n Cj \n');
disp(' ');

disp(Cj);
i=0;
err=Tol+1;
while err>Tol
    xinic=Tj*x0+Cj;
    disp(' ');
    disp(xinic);
    disp(' ');
    err=norm(xinic-x0);
    x0=xinic;
    i=i+1;
end
fprintf('\n Solution in %g iterations: \n',i)
disp(' ');
for in=1:n
    fprintf(' X%g=%g\n',in,xinic(in))
end
disp(' ');
disp(' error equal to: ');
disp(' ');
fprintf(' %g \n',err);