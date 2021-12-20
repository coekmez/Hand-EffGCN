import json, numpy as np

f = open("scripts/non-processed data/rec_7/HandPose_691077791.txt")
data = json.load(f)
f.close()


skeletons = data.copy()
duration = skeletons.pop('recID')
skeletons.pop('timestamp')

timestep = 0


with open('deneme.skeleton', 'w') as f:
    
    f.write(str(duration))
    f.write('\n')
    for timestep in range(duration):
        f.write(str(len(skeletons)))
        f.write('\n')
        for id,skeleton in enumerate(skeletons):
            if (timestep == 0):
                skeletons[skeleton]['handPose'].pop('None')
            f.write(str(id+1))
            f.write('\n')
            f.write(str(len(skeletons[skeleton]['handPose'])))
            f.write('\n')
            for i, joint in enumerate(skeletons[skeleton]['handPose']):
                f.write(str(skeletons[skeleton]['handPose'][joint][timestep]['x']))
                f.write(' ')
                f.write(str(skeletons[skeleton]['handPose'][joint][timestep]['y']))
                f.write(' ')
                f.write(str(skeletons[skeleton]['handPose'][joint][timestep]['z']))
                f.write('\n')