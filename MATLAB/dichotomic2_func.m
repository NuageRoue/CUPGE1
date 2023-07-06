function [ xfinal, nbIter, err ] = dichotomic2_func(fun,a, b, tol, iterMax, trueValue)
%   Fontion de trichotomie qui execute l'algorithme de dichotomie sur l'intervalle [a,b] pour trouver la racine presente dans cet intervalle
%   * Entree :
%       => fun = handle = Pointeur de fonction a traiter
%       => a = Int = Borne inferieure de l'intervalle
%       => b = Int   = Borne superieure de l'intervalle
%       => tol = Float = critere d'arret
%       => iterMax = Int = Maximum d'iterations de notre algorithme
% * Sortie:
%   => xfinal : = Float = L'approximation de notre racine;
%   => nbIter = Int = le nombre d'iteration;
%   => err = [float] = la difference entre la "vraie racine" et la valeur calculee a chaque etapes"

    i = 1;
    FA = fun(a);
    while i <= iterMax && (b - a) > tol
        c1 = a + (b - a)/3 ; % premiere valeur entre A et B;
        c2 = b - (b - a)/3 ; % deuxieme valeur entre A et B;

        FC1 = fun(c1);
        FC2 = fun(c2);


        if FC1 == 0 |((b-a)/3 <= tol) % si FC1 vaut 0 ou si l'ecart entre A et C1 est inferieur a la tolerance, on renvoie C1 comme racine;
            xfinal = c1;
            nbIter = i;
            err(i) = abs(trueValue - xfinal);
            return
        elseif FC2 == 0 % si FC2 vaut 0, on renvoie c2 comme racine.
            xfinal = c2;
            nbIter = i;
            err = abs(trueValue - xfinal);
            return
        end
        if FA * FC1 > 0 % si le changement de signe a lieu apres c1, on doit verifier si il a lieu entre c1 et c2, ou c2 et b
            if FA * FC2 > 0 % si il a lieu entre c2 et b :
              a = c2; % on change la valeur de a
              FA = FC2;
              err(i) =  abs(trueValue - c2); % on prend c2 comme approximation de la racine
            else
              a = c1; % si il a lieu entre c1 et c2, on change les valeurs de a et b
              b = c2;
              FA = FC1;
              err(i) =  abs(trueValue - (a + (b - a)/2)); % on prend le milieu de [c1 ; c2] comme approximation de la racine
            end
        else %sinon, le changement a lieu entre A et C1 : on remplace B par C1
            b = c1;
            err(i) =  abs(trueValue - c1); % on prend c1 comme approximation de la racine
        end
        i = i + 1;
    end
    % si on arrive ici, c'est qu'on a atteint la limite d'iteration. alors, on considere que l'intervalle [a;b] est petit (donc notre approximation est proche de la vraie valeur) et que le TVI y est applicable :
    % on peut donc renvoyer une valeur.
    xfinal = a + (b-a)/2; % on renvoie la valeur au centre de l'intervalle ;
    err(i) = abs(trueValue - xfinal);
    nbIter = iterMax;
end

