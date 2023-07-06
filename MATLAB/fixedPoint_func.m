function [ xfinal, nbIter, err ] = fixedPoint_func(fun, p0, iterMax, tol, trueValue)
%   Fonction d'iteration du point fixe (fixed point iteration)
%
%   * Entree :
%       => fun = handle = Pointeur de fonction a traiter
%       => p0 = Float = initial approximation
%       => tol = Float = critere d'arret
%       => iterMax = Int = Maximum d'iterations de notre algorithme
%       => trueValue = Float = veritable valeur de la racine
%
%   * Sortie:
%       => xfinal = Float = L'approximation de  notre racine
%       => nbIter = Int = Nombre d'iterations necessaire pour trouver la bonne valeur approchee
%       => err = [ Float ] = Valeur de l'erreur entre l'element calcule et la veritable valeur

    i = 1;

    while i <= iterMax
        if abs(fun(p0)-p0) <= tol % si f(p0) = p0 en prenant en compte la tolerance,
            nbIter = i;
            xfinal = p0; % on renvoie p0
            err(i) = abs(trueValue - p0);
            return
        end % si ce n'est pas le cas, on modifie la valeur de p0
        err(i) = abs(trueValue - p0);
        p0 = fun(p0); % on a la suite (Un) definie sur N* tel que Un+1 = f(Un) avec f la fonction passee en entree
        i = i + 1;
    end % malgre tout, on renvoie les valeurs demandees
    nbIter = i;
    xfinal = p0; % on renvoie p0
    err(i) = abs(trueValue - p0);
end



