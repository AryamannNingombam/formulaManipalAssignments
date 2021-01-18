#!/usr/bin/env python
import rospy
from task_2.msg import nameAndAge




def callback(msg):
    print(msg)
    print('Name'+ ': '+msg.name+' , Age : ' + str(msg.age))


if __name__ == '__main__':

    rospy.init_node("Output",anonymous=True)
    rospy.Subscriber("three-tier", nameAndAge, callback)
    

    rospy.spin()
