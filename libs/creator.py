"""class Creator"""
from libs.funcs import Find
from libs.funcs import int_check_elem, str_check_elem
from libs.version import Version


class Creator(object):
    """class Lap to create all data for a lap"""

    def __init__(self, c_elem):
        self.__is_valid = False

        if c_elem is not None:
            self.__obj = {}
            ns = {}
            ns['ns'] = Find(r'{(.+)}', str(c_elem.tag)).group(1)
            # ns['xsi'] = Find(r'{(.+)}',str(c_elem.attrib[0])).group(1)
            for i in c_elem.attrib:
                ns['xsi'] = Find(r'{(.+)}', str(i)).group(1)
            self.__type = c_elem.attrib["{%s}type" % ns['xsi']]
            if self.__type:
                self.__obj['_Creator__type'] = "Type"

            res = str_check_elem(c_elem, "ns", "Name", ns)
            if res[1]:
                self.__name = res[0]
                self.__obj['_Creator__name'] = "Name"

            res = int_check_elem(c_elem, "ns", "UnitId", ns)
            if res[1]:
                self.__unit_id = res[0]
                self.__obj['_Creator__unit_id'] = "UnitId"

            res = int_check_elem(c_elem, "ns", "ProductID", ns)
            if res[1]:
                self.__product_id = res[0]
                self.__obj['_Creator__product_id'] = "ProductID"

            version_elem = c_elem.find("ns:Version", namespaces=ns)
            if version_elem is not None:
                self.__version = Version(version_elem)
            self.__is_valid = True

    @property
    def version(self):
        """property version getter"""
        if self.__version is not None:
            return self.__version
        else:
            return None

    def to_string(self):
        """print the Creator info's"""
        if self.__is_valid:
            return "Creator:\n\tName: %s\n\tUnitId: %d\n\tProductID: %d\n\tVersion: %s" % (
                self.__name, self.__unit_id, self.__product_id, self.__version.to_string())
        else:
            return "No Creator info"

    def to_json(self):
        """to json def"""
        js = ""
        if self.__is_valid:
            b = vars(self)
            for a in self.__obj:
                js += '"{0}": "{1}",'.format(self.__obj[a], b[a])
            # for lap in self.__laps:
            #     js += '%s,' % lap.to_json()
            if self.__version is not None:
                js = '%s "Version": { %s},' % (js, self.__version.to_json())
            js = '"Creator":{ %s }' % js[:-1]
        return js
