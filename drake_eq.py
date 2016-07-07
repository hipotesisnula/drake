#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os


def drake(Rs, fp, ne, fl, fi, fc, L):
    """
    Ecuación de Drake.

    Parámetros
    ----------
    Rs : float
        Tasa anual de formación de estrellas adecuadas en la 
        galaxia.
    fp : float
        Fracción de estrellas que tienen planetas en su órbita.
    ne : float
        Número de esos planetas orbitando dentro de la ecosfera 
        de la estrella.
    fl : float
        Fracción de planetas dentro de la ecosfera en los que la 
        vida se ha desarrollado.
    fi : float
        Fracción de esos planetas en los que la vida inteligente 
        se ha desarrollado.
    fc : Fracción de esos planetas donde la vida inteligente ha 
         desarrollado una tecnología e intenta comunicarse.
    L : lapso, medido en años, durante el que una civilización 
        inteligente y comunicativa puede existir.

    Regresa
    -------
    N : float
        Número de civilizaciones que podrían comunicarse en 
        nuestra galaxia.
    """
    N = Rs * fp * ne * fl * fi * fc * L
    return N


def main(factores, salida=None):
    """
    Calcula el número de civilizaciones inteligentes que podrían
    comunicarse en nuestra galaxia usando la ecuación de Drake.
    """
    # Cada columna representa un factor
    Rs, fp, ne, fl, fi, fc, L = [
        factores[:, i].astype(np.float) for i in range(1, 8)]

    # Calcular número de civilizaciones extraterrestres usando
    # la ecuación de Drake
    N = drake(Rs, fp, ne, fl, fi, fc, L)

    # Mostrar los resultados en pantalla
    out_str = '#\tNúmero de civilizaciones\n'
    for no, est in zip(factores[:, 0], N):
        out_str += '{0}\t{1}\n'.format(no, est)
    
    print(out_str)

    # Guardar los resultados
    if salida is not None:
        with open(os.path.join(salida, 'resultados.txt'), 'w') as f:
            f.write(out_str)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser('Calcula el número de civilizaciones en nuestra '
                                     'galaxia usando la ecuación de Drake')

    parser.add_argument('factores',
                        help=('Ubicación del archivo con los factores '
                              'de la ecuación de Drake'))

    parser.add_argument('-g',
                        help=('Directorio donde se guardarán los resultados'),
                        default=None)

    args = parser.parse_args()

    # Leer el archivo con los factores
    args.factores = np.loadtxt(args.factores, dtype=str,
                               delimiter='\t', skiprows=1)
    # Correr el método principal
    main(args.factores, args.g)
