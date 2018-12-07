from vi_env.VehicleIntersection import VehicleIntersection
# noinspection PyUnresolvedReferences
from vi_env.VehicleIntersectionActionSets import SetByRoad, SetByLight, ToggleRoad, ToggleLight, SetExplicitly


action_set = SetByLight()
# action_set = ToggleLight()
# env = VehicleIntersection()
env = VehicleIntersection(action_set=action_set,
                          max_vehicles_on_map=8,
                          vehicles_to_spawn_per_episode=10,
                          road_length=15)

print("A description of the chosen action set: ")
print(action_set.describe())

done = False
ts = 0
trew = 0
while not done:
    action = env.action_space.sample()
    print("Executing action %d" % action)
    state, reward, done, _ = env.step(action)
    ts += 1
    trew += reward
    env.render()
print("Reward is %d after %d timesteps" % (trew, ts))
