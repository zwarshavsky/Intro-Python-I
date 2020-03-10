# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class WayPoint(LatLon):
    def __init__(self,name,lat,lon):
        self.name = name
        LatLon.__init__(self,lat,lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class GeoCache(WayPoint):
    def __init__(self,name,difficulty,size,lat,lon):
        self.difficulty = difficulty
        self.size = size
        WayPoint.__init__(self,name,lat,lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)

if __name__ == "__main__":
    new_waypoint = WayPoint("Catacombs",41.70505,-121.51521)
    print(f'"{new_waypoint.name}", {new_waypoint.lat}, {new_waypoint.lon}')
    print(new_waypoint.__dict__) 
    new_geocache = GeoCache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
    print(new_geocache.__dict__) 