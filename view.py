#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime

from matplotlib import ticker
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import matplotlib.pyplot as pypl
import tkinter as kink
import matplotlib.dates as mpdates
from matplotlib.ticker import (MultipleLocator, MaxNLocator)

from model_class import CustomFormatter
import datetime


class Plotwindow:
    """
    Calss for plotting a graph
    """

    def __init__(self, masterFrame, size):
        """
        Initialization of the Plot-window
        :param masterFrame: Frame for position in main Application
        :param size: width x height size of the widget
        """
        self.plots = []
        self.figure = pypl.figure(figsize=size, dpi=100)
        self.figure.tight_layout()
        self.axes = pypl.subplot(1, 1, 1)
        self.axeslist = list()
        self.axeslist.append(self.axes)
        # create canvas as matplotlib drawing area
        self.mainFrame = masterFrame
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.mainFrame)
        nav = NavigationToolbar2Tk(self.canvas, self.mainFrame)
        nav.update()
        nav.pack(side=kink.BOTTOM, fill=kink.X)  # Navigation for the plot. Else no navigation is there
        self.canvas.get_tk_widget().pack()  # Get reference to tk_widget

    def __scatter_plotxy__(self, valueList=list(), titel="", labellist=list, xlabel="", ylabel="", multi=False,
                           i=1):  # Todo:Implementing lablelist functionality
        """
        internal Methode for creating the plot
        :param valueList: list which contains the data set for graph
        :param titel: titel of the graph
        :param labellist: list with the labels for the ´lableing information
        :param xlabel: label on grid for x axis
        :param ylabel: label on grid for y axis
        :param multi: default False. if True the canvas is not redrawn
        :return: None
        """
        self.plots.clear()
        # Loop: Creating graph for multi plotting
        for id, data in valueList:
            if multi:  # Multi plot for different graphs
                self.data = data
                self.axes = pypl.subplot(3, 1, i)
                self.axeslist.append(self.axes)
            else:  # Single graph
                self.axes = pypl.subplot(i, 1, 1)
                self.axeslist.append(self.axes)
            # plotting the dat to the active graph
            plot, = pypl.plot(data[0], data[1], alpha=0.7, linewidth=2.0, label=f" {id}")
            self.plots.append(plot)
        # after creating the active graph
        # preparing the legend and the axes
        pypl.legend(handles=self.plots, loc='best')  # with this the legend has the correct information to display
        self.axes.set_ylabel(ylabel)
        self.axes.set_xlabel(xlabel)
        self.axes.set_title(titel)
        self.axes.tick_params(axis='x', labelrotation=-45.0, right=True)
        self.axes.tick_params(axis='x', which='major', width=0.75, length=2, labelsize=7)
        self.axes.xaxis.set_major_locator(mdates.MonthLocator())
        # self.axes.xaxis.set_major_formatter(pypl.FuncFormatter(self.format_func))    #Todo: finishing function
        self.axes.xaxis.set_major_formatter(mdates.ConciseDateFormatter(self.axes.xaxis.get_major_locator()))
        self.axes.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

        self.axes.set_xlim([min(self.data[0]), max(self.data[0])])
        pypl.rc('axes', labelsize=5)  # Setting the labelsize for ticks
        if not multi:  # only is solo graph executed
            self.canvas.draw()

    def format_func(self, value, tick_number):  # Todo: finihsing function
        """
        Goal-> Creating a text for label based on date
        :param value: directly from the tick  creation
        :param tick_number: number of the tick
        :return: text for label
        """
        try:
            date = datetime.datetime.strptime(self.data[0][tick_number], "%Y-%m-%d")
            try:
                date2 = datetime.datetime.strptime(self.data[0][tick_number - 1], "%Y-%m-%d")
            except:
                date2 = datetime.datetime.now()

            if str(date.year) == str(date2.year):
                if date.month > date2.month:
                    return date.strftime("%b")
                elif not int(date.month) == 1:
                    return date.day
            else:
                return date.year
        except:
            pass

    def __clearplot__(self):
        """
        clearing the plot for new data
        :return:
        """
        self.plots.clear()
        self.figure.clf()
        self.figure.tight_layout()
        self.canvas.draw()

    def plot_scatter_data(self, valueList, titel="", labelList=list(), xlabel="", ylabel="", multi=False, i=1):
        """
        Methode for creating the plot
        :param valueList: list which contains the data set for graph or dict for multi plotting
        :param titel: titel of the graph
        :param labellist: list with the labels for the ´lableing information Todo
        :param xlabel: label on grid for x axis
        :param ylabel: label on grid for y axis
        :param multi: default False. if True the canvas is redrawn after plotting all plots
        :return: None or False if multi get wrong param
        """
        self.__clearplot__()
        if multi:
            i = 1
            for item in labelList:
                if type(valueList) == type(dict()):
                    valueList2 = list()
                    for dataset in valueList[item]:
                        valueList2.append(dataset)
                    self.__scatter_plotxy__(valueList=valueList2, titel=item, labellist=labelList, xlabel=xlabel,
                                            ylabel=ylabel, multi=multi, i=i)
                    i += 1
                else:
                    return False
            self.figure.tight_layout()
            self.canvas.draw()
        else:
            if type(valueList) == type(list()):
                self.__scatter_plotxy__(valueList=valueList, titel=titel, labellist=labelList, xlabel=xlabel,
                                        ylabel=ylabel, multi=multi)
            else:
                return False

    def clear(self):
        """External methode to clear the plot"""
        self.__clearplot__()
