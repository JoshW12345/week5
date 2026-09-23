import pybullet as p
import pybullet_data
import time

client = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.81)

plane_id = p.loadURDF("plane.urdf")

robot_start_position = [0,0,2]

robot_start_orientation = p.getQuaternionFromEuler([0,0,0])

robot_id = p.loadURDF("r2d2.urdf", robot_start_position, robot_start_orientation)

print("Connection ID:", client)
print("plane ID:", plane_id)

box_half_extents = [.5,.5,.5]

box_collision = p.createCollisionShape(p.GEOM_BOX, halfExtents=box_half_extents)

box_visual = p.createVisualShape(p.GEOM_BOX, halfExtents=box_half_extents, 
                                 rgbaColor =[1,0,0,1])

box_position = [2,0,.3]

box_id = p.createMultiBody(baseMass=1, baseCollisionShapeIndex=box_collision,
                           baseVisualShapeIndex=box_visual,
                           basePosition = box_position)

box_position = [2,0,3]


def create_box(

 position,

 half_extents,

 color,

 mass=0

):

 collision_shape = p.createCollisionShape(

 p.GEOM_BOX,

 halfExtents=half_extents

 )



 visual_shape = p.createVisualShape(

 p.GEOM_BOX,

 halfExtents=half_extents,

 rgbaColor=color

 )



 object_id = p.createMultiBody(

 baseMass=mass,

 baseCollisionShapeIndex=collision_shape,

 baseVisualShapeIndex=visual_shape,

 basePosition=position

 )



 return object_id

obstacle_1 = create_box (position=[5,5,20],half_extents=[.5,.5,10],color=[.5,0,.5,1],mass=1)

obstacle_2 = create_box (position=[9,15,10],half_extents=[3,.6,6],color=[1,0,1,1],mass=1)

obstacle_3 = create_box (position=[3,3,3],half_extents=[4,4,4],color=[1,1,1,1],mass=1)

obstacle_4 = create_box (position=[7,7,7],half_extents=[10,10,10],color=[1,0,0,1],mass=1)

for x_position in range(-4, 5, 2):
 create_box(
position=[x_position, 3, 0.5],
half_extents=[0.4, 0.4, 0.5],
color=[0.5, 0.2, 0.8, 1]
)

 
for height in range(2, 7):
 create_box(
position=[3, 0, height],
half_extents=[0.25, 0.25, 0.25],
color=[1, 0.5, 0, 1],
mass=1
)



while p.isConnected():
    p.stepSimulation()
    time.sleep(1/240)
