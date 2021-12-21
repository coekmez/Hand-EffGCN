import json, numpy as np

f = open("scripts/non-processed data/rec_7/HandPose_691077791.txt")
hand_data = json.load(f)
f.close()

f = open('scripts/non-processed data/rec_7/activityLabels.txt')
activity_data = json.load(f)
f.close()


skeletons = hand_data.copy()
duration = skeletons.pop('recID')
skeletons.pop('timestamp')
flag = 1
#maybe change this as a command line argument?
setup_id = 1

for activity_id,activity in enumerate(activity_data):
    start_time = activity['Start']
    stop_time = activity['Stop']
    if (activity['Label'] == 'bg'):
        label = 0
    elif (activity['Label'] == ' bg'):
        label = 0
    elif (activity['Label'] == ' grab'):
        label = 1
    
    duration = stop_time - start_time

    #remove frames with weird coordinates
    threshold = 100
    cursor = start_time
    for skeleton_id,skeleton in enumerate(skeletons):
        for temp_cursor in range(start_time,stop_time):
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

    
    with open('data/S00{}C001P001R00{}A00{}.skeleton'.format(setup_id,activity_id,label), 'w') as f:
        f.write(str(duration))
        f.write('\n')
        
        for timestep in range(cursor,stop_time):
            f.write(str(len(skeletons)))
            f.write('\n')
            
            for id,skeleton in enumerate(skeletons):
                if (flag):
                    skeletons[skeleton]['handPose'].pop('None')
                    flag = 0
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