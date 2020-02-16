import cv2
import os
import numpy as np
from read_xml import *
from matplotlib import pyplot as plt


class FindHomography(object):
    def __init__(self, src_xml_path, tgt_xml_path, img4perspective = None):
        self.src_xml_path = src_xml_path   #'./v5/xml_1'
        self.tgt_xml_path = tgt_xml_path
        self.img4perspective = img4perspective
        
    def box2centroid(self, box):
        xcor = int((box[0] + box[2]) / 2)
        ycor = int((box[1] + box[3]) / 2)
        return [xcor, ycor]  
        
    def cal_matrix(self):
        src_xml = sorted([src for src in os.listdir(self.src_xml_path) if not src.startswith('.')])
        tgt_xml = sorted([tgt for tgt in os.listdir(self.tgt_xml_path) if not tgt.startswith('.')])
        src_points = []
        tgt_points = []
        for src_xml_file, tgt_xml_file in zip(src_xml, tgt_xml):
            _, src_boxes, _ = parse_ann(os.path.join(self.src_xml_path, src_xml_file))
            _, tgt_boxes, _ = parse_ann(os.path.join(self.tgt_xml_path, tgt_xml_file))
            for src_box in src_boxes:
                src_points.append(self.box2centroid(src_box))
            for tgt_box in tgt_boxes:
                tgt_points.append(self.box2centroid(tgt_box))
        self.matrix, mask = cv2.findHomography(np.float32(src_points), np.float32(tgt_points))
        return self.matrix
    
    def vis_perspective(self):
        img = cv2.imread(self.img4perspective)
        rows, cols, _ = img.shape
        output = cv2.warpPerspective(img, self.matrix, (cols, rows))
        plt.imshow(output)
        plt.show()