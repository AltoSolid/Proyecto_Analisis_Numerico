%This program finds the roots of a non-linear equation from initials values using Secant method

syms x
fileID = fopen('Secant.txt','w');

iter=input("Enter the number of iterations: ");
x0=input("Enter an initial approximation: ");
x1=input("Enter the second initial approximation: ");
f=input("Enter the function: ");
error=input("Enter the maximum absolute error accepted: ");
f0=subs(f,x0);
f1=subs(f,x1);
xa=x1-((f1*(x1-x0))/(f1-f0));
e= abs(xa-x1);
c=2;
ft=subs(f,xa);

fprintf('Secant\n');
fprintf(fileID,'Secant\n');
%fprintf('iter \t   xi    \t      f(xi)     \t E \n');
fprintf(fileID,'iter \t      xi    \t   f(xi)  \t     E \n');
%fprintf('%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[0;x0;f]);
fprintf(fileID,'%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[0;x0;f0;inf]);
fprintf(fileID,'%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[1;x1;f1;inf]);
fprintf(fileID,'%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[2;xa;ft;e]);

while e>=error && c<=iter
    x0=x1;
    x1=xa;
    f0=subs(f,x0);
    f1=subs(f,x1);
    xa=eval(x1-((f1*(x1-x0))/(f1-f0)));
    e=abs(xa-x1);
    c=c+1;    
    ft=subs(f,xa);
    fprintf(fileID,'%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[c;xa;ft;e]);
end

fprintf(fileID,'With an error of: %1.1e\n',e);
fprintf(fileID,'There is a root in: %12.15f\n',xa);
fclose(fileID);

fprintf('With an error of: %d\n', e)
fprintf('There is a root in: %d', xa)