#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:12:38 2022

@author: usuario
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cycler


def matplotlib_style():
    # Desired styling for matplotlib
    colors = cycler('color',["44aa98","ab4498","332389","86ccec","ddcc76","cd6477","882255", "117732"])
    plt.rcParams['figure.figsize'] = [6,4]
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['text.color'] = '212121'
    plt.rcParams['xtick.color'] = '212121'
    plt.rcParams['ytick.color'] = '212121'
    plt.rcParams['font.family'] = 'sans serif'
    plt.rcParams['axes.facecolor'] = 'None'
    plt.rcParams['axes.edgecolor'] = 'dimgray'
    plt.rcParams['axes.grid'] = False
    plt.rcParams['axes.grid'] = False
    plt.rcParams['grid.color'] = 'lightgray'
    plt.rcParams['grid.linestyle'] = 'dashed'
    plt.rcParams['xtick.labelsize'] = 'small'
    plt.rcParams['ytick.labelsize'] = 'small'
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.framealpha'] = 0.8
    plt.rcParams['legend.facecolor'] = 'white'
    plt.rcParams['legend.edgecolor'] = 'None'
    plt.rcParams['legend.fontsize'] = 'medium'
    plt.rcParams['axes.labelsize'] = 'small'
    plt.rcParams['savefig.facecolor'] = 'None'
    plt.rcParams['savefig.edgecolor'] = 'None'
    plt.rc('axes', prop_cycle=colors)
    
    return


def gmd_scale():
    # Color scale for ploting ground motion values
    cmap = mpl.cm.Spectral_r
    bounds = [0.00, 0.01, 0.02, 0.03, 0.05, 0.075, 0.10, 0.20, 0.3, 0.50, 1.00]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    return cmap, norm

