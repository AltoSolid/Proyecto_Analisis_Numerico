%ITERATIVE GAUSS SEIDEL METHOD WITH RELAXATION (SOR)
format long 

A=input('Enter the coefficient matrix: ');
b=input('Enter the independent terms: ');
x0=input('Enter the vector with the Initial guesses: ');
Nmax=input('Enter the number of iterations: ');
tol=input('Enter tolerance: ');
w=input('Enter lambda of the relaxation: ');
k=norm(A)*norm(A^-1);
disp('Conditional =')
disp(k)
determinante=det(A);
if determinante==0
    disp('The determinant is zero, the problem has no single solution');
end
n=length(b);
d=diag(diag(A));
l=d-tril(A);
u=d-triu(A);
fprintf('\n SOLUTION:\n');
fprintf('\nThe gaussian transition matrix seidel:\n');
Tw=((d-w*l)^-1)*((1-w)*d+w*u);
disp(Tw)
re=max(abs(eig(Tw)));
if re>1
    disp('Spectral radius greater than 1\n The method does not converge');
    return
end
fprintf('\nThe constant vector is:\n');
Cw=w*(d-w*l)^-1*b;
disp(Cw)
i=0;
err=tol+1;
z=[i,x0(1),x0(2),x0(3),err];
while err>tol && i<Nmax
    xi=Tw*x0+Cw;
    err=max(sqrt((xi(1)-x0(1))^2+(xi(2)-x0(2))^2+(xi(3)-x0(3))^2));
    x0=xi;
    i=i+1;
    z(i,1)=i;
    z(i,2)=x0(1);
    z(i,3)=x0(2);
    z(i,4)=x0(3);
    z(i,5)=err;
end
fprintf('\nTABLE:\n\n n      x1       x2          x3         Error\n\n ');
disp(z)