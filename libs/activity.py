"""class Activity"""
from libs.funcs import Find
from libs.lap import Lap
from libs.creator import Creator
from libs.funcs import str_check_elem


class Activity(object):
    """The main object which keeps the sport activity"""

    def __init__(self, activity):
        """initializing object"""

        self.__obj = {}
        ns = {}
        ns['ns'] = Find(r'{(.+)}', str(activity.tag)).group(1)
        temp = activity.attrib['Sport']
        if not temp:
            self.__is_valid = False
            return
        else:
            self.__sport = temp
            self.__obj['_Activity__sport'] = "Sport"

        res = str_check_elem(activity, "ns", "Id", ns)
        if res[1]:
            self.__sport_id = res[0]
            self.__obj['_Activity__sport_id'] = "Id"
        self.__is_valid = False

        lista = activity.findall("ns:Lap", namespaces=ns)
        if lista is not None:
            self.__laps = []
            for a in lista:
                self.__laps.append(Lap(a))

        creator_elem = activity.find("ns:Creator", namespaces=ns)

        if creator_elem is not None:
            self.__creator = Creator(creator_elem)
        self.__is_valid = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def sport(self):
        """property sport getter"""
        return self.__sport

    @sport.setter
    def sport(self, sport):
        """setter for sport"""
        if sport != self.__sport:
            self.__sport = sport

    @property
    def sport_id(self):
        """property sport_id getter"""
        return self.__sport_id

    @sport_id.setter
    def sport_id(self, sport_id):
        """setter for sport_id"""
        if sport_id != self.__sport_id:
            self.__sport_id = sport_id

    @property
    def laps(self):
        """property laps getter"""
        return self.__laps

    @property
    def creator(self):
        """property creator getter"""
        return self.__creator

    def to_json(self):
        """to json def"""
        js = ""

        if self.__is_valid:

            b = vars(self)
            for a in self.__obj:
                js += '"{0}": "{1}",'.format(self.__obj[a], b[a])
            lap_obj = ""
            # print self.__laps
            for lap in self.__laps:
                lap_obj += '%s,' % lap.to_json()[6:]
            js = '%s "Laps": [%s],' % (js, lap_obj[:-1])
            try:
                if self.__creator is not None:
                    js = '%s "Creator": { %s},' % (
                        js, self.__creator.to_json())
            except AttributeError:
                pass
            js = '"Activity":{ %s }' % js[:-1]
        return js
