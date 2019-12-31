from django.shortcuts import render
# Import relevant libraries
import math

# Create your views here.
def index(request):
    return render(request, 'index.html')

def calDistance(request):
    lat1 = float(request.GET["lat1"])
    long1 = float(request.GET["long1"])
    lat2 = float(request.GET["lat2"])
    long2 = float(request.GET["long2"])

    # Convert latitude and longitude to spherical coordinates in radians
    degrees_to_radian = math.pi/180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1) * degrees_to_radian
    phi2 = (90.0 - lat2) * degrees_to_radian

    # theta = longitude
    theta1 = long1 * degrees_to_radian
    theta2 = long2 * degrees_to_radian

    # Compute spherical distance from spherical coordinates
    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2)) + (math.cos(phi1) * math.cos(phi2))

    arc = math.acos(cos)

    # Distance in miles
    dist_miles = (arc * 3960) + "miles"
    # Distance in kilometers
    dist_kms = arc * 6373 + "km"

    return render(request, "index.html", {"dist_miles": dist_miles, "dist_kms": dist_kms})


