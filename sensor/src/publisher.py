#!/usr/bin/env python
import rospy
from common_msgs.srv import MulTwoNum, MulTwoNumRequest

rospy.init_node('publisher')
rospy.wait_for_service('mul_two_number')
requester = rospy.ServiceProxy('mul_two_number', MulTwoNum)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count = 0
while count < 100:
    res = requester(req)
    print count, "request:", req.a, req.b, "response:", res.sum
    if count % 10 == 0:
        print count, "seconds pased"
    rate.sleep()
    count += 1

