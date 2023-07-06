function [ xfinal, nbIter, err ] = falsePos_func (fun, a, b, iterMax , tol , trueValue)
%   Fonction de la fausse position
%
%   * Entree :
%       => fun = handle = Pointeur de fonction a traiter
%       => a = Float = Borne inf de l'intervalle de recherche
%       => b = Float = Borne sup de l'intervalle de recherche
%       => iterMax = Int = Maximum d'iterations de notre algorithme
%       => tol = Float = critere d'arret
%       => trueValue = Float = veritable valeur de la racine
%   * Sortie :
%       => xfinal = Float = L'approximation de notre racine
%       => nbIter = Int = Nombre d'iterations necessaire pour trouver la bonne valeur approchee
%       => err = [ Float ] = Valeur de l'erreur entre l'element calcule et la veritable valeur

    i = 1;
    FA = func(a);
    while i <= iterMax
        c = b - (b - a)/(fun(b) - fun(a))*fun(b) ; % on modifie la valeur e C selon la formule donnee par la methode de la secante ;
        err(i) = abs(trueValue - c);
        FC = func(c);
        if abs(FC) <= tol % si cette valeur est egale a 0 en prenant en compte la tolerance,
            xfinal = c; % on renvoie C comme valeur finale ;
            nbIter = i;
            return
        end % sinon, on modifie notre valeur de A et B au besoin :
        i = i + 1;
        if FA * FC > 0 % si le passage par zero n'est pas compris entre A et C, on remplace A par C et on itere une nouvelle fois;
            a = c;
            FA = FC;
        else % si au contraire le passage par zero se fait entre A et C, on remplace B par C avant d'iterer une nouvelle fois.
            b = c;
        end
      xfinal = c;
      err(i) = abs(trueValue - c);
      nbIter = iterMax;
    end
    %xfinal = -1;
    %echo la methode a echoue [...]
end
