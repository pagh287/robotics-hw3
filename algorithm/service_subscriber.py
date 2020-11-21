#!/usr/bin/env python
import rospy
from common_msgs.srv import AddTwoNum, AddTwoNumResponse

def service_callback(request):
    response = AddTwoNumResponse(sum=request.a * request.b)
    print "request data:", request.a, request.b, ", response:", response.sum
    return response

rospy.init_node('service_subscriber')
service = rospy.Service('add_two_number', AddTwoNum, service_callback)
rospy.spin()
