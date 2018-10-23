"""class Build"""

from libs.version import Version
from libs.funcs import Find


class Build(object):
    """object Build to represent the author data structure"""

    def __init__(self, elem_build):
        self.__obj = {}
        ns = {}
        ns['ns'] = Find(r'{(.+)}', str(elem_build.tag)).group(1)
        self.__is_valid = False

        version_elem = elem_build.find("ns:Version", namespaces=ns)
        if version_elem is not None:
            self.__version = Version(version_elem)
            self.__is_valid = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_string(self):
        """print the Build info's"""
        if self.__is_valid:
            return "Build %s" % self.__version.to_string()
        else:
            return "No Build info"

    def to_json(self):
        """to json def"""
        if self.__is_valid:
            b = vars(self)
            js = '%s,' % self.__version.to_json()
            for a in self.__obj:
                js += '"{0}": "{1}",'.format(self.__obj[a], b[a])
            return '"Build":{ %s }' % js[:-1]

    def read(self, el_build):
        """read build from element build"""
        if el_build is not None:
            ns = {}
            ns['ns'] = Find(r'{(.+)}', str(el_build.tag)).group(1)
            self.__is_valid = True
            self.__version.read(el_build.find("ns:Version", namespaces=ns))
