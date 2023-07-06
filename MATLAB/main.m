clear all
close all
clc

format long

fun = @(x) x^3 + 4*x^2 - 10; % la fonction qu'on va etudier
deriv = @(x) 3 * x^2 + 8*x; % sa derivee

trueValue = roots([1 4 0 -10]);
trueValue = trueValue(3); % la vraie valeur de la racine
tolerance = 10^(-3); % notre tolerance, precision
nbMaxIter = 100; % le nombre maximum d'iteration possible avec la fonction

a = 0;
b = 5;


initPoint = 0; % la valeur passee en entree de la methode du point fixe
funPtFixe = @(x) 1/2 * sqrt(-x^3 +10); % la fonction passee en entree de la methode du point fixe

initNewton = 5; % la valeur passee en entree de la methode de Newton


%temps d'execution sur n_executions :

n_executions = 100;

% methode de la dichotomie :
temps_total = 0;
for i = 1:n_executions % on repete ce qui suit 100 fois
    temps_debut = clock;

    [x_dicho, iter_dicho, err_dicho] = dichotomic_func(fun, 0,5, 10^(-4), 100,trueValue);

    temps_fin = clock;

    %durée d'exécution en secondes de l'algorithme :
    duree_execution = etime(temps_fin, temps_debut);

    temps_total = temps_total + duree_execution; % on fait la somme de tous les temps d'exécution
end
temps_moyen_dicho = temps_total / n_executions; % on fait la moyenne
vitesse_moyenne_dicho = iter_dicho / temps_moyen_dicho; % vitesse exprimee en iteration/seconde


% methode de la trichotomie :
temps_total = 0;
for i = 1:n_executions
    temps_debut = clock;

    [x_tricho, iter_tricho, err_tricho] = dichotomic2_func(fun, a, b, tolerance, nbMaxIter, trueValue);

    temps_fin = clock;

    %durée d'exécution en secondes de l'algorithme
    duree_execution = etime(temps_fin, temps_debut);

    % Ajouter la durée d'exécution au temps total
    temps_total = temps_total + duree_execution;
end
temps_moyen_tricho = temps_total / n_executions;
vitesse_moyenne_tricho = iter_tricho / temps_moyen_tricho; % vitesse exprimee en iteration/seconde


% methode du point fixe :
temps_total = 0;
for i = 1:n_executions
    temps_debut = clock;

    [x_ptFixe, iter_ptFixe, err_ptFixe] = fixedPoint_func(funPtFixe, initPoint, nbMaxIter, tolerance, trueValue);

    temps_fin = clock;

    %durée d'exécution en secondes de l'algorithme
    duree_execution = etime(temps_fin, temps_debut);

    % Ajouter la durée d'exécution au temps total
    temps_total = temps_total + duree_execution;
end
temps_moyen_ptFixe = temps_total / n_executions;
vitesse_moyenne_ptFixe = iter_ptFixe / temps_moyen_ptFixe ;% vitesse exprimee en iteration/seconde


% methode de Newton :
temps_total = 0;
for i = 1:n_executions
    temps_debut = clock;

    [x_newt, iter_newt, err_newt] = newton_func(fun, deriv, initNewton, nbMaxIter, tolerance, trueValue);

    temps_fin = clock;

    %durée d'exécution en secondes de l'algorithme
    duree_execution = etime(temps_fin, temps_debut);

    % Ajouter la durée d'exécution au temps total
    temps_total = temps_total + duree_execution;
end
temps_moyen_newt = temps_total / n_executions;
vitesse_moyenne_newt = iter_newt / temps_moyen_newt; % vitesse exprimee en iteration/seconde



% methode de la secante :
temps_total = 0;
for i = 1:n_executions
    temps_debut = clock;

    [x_seca, iter_seca, err_seca] = secante_func(fun, a, b, nbMaxIter, tolerance, trueValue);

    temps_fin = clock;

    %durée d'exécution en secondes de l'algorithme
    duree_execution = etime(temps_fin, temps_debut);

    % Ajouter la durée d'exécution au temps total
    temps_total = temps_total + duree_execution;
end
temps_moyen_seca = temps_total / n_executions;
vitesse_moyenne_seca = iter_seca / temps_moyen_seca; % vitesse exprimee en iteration/seconde



% methode de la fausse position :
temps_total = 0;
for i = 1:n_executions
    temps_debut = clock;

    [x_falsePos, iter_falsePos, err_falsePos] = falsePos_func (fun, a, b, nbMaxIter , tolerance , trueValue);

    temps_fin = clock;

    %durée d'exécution en secondes de l'algorithme
    duree_execution = etime(temps_fin, temps_debut);

    % Ajouter la durée d'exécution au temps total
    temps_total = temps_total + duree_execution;
end
temps_moyen_falsePos = temps_total / n_executions;
vitesse_moyenne_falsePos = iter_falsePos / temps_moyen_falsePos; % vitesse exprimee en iteration/seconde





%trace des courbes :

max_num_points = max([iter_dicho, iter_falsePos, iter_newt, iter_ptFixe, iter_seca, iter_tricho]);

% on "comble" les matrice pour qu'elles aient toutes autant de valeurs (soit autant que la plus grande)

err_dicho = [ err_dicho, NaN(1, max_num_points - iter_dicho)];
err_tricho = [ err_tricho, NaN(1, max_num_points - iter_tricho)];
err_ptFixe = [ err_ptFixe, NaN(1, max_num_points - iter_ptFixe)];
err_newt = [ err_newt, NaN(1, max_num_points - iter_newt)];
err_seca = [ err_seca, NaN(1, max_num_points - iter_seca)];
err_falsePos = [ err_falsePos, NaN(1, max_num_points - iter_falsePos)];


figure;
plot(log10(err_dicho));
hold on;
plot(log10(err_tricho));
plot(log10(err_ptFixe));
plot(log10(err_newt));
plot(log10(err_seca));
plot(log10(err_falsePos));
hold off;

legend('dichotomie', 'trichotomie', 'point fixe', 'Newton', 'secante', 'fausse position');

xlabel('itération');
ylabel('log10(erreur)');
title("Courbes représentant la difference entre l'approximation de la racine et sa vraie valeur, à chaque itération");

err_dicho = err_dicho(iter_dicho);
err_tricho = err_tricho(iter_tricho);
err_ptFixe = err_ptFixe(iter_ptFixe);
err_newt = err_newt(iter_newt);
err_seca = err_seca(iter_seca);
err_falsePos = err_falsePos(iter_falsePos);
