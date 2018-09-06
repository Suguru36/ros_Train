

#!/use/bin/env python
import rospy
from std_msg.msg import String
def callback(message):
    rospy.loginfo("I heard %s", message.date)

rospy.init_node('listener')
sub = rospy.Subscriber('chatter' , String, callback)
rospy.spin()
