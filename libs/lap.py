"""class Lap"""
from libs.funcs import Find
from libs.funcs import float_check_elem, int_check_elem, str_check_elem
from libs.trackpoint import TrackPoint


class Lap(object):
    """class Lap to create all data for a lap"""

    def __init__(self, lap_elem):
        ns = {}
        ns['ns'] = Find(r'{(.+)}', str(lap_elem.tag)).group(1)
        self.__is_valid = True
        self.__obj = {}
        self.__track_points = []

        self.__start_time = lap_elem.attrib['StartTime']
        if self.__start_time:
            self.__obj['_Lap__start_time'] = "StartTime"

        res = float_check_elem(lap_elem, "ns", "TotalTimeSeconds", ns)
        if res[1]:
            self.__total_time_seconds = res[0]
            self.__obj['_Lap__total_time_seconds'] = "TotalTimeSeconds"

        res = float_check_elem(lap_elem, "ns", "DistanceMeters", ns)
        if res[1]:
            self.__distance_meters = res[0]
            self.__obj['_Lap__distance_meters'] = "DistanceMeters"

        res = float_check_elem(lap_elem, "ns", "MaximumSpeed", ns)
        if res[1]:
            self.__max_speed = res[0]
            self.__obj['_Lap__max_speed'] = "MaximumSpeed"

        res = int_check_elem(lap_elem, "ns", "Calories", ns)
        if res[1]:
            self.__calories = res[0]
            self.__obj['_Lap__calories'] = "Calories"

        res = int_check_elem(
            lap_elem, "", "ns:AverageHeartRateBpm/ns:Value", ns)
        if res[1]:
            self.__avg_hrm = res[0]
            self.__obj['_Lap__avg_hrm'] = "AverageHeartRateBpm"

        res = int_check_elem(
            lap_elem, "", "ns:MaximumHeartRateBpm/ns:Value", ns)
        if res[1]:
            self.__max_hrm = res[0]
            self.__obj['_Lap__max_hrm'] = "MaximumHeartRateBpm"

        res = str_check_elem(lap_elem, "ns", "Intensity", ns)
        if res[1]:
            self.__intensity = res[0]
            self.__obj['_Lap__intensity'] = "Intensity"

        res = str_check_elem(lap_elem, "ns", "Cadence", ns)
        if res[1]:
            self.__cadence = res[0]
            self.__obj['_Lap__cadence'] = "Cadence"

        res = str_check_elem(lap_elem, "ns", "TriggerMethod", ns)
        if res[1]:
            self.__trigger_method = res[0]
            self.__obj['_Lap__trigger_method'] = "TriggerMethod"

        lista = lap_elem.findall(".ns:Track/ns:Trackpoint", namespaces=ns)
        for a in lista:
            self.__track_points.append(TrackPoint(a))

        ext = lap_elem.find(".ns:Extensions", namespaces=ns)
        if ext is not None:
            for ex in ext:
                ns['ns3'] = Find(r'{(.+)}', str(ex.tag)).group(1)
           
            res = float_check_elem(lap_elem, "", ".ns:Extensions/ns3:LX/ns3:AvgSpeed", ns)
            if res[1]:
                self.__avg_speed = res[0]
                self.__obj['_Lap__avg_speed'] = "AvgSpeed"

            res = int_check_elem(lap_elem, "", ".ns:Extensions/ns3:LX/ns3:MaxBikeCadence", ns)
            if res[1]:
                self.__max_bike_cadence = res[0]
                self.__obj['_Lap__max_bike_cadence'] = "MaxBikeCadence"
            
            res = int_check_elem(lap_elem, "", ".ns:Extensions/ns3:LX/ns3:Steps", ns)
            if res[1]:
                self.__steps = res[0]
                self.__obj['_Lap__steps'] = "Steps"



    @property
    def start_time(self):
        """property start_time getter"""
        return self.__start_time

    def to_json(self):
        """to json def"""
        js = ""
        if self.__is_valid:
            b = vars(self)
            for a in self.__obj:
                js += '"{0}": "{1}",'.format(self.__obj[a], b[a])
            tpoints = ""
            for track in self.__track_points:
                tpoints += '%s,' % track.to_json()[13:]
            js += '"TrackPoints": [%s]' % tpoints[:-1]
            js = '"Lap":{ %s }' % js
        return js
