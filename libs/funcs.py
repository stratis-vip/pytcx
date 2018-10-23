# -*- coding: utf-8 -*-
#!/usr/bin/env python -tt
"""All the functions"""

import re

def Find(pat, text):
    """Search a pattern "pat" in the text \"text\""""
    m = re.search(pat, text, re.DOTALL)
    if m:
        return m
    else:
        return None

def FindAll(pat, text):
    """Search a pattern "pat" in the text \"text\""""
    m = re.findall(pat, text, re.DOTALL)
    if m:
        return m
    else:
        return None

def str_check_elem(elem, namespace, tag, ns):
    """Checks an element "elem" wich is at the form ns:tag, where ns = "namespace" and
    tag = "tag. the last "ns" is a dictionary with namespaces. It used to get ns['ns'] element.
    When there is more depth, use ns ="" and put the ns value in the tag.
    F.e str_check_elem(element, "", .ns:alfa/ns1:bita", ns).
    Returns string"""
    if namespace is not None and namespace != "":
        temp = elem.find("%s:%s" % (namespace, tag), namespaces=ns)
    else:
        temp = elem.find(tag, namespaces=ns)
    if temp is None:
        return (None, False)
    else:
        return (temp.text, True)

def int_check_elem(elem, namespace, tag, ns):
    """Checks an element "elem" wich is at the form ns:tag, where ns = "namespace" and
    tag = "tag. the last "ns" is a dictionary with namespaces. It used to get ns['ns'] element.
    When there is more depth, use ns ="" and put the ns value in the tag.
    F.e str_check_elem(element, "", .ns:alfa/ns1:bita", ns).
    Returns int"""
    res = str_check_elem(elem, namespace, tag, ns)
    if res[0] is not None and res != "":
        return (int(res[0]), True)
    else:
        return (None, False)

def float_check_elem(elem, namespace, tag, ns):
    """Checks an element "elem" wich is at the form ns:tag, where ns = "namespace" and
    tag = "tag. the last "ns" is a dictionary with namespaces. It used to get ns['ns'] element.
    When there is more depth, use ns ="" and put the ns value in the tag.
    F.e str_check_elem(element, "", .ns:alfa/ns1:bita", ns).
    Returns float"""
    res = str_check_elem(elem, namespace, tag, ns)
    if res[0] is not None and res != "":
        return (float(res[0]), True)
    else:
        return (None, False)
