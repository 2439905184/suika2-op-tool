import os
path_now = os.getcwd()
img_path = "op/"
bgm_file = "eden_op.ogg"
#文件名前缀
img_file_qz = "Image"
img_frame_start = 1
fps = 25
#请自行调整每张图片暂留时间 引擎fps为60
frame_stay = 0.02 #0.016666 格式工厂按0.02
output = "txt/op.txt"
#一共多少个图片
frames = 6829
file = open(output,"w+")
file.write("@bg black.png \n")
file.write("@bgm "+bgm_file+"\n")
#暂停对节奏
file.write("@wait 3 \n")
for i in range(frames):
    file.write("@bg "+img_path+img_file_qz+str(img_frame_start)+".png"+"\n")
    file.write("@wait "+str(frame_stay)+"\n")
    img_frame_start +=1
file.write("@click")
file.close()
