import cv2, time, pandas
from datetime import datetime

first_frame=None #FOR STORING THE BASE PICTURE
status_list=[None,None] #FOR STORING THE STATUS (OBJECT ENTERING STATUS 0 TO 1, OBJECT LEAVING THAT IS STATUS 1 TO 0)
times=[]
df=pandas.DataFrame(columns=["Start","End"]) #creating the dataframe structure

video=cv2.VideoCapture(0) #TURN ON THE WEBCAM

while True: # SERIES OF FRAMES TILL WE TYPE Q FOR QUITTING (SERIES OF FRAMES IS A VIDEO)
    check, frame = video.read() # capture the first frame
    status=0 # FOR SHOWING THERE IS NO MOTION
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0) # THIS IS FOR THE CURRENT FRAME , THIS ACTUALLY BLURS THE IMAGE MEANS SMOOTHING DOWN THE IMAGE . DEFAULT ACCEPTED NUMBERS ARE GIVEN

    if first_frame is None: #CONVERT THE FIRST FRAME TO GREY SCALE
        first_frame=gray
        continue # CONTINUE TO THE BEGINNING OF THE LOOP (TO STORE ONLY ONE FRAME )

    #COMPARING THE TWO FRAMES (BASE AND CURRENT FRAME ) AND MAKING A DELTA FRAME
    delta_frame=cv2.absdiff(first_frame,gray)

    # CREATING THRESHOLD AND SETTING VALUES FOR CONTOURS AND USING THRESH_BINARY METHOD
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # WHY 1 ? THE THRESHOLD METHOD RETURNS A TOUPLE TO ACCESS THE SECOND ELEMENT OF THE TOUPLE WHICH CORRESPONDS TO THE FRAME VALUES WE WROTE [1]

    # SMOOTHING DOWN THE THRESHOLD FRAME (BY REMOVING THE BLACK HOLES IN THE WHITE CONTOURS)
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) #ITERATING 2 TIMES TO THE THRESHOLD FRAME

    #THERE ARE TWO METHODS FOR CONTOURS findcontours and drawcontours(for drawing contours on the image)
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# FINDING THE CONTOURS IN THE THRESHOLD IMAGE AND STORING THEM IN THE TOUPLE

    #FILTERING OUT THE contours
    for contour in cnts:
        if cv2.contourArea(contour) < 10000: # DEPENDING ON WHAT OBJECT TO CAPTURE ADJUST THE PIXELS
            continue # CONTINUE TO THE BEGINNING OF THE FOR LOOP AGAIN -> MEANS THAT GO TO THE SECOND CONTOUR AND IF GREATER THEN MOVE ON AND DRAW THE RECTANGLE ON THAT CONTOUR
        status=1 # WHEN FOUND THE OBJECT CHANGE THE status

        # CREATING RECTANGLE
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)

    status_list=status_list[-2:]

# for recording the time of the moving object when status chances from 0 to 1 and 1 to 0 and append in the times list
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    #SHOWING FRAMES , PRESS Q TO QUIT THE VIDEO
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1) #WAIT TILL THE KEY IS PRESSED

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv") # CREATING A CSV TO PLOT GRAPH

video.release() #RELEASE THE WECAM
cv2.destroyAllWindows # DESTROYING ALL FRAMES
