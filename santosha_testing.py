import detect


# !python detect.py
# --source ../Road_Sign_Dataset/images/test/
# --weights runs/train/yolo_road_det/weights/best.pt
# --conf 0.25
# --name yolo_road_det


save_dir = detect.run(
    source='yolov5/images/test',
    weights='yolov5/runs/train/yolo_pantry_packaging_v22/weights/best.pt',
    name='yolo_pantry_packaging_v22',
    #view_img=True,
    #save_dir = 'yolov5/runs/detect/yolo_pantry_packaging_v22/1',
    save_csv=True,
    save_txt=True
)
print(save_dir)
print('done')