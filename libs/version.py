"""class Version"""
from libs.funcs import Find, int_check_elem


class Version(object):
    """object Version to represent the author data structure"""

    def __init__(self, elem_version):
        self.__obj = {}

        ns = {}
        ns['ns'] = Find(r'{(.+)}', str(elem_version.tag)).group(1)
        self.__is_valid = False
        res = int_check_elem(elem_version, "ns", "VersionMajor", ns)
        if res[1]:
            self.__v_major = int(res[0])
            self.__obj['_Version__v_major'] = "VersionMajor"

        res = int_check_elem(elem_version, "ns", "VersionMinor", ns)
        if res[1]:
            self.__v_minor = int(res[0])
            self.__obj['_Version__v_minor'] = "VersionMinor"

        res = int_check_elem(elem_version, "ns", "BuildMajor", ns)
        if res[1]:
            self.__b_major = int(res[0])
        self.__obj['_Version__b_major'] = "BuildMajor"

        res = int_check_elem(elem_version, "ns", "BuildMajor", ns)
        if res[1]:
            self.__b_minor = int(res[0])
        self.__obj['_Version__b_minor'] = "BuildMinor"

        self.__is_valid = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return '\"{}\"'.format(self.to_string())

    def to_string(self):
        """print the Version info's"""
        ver = "Version: "
        if self.__is_valid:
            try:
                if self.__v_major is not None:                 
                    ver = "%s%d" % (ver, self.__v_major)
            except AttributeError:
                pass
            try:
                if self.__v_minor is not None:
                    ver = "%s.%d" % (ver, self.__v_minor)
            except AttributeError:
                pass
            try:
                if self.__b_major is not None:
                    ver = "%s.%d" % (ver, self.__b_major)
            except AttributeError:
                pass
            try:
                if self.__b_minor is not None:
                    ver = "%s.%d" % (ver, self.__b_minor)
            except AttributeError:
                pass
        else:
            ver = "No Version info"
        return ver

    def to_json(self):
        """jsonize the object"""
        if self.__is_valid:
            b = vars(self)
            js = ""
            for a in self.__obj:
                js += '"{0}": "{1}",'.format(self.__obj[a], b[a])
            return '"Version":{ %s }' % js[:-1]

    def read(self, el_version):
        """read version from element version"""
        if el_version is not None:

            self.__is_valid = True
            ns = {}
            ns['ns'] = Find(r'{(.+)}', str(el_version.tag)).group(1)
            self.__v_major = int_check_elem(
                el_version, "ns", "VersionMajor", ns)
            self.__v_minor = int_check_elem(
                el_version, "ns", "VersionMinor", ns)
            self.__b_major = int_check_elem(el_version, "ns", "BuildMajor", ns)
            self.__b_minor = int_check_elem(el_version, "ns", "BuildMinor", ns)
