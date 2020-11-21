#!/usr/bin/env python
import rospy
from common_msgs.srv import MulTwoNum, MulTwoNumResponse

def service_callback(request):
    response = MulTwoNumResponse(mul=request.a * request.b)
    print "request data:", request.a, request.b, ", response:", response.sum
    return response

rospy.init_node('sensor')
service = rospy.Service('Mul_two_number', MulTwoNum, common_msgs)
rospy.spin()

