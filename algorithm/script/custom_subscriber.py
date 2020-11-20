#!/usr/bin/env python
import rospy
from topic_custom.msg import TimePose

def callback(msg):
    if msg.pose.x % 7 == 1 
        print "Today is Monday"
    elif msg.pose.x % 7 == 2
        print "Today is Tuesday"
    elif msg.pose.x % 7 == 3
        print "Today is Wednesday"
    elif msg.pose.x % 7 == 4
        print "Today is Thursday"
    elif msg.pose.x % 7 == 5
        print "Today is Friday"
    elif msg.pose.x % 7 == 6
        print "Today is Saturday"
    elif msg.pose.x % 7 == 0
        print "Today is Sunday"


rospy.init_node('custom_subscriber')
sub = rospy.Subscriber('custom_msg', TimePose, callback)
rospy.spin()

