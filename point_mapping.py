import cv2
import os
import numpy as np
from read_xml import *
from config_foot import *
# from config_head import *

class PointMapping(object):
    def __init__(self, tgt_imgs_path, ori_xml_path, matrix):
        self.tgt_imgs_path = tgt_imgs_path   #'./v5/time_same_2'
        self.ori_xml_path = ori_xml_path
        self.matrix = matrix
    
    def box2centroid(self, box):
        xcor = int((box[0] + box[2]) / 2)
        ycor = int((box[1] + box[3]) / 2)
        centroid = np.float32([xcor, ycor]).reshape(-1, 1, 2)
        return centroid 
    
    def mapping(self):
        ori_xml_names = [xml[:-4] for xml in os.listdir(self.ori_xml_path) if not xml.startswith('.')]
        tgt_img_files = sorted([img for img in os.listdir(self.tgt_imgs_path) if not img.startswith('.')])
        video = cv2.VideoWriter(vis_video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, size) 
        print('Writing mapping points into the video...')
        for img_file in tgt_img_files:
            img_path = os.path.join(self.tgt_imgs_path, img_file)
            frame = cv2.imread(img_path)
            if img_file[:-4] in ori_xml_names :
                xml_path = os.path.join(self.ori_xml_path, '{}.xml'.format(img_file[:-4]))
                _, all_boxes, _ = parse_ann(xml_path)
                for box in all_boxes:
                    mapped_x, mapped_y = cv2.perspectiveTransform(self.box2centroid(box), self.matrix)[0][0]
                    frame = cv2.circle(frame, (int(mapped_x), int(mapped_y)), 20, (233, 0, 0), -1)
                video.write(frame)
            else:
                video.write(frame)