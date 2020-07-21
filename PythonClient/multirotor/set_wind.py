import setup_path
import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

client.armDisarm(True)

# Set wind to (20,0,0) in NED (forward direction)
print("Setting wind to (20,0,0)")
wind = airsim.Vector3r(20, 0, 0)
client.simSetWind(wind)

# Takeoff or hover
landed = client.getMultirotorState().landed_state
if landed == airsim.LandedState.Landed:
    print("taking off...")
    client.takeoffAsync().join()
else:
    print("already flying...")
    client.hoverAsync().join()

time.sleep(5)

# Set wind to (0,25,0) in NED (towards right)
print("Setting wind to (0,25,0)")
wind = airsim.Vector3r(0, 25, 0)
client.simSetWind(wind)

time.sleep(5)

# Set wind to 0
print("Resetting wind to (0,0,0)")
wind = airsim.Vector3r(0, 0, 0)
client.simSetWind(wind)
