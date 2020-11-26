%This program finds the roots of a non-linear equation from an initial value using Newton method

syms x
format long
fileID = fopen('Newton_result.tex','w');
iter = input("Enter iterations: ");
x0 = input("Enter an initial approximation: ");
fun = input("Enter function: ");
dfun = input("Enter derivative: ");
tol = input("Enter tolerance(use 10^n format): ");

iter = 100;
x0 = 0.5;
fun = log(sin(x)^2+1)-1/2;
dfun = 2*((sin(x)^2+1)^-1)*sin(x)*cos(x);
tol = 10^-7;
f=subs(fun,x0);
df=subs(dfun,x0);
c=1;
a = x0-f/df;
e=(abs(a-x0));

fprintf('Newton\n');
fprintf(fileID,'Newton\n');
%fprintf('iter \t   xi    \t      f(xi)     \t E \n');
fprintf(fileID,'iter \t      xi    \t   f(xi)  \t     E \n');
%fprintf('%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[0;x0;f]);
fprintf(fileID,'%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[0;x0;f;inf]);

while e>tol && c<=iter
    a = x0-f/df;
    f=subs(fun,a);
    df=subs(dfun,a);
    e=(abs(a-x0));
    x0=a
    %fprintf('%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[c;a;f;e]);
    fprintf(fileID,'%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[c;a;f;e]);
    c=c+1
    
end

fprintf(fileID,'With an error of: %1.1e\n',e);
fprintf(fileID,'There is a root in: %12.15f\n',a);
fclose(fileID);


fprintf("With an error of: %1.1e\n",e)
fprintf("There is a root in: %12.15f\n",a)