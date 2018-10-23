"""class Author"""
from libs.build import Build
from libs.funcs import Find
from libs.funcs import str_check_elem


class Author(object):
    """object Author to represent the author data structure"""

    def __init__(self, elem_auth):
        self.__obj = {}
        ns = {}
        ns['ns'] = Find(r'{(.+)}', str(elem_auth.tag)).group(1)
        self.__is_valid = False
        res = str_check_elem(elem_auth, "ns", "Name", ns)
        if res[1]:
            self.__name = res[0]
            self.__obj['_Author__name'] = "Name"

        res = str_check_elem(elem_auth, "ns", "LangID", ns)
        if res[1]:
            self.__lang_id = res[0]
            self.__obj['_Author__lang_id'] = "LangID"

        res = str_check_elem(elem_auth, "ns", "PartNumber", ns)
        if res[1]:
            self.__part_number = res[0]
            self.__obj['_Author__part_number'] = "PartNumber"

        build_elem = elem_auth.find("ns:Build", namespaces=ns)
        if build_elem is not None:
            self.__build = Build(build_elem)

        self.__is_valid = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_string(self):
        """print the Author info's"""
        if self.__is_valid:
            return "Author:\n\tName: %s\n\t%s\n\tLangId: %s\n\tPartNumber: %s" % (
                self.__name, self.__build.to_string(), self.__lang_id, self.__part_number)
        else:
            return "No Author info"

    @property
    def name(self):
        """name property"""
        return self.__name

    @name.setter
    def name(self, val):
        """name setter"""
        self.__name = val

    @property
    def lang_id(self):
        """lang_id getter"""
        return self.__lang_id

    @property
    def is_valid(self):
        """is_valid getter"""
        return self.__is_valid

    @property
    def part_number(self):
        """part_number getter"""
        return self.__part_number

    @property
    def build(self):
        """build getter"""
        return self.__build

    def read(self, el_author):
        """read Author from element author"""
        if el_author is not None:
            ns = {}
            ns['ns'] = Find(r'{(.+)}', str(el_author.tag)).group(1)
            self.__is_valid = True
            self.__lang_id = el_author.find("ns:LangID", namespaces=ns).text
            self.__part_number = el_author.find(
                "ns:PartNumber", namespaces=ns).text
            self.__name = el_author.find("ns:Name", namespaces=ns).text
            self.__build.read(el_author.find("ns:Build", namespaces=ns))

    def to_json(self):
        """to json def"""
        if self.__is_valid:
            b = vars(self)
            js = ""
            for a in self.__obj:
                if a == '_Author__build':
                    js += '%s,' % self.__build.to_json()
                else:
                    js += '"{0}": "{1}",'.format(self.__obj[a], b[a])
            return '"Author":{ %s }' % js[:-1]
