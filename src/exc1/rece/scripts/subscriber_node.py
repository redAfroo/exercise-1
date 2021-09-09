#!/usr/bin/env python 

import rospy
from std_msgs.msg import String

def callback(data):
    #rospy.loginfo("recieved DATA: %s ", data.data)
    #print(data.data)
    pub = rospy.Publisher("kthfs_result", String, queue_size = 10)
    q = 0.15
    new_msg = str(int(data.data)/q)
    rate = rospy.Rate(20)
    pub.publish(new_msg)
    rate.sleep()
    

def listener():
    
    rospy.init_node("subscriber_node", anonymous = True)
    rospy.Subscriber("kanbour", String, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
       

    except rospy.ROSInterruptException:
        pass
