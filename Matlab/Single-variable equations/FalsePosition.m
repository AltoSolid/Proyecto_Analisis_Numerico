#This program finds the solution to the equation f(x)=0 in the interval [a,b]
#using the method of the false rule

format long 
syms x
iter=input("Enter the number of iterations: ");
x0=input("Enter an initial approximation: ");
x1=input("Enter the second initial approximation: ");
f=input("Enter the function: ");
error=input("Enter the maximum absolute error accepted: ");
b=[x1];
c=1; %counter to repeat the method for each interval

f1=subs(f,x0);
f2=subs(f,x1);
xm=eval((f2*x0-f1*x1)/(f2-f1));
fm=eval(subs(f,xm));

 if x1 < x0
            error=["Error", "X1 cannot be greater than X0"];
            Error=table(error);
            writetable(Error);
        else 
       if f1==0
        type1 = ["There is a root in ", x0];
        type1 = table(type1);
        writetable(type1,"False_position");
        return
    elseif f2==0
        type2 = ["There is a root in ", x1];
        type2 = table(type2);
        writetable(type2,"False_position");
        return
    end
    if f1*fm <= 0
        x1=xm;
    else 
        x0=xm;
    end
    e=10;
    fm=eval(subs(f,xm));
    Iter=[c];
    a=[x0];
    Xm=[xm];
    Fxm=[fm];
    E=[0];

  
    while (e) > error && c <= iter
        xmant=xm;
        f1 = subs(f,x0);
        f2= subs(f,x1);
        xm=eval((f2*x0-f1*x1)/(f2-f1));
        fm = eval(subs(f,xm));
        if f1 == 0
            type1 = ["There is a root in ", x0];
            type1 = table(type1);
            writetable(type1,"False_position");
            return
        elseif f2 == 0
            type2 = ["There is a root in ", x1];
            type2 = table(type2);
            writetable(type2,"False_position");
            return
        end
                e= abs(xm-xmant);
        c = c+1;
        fxi= eval(subs(f,xm));
        Iter(c,1) = [c];
        a(c,1)= [x0];
        Xm(c,1)= [xm];
        b(c,1)= [x1];
        Fxm(c,1) = [fm];
        E(c,1) = [e];
        if f1*fm <= 0
            x1=xm;
        else 
            x0=xm;
        end

        end
    T = table(Iter,a,Xm,b,Fxm,E);
    writetable(T,"False_position");
end


    