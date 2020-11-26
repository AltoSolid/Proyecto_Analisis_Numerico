%This program finds the solution to the equation f(x)=0 in the interval [a,b].
%using the method of bisection. 

syms x
format long
fileID = fopen('Bisection_result','w');

%iter = input("Number of iterations: ");
%x0 = input("The first value of the interval: ");
%x1 = input("The second value of the interval: ");
%f = input("Function: ");
%error = input("Enter the maximum relative error accepted (using 10^n format)")

itera = 100;
a = 0;
b = 1;
f = log(sin(x)^2+1)-1/2;
tol = 10^-7;
c = 1;

xmi=(a+b)/2;
fxm=subs(f,xmi);
e = abs(xmi-a);

fprintf('Bisection\n');
fprintf(fileID,'Bisection\n');
fprintf(fileID,'iter \t      a    \t         x(m)  \t           b  \t       f(Xm)  \t E \n');
fprintf(fileID,'%3.0f \t %12.10f \t %12.10f \t %12.10f \t %1.1e\t %1.1e\n',[c;a;xmi;b;fxm;inf]);

while e>=tol && c<=itera
    xmi=(a+b)/2;
    fai=subs(f,a);
    fbi=subs(f,b);
    fxm=subs(f,xmi);
    e = abs(xmi-a);
    if c > 1
        fprintf(fileID,'%3.0f \t %12.10f \t %12.10f \t %12.10f \t %1.1e\t %1.1e\n',[c;a;xmi;b;fxm;e]);
    end
    
    if fai==0
        fprintf("There's a root in: %d", a)
    elseif fbi==0
        fprintf("There's a root in: %d", b)
    end
    
    if fai*fxm<0
        a=a;
        b=xmi;
        e = abs(xmi-a);        
    else
        a=xmi;
        b=b;
        e = abs(xmi-b);
    end   
    c=c+1;
end

fprintf('Error: %1.1e\n', e)
fprintf('There is a root in: %12.15f\n', xmi)