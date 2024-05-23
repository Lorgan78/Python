#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime


class Template:
    """
    Template for preparing the json data
    """

    def __init__(self, exist=False, dumb=dict(), multilist=0):
        """
        Initialization of Class
        :param exist: True -> Template exist | False new Template for creating  Template for a new json
        :param dumb: contains the json dictionary if Exist == True, else empty dictionary
        :param multilist: If the template is for a multi Graph display   Todo: Implementing missing params for universal use of  Application
        """
        if exist:  # for existing template. initialise with data from Template.json
            self.__init_existing_template__(json_key=dumb["list"], multilist=multilist, list_items=dumb["list"],
                                            dataarea=dumb["data_area"], depths=dumb["depth"],
                                            data_depths=dumb["data_depth"], graph_data=dumb["graph_data"],
                                            placeholder=dumb["placeholder"])
        else:
            self.__init_empty_template__()  # Empty Template

    def __init_existing_template__(self, json_key, multilist, list_items, dataarea, depths, data_depths, graph_data, placeholder):
        """
        internal methode for initialisation
        :param json_key: identifier for the json
        :param multilist:  if multigraph
        :param list_items: values for selecting the wanted data
        :param dataarea: name of the json field which holds the wanted information
        :param depths: how many step  there are to go until findig data
        :param data_depths: how deep the data lays
        :param graph_data: which data should be printed on graph
        :return: Object
        """
        self.__json_key__ = json_key
        self.__multilist__ = multilist
        self.__list_items__ = str(list_items).replace(" ", "").replace("dict_keys", "").replace("([", "").replace("]",
                                                                                                                  "").replace(
            "(", "").replace(")", "").replace("'", "").split(",")
        self.__data_area__ = dataarea
        self.__data_depth__ = data_depths
        self.__depth__ = depths
        self.__data_list__ = list()
        self.__graph_data__ = graph_data
        self.__placeholder__ = placeholder

    def __init_empty_template__(self):
        """
        Creating an empty templated
        :return: empty object
        """
        self.__json_key__ = ""
        self.__multilist__ = list()
        self.__list_items__ = list()
        self.__data_area__ = "0"
        self.__depth__ = 0
        self.__data_depth__ = 0
        self.__placeholder__= 0

    def get_template_key(self):
        """
        getter methode to get template key identifier
        optional use of json_key
        :return: template identifier as string
        """
        return self.json_key

    @property
    def data_depth(self):
        """
        :return: Data depth int
        """
        return self.__data_depth__

    @data_depth.setter
    def data_depth(self, value):
        """
        :param value: int
        :return:True if valide value else  False
        """
        if value.isdigit():
            self.__data_depth__ = value
            return True
        return False

    @data_depth.deleter
    def data_depth(self):
        """
        :return: True if deleted
        """
        del self.__data_depth__
        return True

    @property
    def json_key(self):
        """
        Json key/ template key identifier
        :return: string containing template key identifier
        """
        return str(self.__json_key__)

    @json_key.setter
    def json_key(self, value):
        """
        :param value: identifier for json. keys of the template
        :return: True if value is accepted else false
        """
        if len(value) > 0:
            self.__data_depth__ = value
            return True
        return False

    @json_key.deleter
    def json_key(self):
        """
        :return: True after deleting data
        """
        del self.__json_key__
        return True

    @property
    def multilist(self):
        """
        :return: Multi_key Bool
        """
        return self.__multilist__

    @multilist.setter
    def multilist(self, value):
        """
        :param value: Identifier for multi plot Bool True or False
        :return: True if value is accepted else false
        """
        if isinstance(value[0], bool):
            self.__multilist__ = value
            return True
        return False

    @multilist.deleter
    def multilist(self):
        """
        :return: True if deleted
        """
        del self.__multilist__
        return True

    @property
    def list_items(self):
        """
        :return: List() with identifier for json keywords
        """
        return self.__list_items__

    @list_items.setter
    def list_items(self, value):
        """
        :param value: Type list() identifier List for json keywords
        :return: True if value is accepted else false
        """
        if type(value) == type(list()):
            self.list_items = value
        return False

    @list_items.deleter
    def list_items(self):
        """
        :return: True if deleted
        """
        del self.__list_items__
        return True

    @property
    def data_area(self):
        """
        :return: List() with identifier to select wanted data in json
        """
        return self.__data_area__

    @data_area.setter
    def data_area(self, value):
        """
        :param value: List() with the identifier for data in json
        :return: True if value is accepted else false
        """
        if type(value) == type(list()):
            self.__data_area__ = value
        return False

    @data_area.deleter
    def data_area(self):
        """
        :return: True if deleted
        """
        del self.__data_area__
        return True
        self.__data_list__ = list()

    @property
    def data_list(self):
        """
        :return: List with selected data from json
        """
        return self.__data_list__

    @data_list.setter
    def data_list(self, value):
        """
        :param value: List() with selected data from json
        :return: True if value is accepted else false
        """
        if type(value) == type(list()):
            self.__data_list__ = value
            return True
        return False

    @data_list.deleter
    def data_list(self):
        """
        :return: True if deleted
        """
        del self.__data_list__
        return True

    @property
    def graph_data(self):
        """
        :return: List() containing the data for plotting at graph
        """
        return self.__graph_data__

    @graph_data.setter
    def graph_data(self, value):
        """
        :param value: List()  containing the data for plotting at Graph
        :return: True if value is accepted else false
        """
        if type(value) == type(list()):
            self.__graph_data__ = value
            return True
        return False

    @graph_data.deleter
    def graph_data(self):
        """
        :return: True if deleted
        """
        del self.__graph_data__
        return True

    @property
    def placeholder(self):
        """
        :return: placeholder  containing value for replacing missing datapoint
        """
        return self.__placeholder__

    @placeholder.setter
    def placeholder(self, value):
        """
        :param value: Value which replace incorrect or not existing value type digit
        :return: True if value is accepted else false
        """
        if value.isdigit():
            self.__placeholder__ = value
            return True
        return False

    @placeholder.deleter
    def placeholder(self):
        """
        :return: True if deleted
        """
        del self.__placeholder__
        return True


# Todo: finishing formatter class
from matplotlib.ticker import Formatter


# Custom formatter class
class CustomFormatter(Formatter):
    """
    customized Formatter
    """

    def __init__(self, ax: any, datelist=list()):
        super().__init__()
        self.set_axis(ax)

    def __call__(self, x, pos=None, datelist=list()):
        # Find the axis range
        vmin, vmax = self.axis.get_view_interval()

        # Use the range to define the custom string
        if vmax - vmin > 300:
            print(pos)
            if pos % 300 == 0:
                # date = datetime.datetime.strptime(datelist[pos], "%Y-%m-%d")
                return pos
            return
        return f"[{vmin:.1f}, {vmax:.1f}]: {x:.1f}"
