import base64
from ultralytics import YOLO
import cv2
import os

model = YOLO('./best.pt')


def doDetect(iamge_path):
    # Run batched inference on a list of images or directories
    result=model.predict(iamge_path,save=True,save_txt=True,save_conf=True,show_labels=True,show_conf=True)
    for i in result:
        print("i",i)
        iamge_name=iamge_path.split('/')[-1]
        detected_image_path=os.path.join(i.save_dir,iamge_name)
        #将这个图片转为base64编码
        with open(detected_image_path,"rb") as f:
            base64_data = base64.b64encode(f.read())
            base64_str = str(base64_data, "utf-8")
            result = {"image": base64_str}
        #读取i.save_dir下的txt文件
        
        #textname为iamge_name去掉后缀，加上txt
        dot_index = iamge_name.rfind(".")
        if dot_index != -1:  # 确保找到了点号
            filename_without_extension = iamge_name[:dot_index]
        else:
            filename_without_extension = iamge_name
        txt_path=os.path.join(i.save_dir+"/labels",filename_without_extension+'.txt')
        #打开这个text文件，判断有多少行
        line=0
        with open(txt_path,'r') as f:
            for _ in f.readlines():
                line+=1
        
        
            
        return {
            "image": base64_str,
            "damage_count":line
        }
    

    

    
