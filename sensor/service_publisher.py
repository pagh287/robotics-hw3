#!/usr/bin/env python
import rospy
from common_msgs.srv import AddTwoNum, AddTwoNumRequest

rospy.init_node('service_publisher')
rospy.wait_for_service('add_two_number')
requester = rospy.ServiceProxy('add_two_number', AddTwoNum)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count = 0
while count < 30:
    req = AddTwoNumRequest(a=count, b=count/2)
    res = requester(req)
    print "request:", req.a, req.b, "response:", res.sum
    if count % 10 == 0:
        req = AddTwoNumRequest(a=count, b=count*2)
        res = requester(req)
        print count, "seconds passed. -----------"

    rate.sleep()
    count += 1
