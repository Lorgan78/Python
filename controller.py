#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime
import json
import model_class as mc
import view as view
import tkinter as kink


class Controller:
    """controller function-> control of logic"""

    def __init__(self):
        """
        Initialization of class Controller
        """
        self.root = kink.Tk()
        self.root.geometry("1200x1400")
        self.root.title("MyPlot")
        self.mainframe = kink.Frame(self.root)
        self.mainframe.grid(row=4, column=4, sticky="nsew")
        self.__init_widgets__()
        self.plot_w = view.Plotwindow(self.subFrame, (8, 8))

    def __init_widgets__(self):
        """
        Initialization of the widgets.
        :return:
        """
        name = "World"
        self.buttonframe = kink.Frame(self.root, bg="white")
        self.buttonframe.grid(row=0, column=0, sticky="nsew")
        self.button1 = kink.Button(self.buttonframe, text=name, command=lambda: self.plotten(name, multi=True))
        self.button1.grid(row=1, column=0, sticky="nsew")
        self.button2 = kink.Button(self.buttonframe, text="Clear", command=self.clear)
        self.button2.grid(row=0, column=1, sticky="nsew")
        self.button3 = kink.Button(self.buttonframe, text="Close", command=self.close)
        self.button3.grid(row=0, column=2, sticky="nsew")
        self.listbox = kink.Listbox(self.mainframe)
        self.listbox.grid(row=2, column=1)
        self.labelText = kink.StringVar()
        self.labelText.set("Select Land")
        self.label1 = kink.Label(self.mainframe, textvariable=self.labelText)
        self.label1.config(width=40, relief="sunken", borderwidth=2, font=("Arial", 20))
        self.label1.grid(row=0, column=2)
        self.button4 = kink.Button(self.mainframe, text="Show selected", command=self.show_selected)
        self.button4.grid(row=2, column=0)
        self.subFrame = kink.Frame(self.mainframe)
        self.subFrame.grid(row=1, column=2, rowspan=3)

    def close(self):
        """
        Destroy class Controller.
        :return:
        """
        self.root.destroy()

    def clear(self):
        """
        Clear plot window for new information
        :return:
        """
        self.labelText.set("Select Land")
        self.plot_w.clear()

    def show_selected(self):
        self.plotten(value=self.listcontinent[self.listbox.curselection()[0]], multi=True)
        return

    def plotten(self, value, multi, labellist=list()):
        """
        Creating view of the selected Data
        :param value: contains the name of dataset.
        :param multi: True if it is a data set for multi plotting
        :param labellist: list of label for multi plotting.
        :return: None
        """
        __diction__ = self.get_draw_value(value)  # Getting correct Dataset based on name
        self.x_cords = None
        try:  # creating data variables class variable.
            self.x_cords = __diction__["date"]
            self.total_Cases = __diction__['total_cases']
            self.new_case = __diction__['new_cases']
            self.stringency_index = __diction__['stringency_index']
            self.total_deaths = __diction__['total_deaths']
            self.new_deaths = __diction__['new_deaths']
            self.new_cases_smoothed = __diction__['new_cases_smoothed']
            self.labelText.set("Corona statistic -> " + value)
            self.label1.update()
            # converting json data in correct version for plotting.
            dumyList = list()
            for item in self.x_cords:
                dumyList.append(datetime.datetime.strptime(item, "%Y-%m-%d"))
            self.x_cords = dumyList.copy()

            dumyList.clear()
            for item in self.total_Cases:
                dumyList.append(int(item))
            self.total_Cases = dumyList.copy()

            dumyList.clear()
            for item in self.total_deaths:
                dumyList.append(int(item))
            self.total_deaths = dumyList.copy()

            dumyList.clear()
            for item in self.new_case:
                dumyList.append(int(item))
            self.new_case = dumyList.copy()

            dumyList.clear()
            for item in self.new_deaths:
                dumyList.append(int(item))
            self.new_deaths = dumyList.copy()

            dumyList.clear()
            for item in self.new_cases_smoothed:
                dumyList.append(int(item))
            self.new_cases_smoothed = dumyList.copy()
            dumyList.clear()
            del dumyList
        except:
            pass
        if multi:
            labellist = list()
            labellist.append("total")
            labellist.append("stringency")
            labellist.append("new")
            tupel_dict = self.create_dict_list()
            self.plot_w.plot_scatter_data(valueList=tupel_dict, titel="Corona statistic -> " + value, xlabel="Date",
                                          labelList=labellist, multi=True)
        else:
            tupel_list = self.create_tupel_list()
            self.plot_w.plot_scatter_data(valueList=tupel_list, titel="Corona statistic -> " + value, xlabel="Date",
                                          multi=False)

    def create_dict_list(self):
        # creating Tupel and update tupel dict  for use in plot
        tupel_dict = dict()
        try:
            tupel_list = list()
            tupel_list.append(("total cases", (self.x_cords, self.total_Cases)))
        except:
            pass
        try:
            tupel_list.append(("total deaths", (self.x_cords, self.total_deaths)))
        except:
            pass
        tupel_dict.update({"total": tupel_list.copy()})
        try:
            tupel_list = list()
            tupel_list.append(("new cases", (self.x_cords, self.new_case)))
        except:
            pass
        try:
            tupel_list.append(("new deaths", (self.x_cords, self.new_deaths)))
        except:
            pass
        try:
            tupel_list.append(("new cases smoothed", (self.x_cords, self.new_cases_smoothed)))
        except:
            pass
        tupel_dict.update({"new": tupel_list.copy()})
        try:
            tupel_list = list()
            tupel_list.append(("stringency index", (self.x_cords, self.stringency_index)))
        except:
            pass
        tupel_dict.update({"stringency": tupel_list.copy()})
        return tupel_dict.copy()

    def create_tupel_list(self):
        """
        creating Tupel and append tupel list  for use in plot
        :return: returns a copy of the tupel list
        """
        tupel_list = list()
        try:
            tupel_list.append(("total cases", (self.x_cords, self.total_Cases)))
        except:
            pass
        try:
            tupel_list.append(("new cases", (self.x_cords, self.new_case)))
        except:
            pass
        try:
            tupel_list.append(("stringency index", (self.x_cords, self.stringency_index)))
        except:
            pass
        try:
            tupel_list.append(("total deaths", (self.x_cords, self.total_deaths)))
        except:
            pass
        try:
            tupel_list.append(("new deaths", (self.x_cords, self.new_deaths)))
        except:
            pass
        try:
            tupel_list.append(("new cases smoothed", (self.x_cords, self.new_cases_smoothed)))
        except:
            pass

        # valueList=list(), title="",labellist=list,xlabel="",ylabel=""
        # call plot  methode. Send over the Tupel list for view
        return tupel_list.copy()

    def create_value_diction(self, templatefile="template.json", jsonfile="owid-covid-data.json"):
        """
        Create Dictionary with data from json
        :param templatefile: Template with information to identify the selected json
        :param jsonfile: selected json file
        :return: True if exist in Template else False
        """
        b = self.loading_template(templatefile)
        c = self.get_json_key(jsonfile)
        for listitem in b["template"]:
            template = mc.Template(dumb=listitem, exist=True)
            existing = self.exist(c, template)  # Check if template fit to json
            if existing:  # if True create template for processing data
                self.template = template
                self.listcontinent = list()
                self.diction = dict()
                self.placeholder = template.placeholder
                # Loop: creating dictionary with correct data based on Lnd in template.List_items
                for value in self.template.list_items:
                    self.diction.update({self.test2[value]['location']: self.test2[value][self.template.data_area]})
                    self.listcontinent.append(self.test2[value]["location"])  # Adding the land to list. USe for Listbox
                break
        return existing  # return value of exist check

    def create_location_data_diction(self):
        """
        Creates a dictionary with the wanted information from json
        :return: True if worked else False which mean something doesn't fit with the json and template
        """
        if self.create_value_diction():  # calling the method create_value_diction if True next step executed
            self.listelements = dict()
            # Loop which crete teh dictionary
            for i in self.listcontinent:
                self.listbox.insert("end", i)
                self.x_cords_list = list()
                self.total_Cases_list = list()
                self.new_case_list = list()
                self.stringency_index = list()
                self.total_deaths_list = list()
                self.new_deaths_list = list()
                self.new_cases_smoothed_list = list()
                dumylist = list()
                # Loop to create internal data for processing from json data converting string to Datetime object
                for item in self.x_cords_list:
                    dumylist.append(datetime.datetime.strptime(item, "YYYY-MM-DD"))
                self.x_cords_list = dumylist.copy()
                del dumylist
                # Loop to create internal data for processing from json data
                for item in self.diction[i]:
                    self.x_cords_list.append(item["date"])
                    try:
                        self.total_Cases_list.append(item['total_cases'])
                    except:
                        self.total_Cases_list.append(self.placeholder)
                    try:
                        self.new_case_list.append(item['new_cases'])
                    except:
                        self.new_case_list.append(self.placeholder)
                    try:
                        self.stringency_index.append(item['stringency_index'])
                    except:
                        self.stringency_index.append(self.placeholder)
                    try:
                        self.total_deaths_list.append(item['total_deaths'])
                    except:
                        self.total_deaths_list.append(self.placeholder)
                    try:
                        self.new_deaths_list.append(item['new_deaths'])
                    except:
                        self.new_deaths_list.append(self.placeholder)
                    try:
                        self.new_cases_smoothed_list.append(item['new_cases_smoothed'])
                    except:
                        self.new_cases_smoothed_list.append(self.placeholder)
                    # Adding the created information in internal list
                    self.listelements.update({i: list([
                        {"date": self.x_cords_list.copy()}, {"total_cases": self.total_Cases_list.copy()},
                        {"new_cases": self.new_case_list.copy()}, {"stringency_index": self.stringency_index.copy()},
                        {"total_deaths": self.total_deaths_list.copy()}, {"new_deaths": self.new_deaths_list.copy()},
                        {"new_cases_smoothed": self.new_cases_smoothed_list.copy()}])})

            self.draw_list = self.listelements.copy()
            return True  # Returns True to signal next phase can start
        return False  # False if the json was not found or something went wrong

    def get_draw_value(self, value):
        """
        returns the selected Data set for view
        :param value: identifier of the selection
        :return: dictionary with selected Data set
        """
        valuedict = dict()
        for name in self.template.graph_data.items():
            try:
                for item in self.draw_list[value]:  # Loop: selecting the correct data based on keyword
                    try:
                        if item[name[1]]:
                            valuedict.update({name[1]: item[name[1]]})  # Adding the correct value
                            break
                    except:
                        pass
            except:
                pass
        return valuedict.copy()

    def get_json_key(self, filename):
        """
        returns the value of json identifier in json for checking
        :param filename: returns the key value of loaded json
        :return:Json identifier
        """
        self.test2 = dict()
        self.test2 = self.loading_template(filename)  # loading json in internal variable
        return self.test2.keys()

    def exist(self, json_key, template=mc.Template()):
        """
        Methode to check if template is the correct version for this json
        :param json_key: json key from json
        :param template:  template from template.json
        :return: True i correct Template else False
        """
        if str(json_key) == template.get_template_key():
            return True
        else:
            return False

    def loading_template(self, filename=""):
        """
        Loading a template file
        :param filename: Name of fiel which should be loaded
        :return: json from file
        """
        with open(filename, "r") as file:
            return json.load(file)


def startup(application_param=None, solo=False):
    """
    for executing the application
    :param application_param: if main there is a controller already initialized
    :param solo: if executed in another code as solo application
    :return: True False to identify fi everything went correctly
    """
    if application_param == None:
        application = Controller()
    else:
        application = application_param
    if application.create_value_diction():  # If worked(True) next step
        if application.create_location_data_diction():  # If worked(True) next step
            if solo:  # if external executed as none main
                application.root.mainloop()
            return True  # Return True only if everything went correctly
        else:  # if something went wrong during the data initialization
            print("Could not initialize data!\n\rSomething went wrong with the json Data")
            return False

    else:  # if something went wrong during startup initialization
        print("Could not initialize Program! \n\rSomething went wrong during the initialization.")
        return False


def main():
    """Application start routine if code is executed as main application"""
    application = Controller()  # initialization of controller
    if startup(application):
        application.root.mainloop()  # starting Application
    else:
        del application  # if something went wrong deleting Application


if __name__ == "__main__":  # execute Application only if executed as main application. else needed to start manuel
    main()
