function [ xfinal, nbIter, err ] = newton_func(fun, deriv, p0, iterMax, tol, trueValue)

% Fonction de Newton
%
% * Entree :
%   => fun = handle = Pointeur de fonction a traiter
%   => deriv = handle = Pointeur sur la derivee de fonction a traiter
%   => p0 = Fl o a t = p r emi e r e app r oxim a ti on
%   => tol = Float = critere d'arret
%   => iterMax = Int = Maximum d'iterations de notre algorithme
%   => trueValue = Float = veritable valeur de la racine
%
% * Sortie :
%   => xfinal = Float = L'approximation de notre racine
%   => nbIter = Int = Nombre d'iterations necessaire pour trouver la bonne valeur approchee
%   => err = [ Float ] = Valeur de l'erreur entre l'element calcule et la veritable valeur

  i = 1;
  while i <= iterMax
    if abs(fun(p0)) <= tol % si f(p0) = 0 en prenant en compte la tolerance
      xfinal = p0; % on renvoie p comme valeur finale
      nbIter = i;
      err(i) = abs(trueValue - p0);
      return
    end
    err(i) = abs(trueValue - p0);
    i = i+1;
    p0 = p0 - (fun(p0)/deriv(p0)); % sinon, on change la valeur de p selon la suite (Un) definie sur N* par Un+1 = Un - f(Un)/f'(Un)
  end
  xfinal = p0; % on renvoie p comme valeur finale
  nbIter = i;
  err(i) = abs(trueValue - p0);
end
