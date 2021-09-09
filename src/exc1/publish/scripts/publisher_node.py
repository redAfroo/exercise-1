#!/usr/bin/env python

import rospy
from std_msgs.msg import String



def talk_to_me():
    pub = rospy.Publisher("kanbour", String, queue_size=10) 
    
    #forsta argumentet ar namnet pa topic
    #andra argumentet ar typ av message

    rospy.init_node("publisher_node", anonymous=True)
    rate = rospy.Rate(20)
    rospy.loginfo('publisher node')
    while not rospy.is_shutdown():
        
        for x in range(1,100,4):        
            msg = str(x) #+ "     ---- %s" %rospy.get_time()
            pub.publish(msg)
            print(msg)
            rate.sleep()
        #msg= "hello Omar - %s" %rospy.get_time()
        
            
        #pub.publish(msg)
        #print(msg)
        #rate.sleep()
        #print("heello")


if __name__ == '__main__':
    try:
        talk_to_me()

    except rospy.ROSInterruptException:
        pass
