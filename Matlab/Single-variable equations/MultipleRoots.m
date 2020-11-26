syms x
format short
fileID = fopen('MultipleRoots.txt','w');
iter=input("Enter iterations: ");
x0=input("Enter an initial approximation: ");
f=input("Enter the function to evaluate: ");
fp=input("Enter the first derivative: ");
fpp=input("Enter the second derivative: ");
error=input("Enter the maximum absolute error accepted: ");
f0=subs(f,x0);
f1=subs(fp,x0);
f2=subs(fpp,x0);
g=x0-((f0*f1)/((f1^2)-(f0*f2)));
e=1;
g2=0;
c=2;

fprintf('Multiple roots\n');
fprintf(fileID,'Multiple roots\n');
%fprintf('iter \t   xi    \t      f(xi)     \t E \n');
fprintf(fileID,'iter \t      xi    \t   f(xi)  \t   fp(xi)  \t   fpp(xi)  \t     E \n');
%fprintf('%3.0f \t %12.10f \t %1.1e\t %1.1e\n',[0;x0;f]);
fprintf(fileID,'%3.0f \t %12.10f \t  %1.1e\t  %1.1e\t  %1.1e\t       %1.1e\n',[0;x0;f0;f1;f2;inf]);
f0=subs(f,g);
f1=subs(fp,g);
f2=subs(fpp,g);
e=abs(x0-g);
fprintf(fileID,'%3.0f \t %12.10f \t  %1.1e\t  %1.1e\t  %1.1e\t       %1.1e\n',[1;g;f0;f1;f2;e]);

while e>=error && c<=iter
    f0=subs(f,g);
    f1=subs(fp,g);
    f2=subs(fpp,g);
    g2=g;
    g=eval(g2-((f0*f1)/((f1^2)-(f0*f2))));
    e=abs(g-g2);
    fprintf(fileID,'%3.0f \t %12.10f \t  %1.1e\t  %1.1e\t  %1.1e\t       %1.1e\n',[c;g;f0;f1;f2;e]);
    c=c+1;
end
fprintf(fileID, 'With an error of: %d\n', e);
fprintf(fileID, 'There is a root in: %d', g);
fprintf('With an error of: %d\n', e);
fprintf('There is a root in: %d', g);