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

flag_left = 1
flag_right = 1
#maybe change this as a command line argument?
setup_id = 1

#copying number
copying = 50
for c in range(1,copying):

    for activity_id,activity in enumerate(activity_data): #activity id derken toplam kac tane recording var onu diyorum

        start_time = activity['Start']
        stop_time = activity['Stop']
        if (activity['Label'] == 'bg'):
            label = 1
        elif (activity['Label'] == ' bg'):
            label = 1
        elif (activity['Label'] == ' grab'):
            label = 2
        
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

        if (activity_id + c < 10):
            filename = 'data/S00{}C00{}P001R001A00{}.skeleton'.format(setup_id,activity_id + c,label)
        elif (activity_id + c < 100):
            filename = 'data/S00{}C0{}P001R001A00{}.skeleton'.format(setup_id,activity_id + c,label)
        else:
            filename = 'data/S00{}C{}P001R001A00{}.skeleton'.format(setup_id,activity_id + c,label)
        
        with open(filename, 'w') as f:
            f.write(str(stop_time - cursor))

            
            for timestep in range(cursor,stop_time):
                f.write('\n')
                f.write(str(len(skeletons)))

                if (flag_left):
                        skeletons['leftHand']['handPose'].pop('None')
                        flag_left = 0
                if (flag_right):
                        skeletons['rightHand']['handPose'].pop('None')
                        flag_right = 0
                
                for id,skeleton in enumerate(skeletons):
                    f.write('\n')
                    f.write(str(id+1))
                    f.write('\n')
                    f.write(str(len(skeletons[skeleton]['handPose'])))
                    for i, joint in enumerate(skeletons[skeleton]['handPose']):
                        f.write('\n')
                        f.write(str(skeletons[skeleton]['handPose'][joint][timestep]['x']))
                        f.write(' ')
                        f.write(str(skeletons[skeleton]['handPose'][joint][timestep]['y']))
                        f.write(' ')
                        f.write(str(skeletons[skeleton]['handPose'][joint][timestep]['z']))