import json, numpy as np

f = open("scripts/non-processed data/rec_7/HandPose_691077791.txt")
data = json.load(f)
f.close()


skeletons = data.copy()
duration = skeletons.pop('recID')
skeletons.pop('timestamp')

#remove frames with weird coordinates
threshold = 100
cursor = 0
for id,skeleton in enumerate(skeletons):
    for temp_cursor in range(duration):
        if(abs(skeletons[skeleton]['handPose']['Wrist'][temp_cursor]['x']) > threshold):
            continue
        elif(abs(skeletons[skeleton]['handPose']['Wrist'][temp_cursor]['y']) > threshold):
            continue
        elif(abs(skeletons[skeleton]['handPose']['Wrist'][temp_cursor]['z']) > threshold):
            continue
        else:
            if (temp_cursor > cursor):
                cursor = temp_cursor
            break


with open('deneme.skeleton', 'w') as f:
    
    f.write(str(duration - cursor))
    f.write('\n')
    for timestep in range(cursor,duration):
        f.write(str(len(skeletons)))
        f.write('\n')
        for id,skeleton in enumerate(skeletons):
            if (timestep == cursor):
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