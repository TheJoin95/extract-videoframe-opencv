import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut, frameInterval=500, videoStart=0, videoEnd=0):
  vidcap = cv2.VideoCapture(pathIn)
  
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
  duration = frame_count/fps

  print("fps %d" % fps)
  print("duration (seconds) %d" % duration)

  if videoEnd == 0:
    videoEnd = duration

  success,image = vidcap.read()
  success = True

  iteration = 0
  currentDuration = 0

  if(videoStart != 0):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, videoStart*1000)
    currentDuration += videoStart

  while success:
    if (currentDuration >= videoEnd):
      print("Reached the end of interval %d seconds" % videoEnd)
      break

    vidcap.set(cv2.CAP_PROP_POS_MSEC,(iteration*frameInterval))
    success,image = vidcap.read()

    print("Saving " + pathOut + "frame%d.jpg" % iteration)
    cv2.imwrite( pathOut + "frame%d.jpg" % iteration, image)
    iteration = iteration + 1
    currentDuration += (frameInterval / 1000)

if __name__=="__main__":
  extractImages('PATH_TO_VIDEO', 'PATH_TO_DESTINATION_DIR', 500, 0, 10)
