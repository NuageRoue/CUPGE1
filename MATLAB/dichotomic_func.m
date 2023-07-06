function [ xfinal, nbIter, err ] = dichotomic_func(fun,a,b , tol , iterMax, trueValue )
% Fonction de dichotomie qui execute l'algorithme de dichotomie sur l'intervalle [a,b] pour trouver la racine presente dans cet intervalle
%
% * Entree :
%   => fun = handle = Pointeur de fonction a traiter
%   => a = Int = Borne inferieure de l'intervalle
%   => b = Int = Borne superieure de l'intervalle
%   => tol = Float = critere d'arret
%   => iterMax = Int = Maximum d'iterations de notre algorithme
%
% * Sortie:
%   => xfinal : = Float = L'approximation de notre racine;
%   => nbIter = Int = le nombre d'iteration;
%   => err = [float] = la difference entre la "vraie racine" et la valeur calculee a chaque etapes"

    i = 1;
    FA = fun(a);
    while i <= iterMax && (b - a) > tol
        c = a + (b - a)/2 ; % milieu de l'intervalle [a ; b]
        err(i) = abs(trueValue - c);
        FC = fun(c);
        if FC == 0 || ((b-a)/2 < tol) %si on trouve la valeur exacte donnant 0 ou si l'ecart entre a et b est inferieur a la tolerance
            xfinal = c; % on renvoie c qui fait office de racine (exacte ou non)
            nbIter = i; % le nombre d'iteration necessaire pour que l'algorithme renvoie une valeur
            return
        end
        i = i + 1;
        if FA * FC > 0 %si FA et FC sont de meme signe, on remplace A par C (cela veut dire selon le TVA que le passage par zero est situe entre C et B)
            a = c;
            FA = FC;
        else % sinon, c'est que le passage par zero a lieu entre A et C : on remplace donc b par C
            b = c;
        end
    end
    % si on arrive ici, c'est qu'on a atteint la limite d'iteration. alors, on considere que l'intervalle [a;b] est petit (donc notre approximation est proche de la vraie valeur) et que le TVI y est applicable :
    % on peut donc renvoyer une valeur.
    xfinal = a + (b - a)/2 ;
    err(i) = abs(trueValue - c);
    nbIter = iterMax;
end

