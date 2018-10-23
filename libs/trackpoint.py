"""class Lap"""
from libs.funcs import Find
from libs.funcs import float_check_elem, int_check_elem, str_check_elem


class TrackPoint(object):
    """class Lap to create all data for a lap"""

    def __init__(self, t_elem):
        ns = {}
        ns['ns'] = Find(r'{(.+)}', str(t_elem.tag)).group(1)
        self.__obj = {}
        self.__is_valid = True
        res = str_check_elem(t_elem, "ns", "Time", ns)
        if res[1]:
            self.__time = res[0]
            self.__obj['_TrackPoint__time'] = "Time"

        res = float_check_elem(t_elem, "", "ns:Position/ns:LatitudeDegrees", ns)
        if res[1]:
            self.__lat_degrees = res[0]
            self.__obj['_TrackPoint__lat_degrees'] = "LatitudeDegrees"

        res = float_check_elem(t_elem, "", "ns:Position/ns:LongitudeDegrees", ns)
        if res[1]:
            self.__lon_degrees = res[0]
            self.__obj['_TrackPoint__lon_degrees'] = "LongitudeDegrees"

        res = float_check_elem(t_elem, "ns", "AltitudeMeters", ns)
        if res[1]:
            self.__alt_meters = res[0]
            self.__obj['_TrackPoint__alt_meters'] = "AltitudeMeters"

        res = float_check_elem(t_elem, "ns", "DistanceMeters", ns)
        if res[1]:
            self.__distance_meters = res[0]
            self.__obj['_TrackPoint__distance_meters'] = "DistanceMeters"
        
        res = int_check_elem(t_elem, "", "ns:HeartRateBpm/ns:Value", ns)
        if res[1]:
            self.__hrm = res[0]
            self.__obj['_TrackPoint__hrm'] = "HeartRateBpm"

        res = int_check_elem(t_elem, "ns", "Cadence", ns)
        if res[1]:
            self.__cadence = res[0]
            self.__obj['_TrackPoint__cadence'] = "Cadence"

        res = str_check_elem(t_elem, "ns", "SensorState", ns)
        if res[1]:
            self.__sensor_state = res[0]
            self.__obj['_TrackPoint__sensor_state'] = "SensorState"


        ext = t_elem.find(".ns:Extensions", namespaces=ns)

        if ext is not None:
            for ex in ext:
                ns['ns3'] = Find(r'{(.+)}', str(ex.tag)).group(1)

            res = float_check_elem(t_elem, "", ".ns:Extensions/ns3:TPX/ns3:Speed", ns)
            if res[1]:
                self.__speed = res[0]
                self.__obj['_TrackPoint__speed'] = "Speed"

            res = int_check_elem(t_elem, "", ".ns:Extensions/ns3:TPX/ns3:RunCadence", ns)
            if res[1]:
                self.__run_cadence = res[0]
                self.__obj['_TrackPoint__run_cadence'] = "RunCadence"

    def to_json(self):
        """to json def"""
        js = ""
        if self.__is_valid:
            b = vars(self)
            for a in self.__obj:
                js += '"{0}": "{1}",'.format(self.__obj[a], b[a])
            # for lap in self.__laps:
            #     js += '%s,' % lap.to_json()
            js = '"Trackpoint":{ %s }' % js[:-1]
        return js
