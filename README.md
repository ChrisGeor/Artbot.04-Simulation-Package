# Artbot.04-Simulation-Package

This Package simulates a fully autonomous Differential drive robot(with an optional teleoperational_keyboard script)
,publishing navigation goals, via navigation_stack, using teb_local_planner in a realistic race track
while using a map created by gmapping on first lap for localization with amcl.

running the configuration_gazebo_full.launch file in the differential_robot_2dnav package, will open the simulation with gazebo,
alongside rviz with a built in configuration format for optimal visualization of the raw data in use.
