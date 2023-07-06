function [ xfinal, nbIter, err ] = secante_func(fun, a, b, iterMax, tol, trueValue)
% Fonction de la secante
%
% * Entree :
%   => fun = handle = Pointeur de fonction a traiter
%   => a = Float = Borne inf de l'intervalle de recherche
%   => b = Float = Borne sup de l'intervalle de recherche
%   => iterMax = Int = Maximum d'iterations de notre algorithme
%   => tol = Float = critere d'arret
%   => trueValue = Float = veritable valeur de la racine
%
% * Sortie :
%   => xfinal = Float = L'approximation de notre racine
%   => nbIter = Int = Nombre d'iterations necessaire pour trouver la bonne valeur approchee
%   => err = [ Float ] = Valeur de l'erreur entre l'element calcule et la veritable valeur

  i = 1;
  c = b - (b - a)/(fun(b) - fun(a))*fun(b);

  while i <= iterMax
    if abs(fun(c)) < tol % si la valeur absolue de f(c) vaut 0 en prenant en compte la tolerance,
      xfinal = c; % on renvoie c comme valeur finale
      nbIter = i;
      err(i) = abs(trueValue - c);
      break
    end%sinon, on change la valeur de A, B et C, avec :
    err(i) = abs(trueValue - c);
    i = i+1;
    a = b; % la valeur de B remplace la valeur de A ;
    b = c; % la valeur de C remplace la valeur de B ;
    c = b - (b - a)/(fun(b) - fun(a))*fun(b); % la nouvelle valeur de C ;
  end
  xfinal = c; % on renvoie c comme valeur finale
  nbIter = i;
  err(i) = abs(trueValue - c);
end
