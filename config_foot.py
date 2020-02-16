### video with mapping points###
vis_video_path = 'vis_foot.avi' 
fps = 15
size = (1440, 1440)

### xml path of 2 point lists to calculate the homography matrix ###
src_xml_path = './assets_foot/xml_1'
tgt_xml_path = './assets_foot/xml_2'
img4perspective = './assets_foot/test.jpg'

### map the points to the target images ###
tgt_imgs_path = './assets_foot/time_same_2'
ori_xml_path = './assets_foot/vis_xml/'