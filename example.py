from config_foot import *
# from config_head import *
from find_matrix import *
from point_mapping import *

if __name__ == '__main__':

    FH = FindHomography(src_xml_path, tgt_xml_path, img4perspective)        
    matrix = FH.cal_matrix()
    FH.vis_perspective()
    
    PM = PointMapping(tgt_imgs_path, ori_xml_path, matrix)
    PM.mapping()