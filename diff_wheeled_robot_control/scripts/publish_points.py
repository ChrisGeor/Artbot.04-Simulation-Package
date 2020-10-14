#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



def goal_pose():
	goal_pose = MoveBaseGoal()
	goal_pose.target_pose.header.frame_id = 'base_footprint'
	goal_pose.target_pose.pose.position.x = 3
	goal_pose.target_pose.pose.position.y = 0
	goal_pose.target_pose.pose.position.z = 0
	goal_pose.target_pose.pose.orientation.x = 0
	goal_pose.target_pose.pose.orientation.y = 0
	goal_pose.target_pose.pose.orientation.z = 0
	goal_pose.target_pose.pose.orientation.w = 1

	return goal_pose

#def data_provider():
	
	
#	rospy.Subscriber("/scan",LaserScan,callback)
#	rospy.spin()

#def callback(SensorData):
	
	
	#rate=rospy.Rate(100)
	
	
	
	
#	flag= False
#	counter=0
#	for m in range (100,300):
#		if(SensorData.ranges[m]>3):
#			counter=counter+1
#	if (counter<180):
#
#		for i in range (100,300):
#			if(SensorData.ranges[i]<3):
#				flag=True
#				break
#		if(flag==True):
#			counter1=0
#			counter2=0		
#			for j in range (1,200):
 #               		if(SensorData.ranges[j]<3):counter1=counter1+1
#					
#			for k in range (200,400):
#				if(SensorData.ranges[k]<3):counter2=counter2+1
#						
#			if (counter1>counter2):	
#				
#				
#			elif (counter1<counter2):
#				m
#				
#			else:
#				
#				
#	
#		else:
#			
#			
#	else:		
#		
#			
#		
#		
#			
#
	#rate.sleep()
	
if __name__ == '__main__':

	rospy.init_node('publish_points')
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	client.wait_for_server()	
	
	while True:
			goal = goal_pose()
			client.send_goal(goal)
			client.wait_for_result()
	
	#try:data_provider()
	#except rospy.ROSInterruptException: pass
			
		
				
