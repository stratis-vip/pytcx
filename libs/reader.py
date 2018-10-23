"""class Reader"""

import xml.etree.ElementTree as ET
from libs.funcs import Find
from libs.activity import Activity
from libs.author import Author

SPORTS = {"running": "Running", "cycling": "Cycling",
          "biking": "Cycling", "swimming": "Swimming"}


class Reader(object):
    """object Reader is responsible to open and close a tcx file"""

    def __init__(self, filename):
        self.__fname = filename
        self.__f = None
        self.__data = None
        self.__sport = None
        self.__sport_id = None
        self.__error = ""
        self.__activities = []
        self.__current_activity = 0
        self.__is_readed = False

        self.__author = None
        self.__ns = {}

        self.__open_file__()
        self.__check_tcx__()

    def __close__(self):
        self.__f.close()
        self.__f = None
        self.__data = None
        self.__sport = None
        self.__sport_id = None

    def __open_file__(self):
        """try to open the __fname"""
        import os.path

        if not os.path.isfile(self.__fname):
            self.__error += "File \"%s\" doesn't exists\n" % self.__fname
            self.__f = None
        else:
            try:
                self.__f = open(self.__fname)
            finally:
                pass

    def __check_tcx__(self):
        """Check if "filename" is a valid tcx file"""
        if self.__f is None:
            self.__is_valid = False
            return
        self.__data = self.__f.read(800)
        m = Find(r'<Tr.+e.+\s*<A.+\s*.+Sport="(\w+)">\s*<Id>(.+)</Id>', self.__data)
        if m and m.group():
            self.__sport = get_sport(m.group(1))
            self.__sport_id = m.group(2)
            if self.__sport and self.__sport_id:
                self.__data += self.__f.read()
                self.__is_valid = True
        else:
            self.__error += "File \"%s\" is not a valid TCX file\n" % self.__fname
            self.__close__()

    def read(self):
        """reads the tcx file"""
        if not self.__is_valid:
            return
        try:
            root = ET.fromstring(self.__data)
            self.__ns['ns'] = Find(r'{(.+)}', str(root.tag)).group(1)
            activities = root.findall(
                ".ns:Activities/ns:Activity", namespaces=self.__ns)
            for activity in activities:
                self.__activities.append(Activity(activity))
                if self.__current_activity + 1 < len(activities):
                    self.__current_activity += 1
            auth = root.find("ns:Author", namespaces=self.__ns)
            if auth is not None:
                self.__author = Author(auth)
            self.__is_readed = True
        except ET.ParseError as err:
            self.__data = ""
            self.__is_valid = False
            self.__is_readed = False
            # import pdb; pdb.set_trace()
            self.__error += str(err)

    @property
    def data(self):
        """data getter"""
        return self.__data

    @property
    def sport_id(self):
        """id getter"""
        return self.__sport_id

    @property
    def last_error(self):
        """last_error getter"""
        return self.__error

    @property
    def is_valid(self):
        """is_valid getter"""
        return self.__is_valid

    @property
    def sport(self):
        """sport getter"""
        return self.__sport
    # private
    __is_valid = False

    @property
    def activities(self):
        """activity getter"""
        print("activities %d" % len(self.__activities))
        return self.__activities

    @property
    def author(self):
        """author getter"""
        return self.__author

    def to_json(self):
        """to json def"""
        js = ""
        if self.__is_valid:
            acts = ""
            for activity in self.__activities:
                acts += '%s,' % activity.to_json()[11:]
            js = '"Activities": [%s]' % acts[:-1]
            try:
                if self.__author is not None:
                    js += ',%s' % self.__author.to_json()
            except AttributeError:
                pass
        return '{"TrainingCenterDatabase": {%s}}' % js
    
    def write(self, filename):
        """write json to filename"""
        # import pdb
        # pdb.set_trace()
        if self.__is_valid and self.__is_readed:
            F = open(filename, "w")
            if F is not None:
               F.write(self.to_json())
               F.close()
            else:
                self.__error = 'Error opening "%s" for writing' % filename
        else:
            print (self.__is_valid)


def get_sport(a):
    """Get the sport from tcx description"""
    if a.lower() in SPORTS:
        return SPORTS[a.lower()]
    else:
        return None
