#对语义分割后的结果进行监测
##读取图片
import os
from gray_de import detect
import json
from fit import fit3

#工作路径
current_folder=os.getcwd()
parent = os.path.dirname(current_folder)
grandparent = os.path.dirname(parent)
#print(parent)
#print(grandparent)

folder_img = grandparent+'/data/image'

for filename in os.listdir(folder_img):
    if filename.endswith('.png'):
        data={
            "info":{
                "image_name":'',
                "image_size":[]
            },
            "perception":[
                {
                    "tracker_id": -1,
                    "lanetype": "",
                    "fitlane": {
                        "c0": 0,
                        "c1": 0,
                        "c2": 0,
                        "c3": 0
                    }
                },
                {
                    "tracker_id": -2,
                    "lanetype": "",
                    "fitlane": {
                        "c0": 0,
                        "c1": 0,
                        "c2": 0,
                        "c3": 0
                    }
                },
                {
                    "tracker_id": 1,
                    "lanetype": "",
                    "fitlane": {
                        "c0": 0,
                        "c1": 0,
                        "c2": 0,
                        "c3": 0
                    }
                },
                {
                    "tracker_id": 2,
                    "lanetype": "",
                    "fitlane": {
                        "c0": 0,
                        "c1": 0,
                        "c2": 0,
                        "c3": 0
                    }
                }
            ]

        }
        data['info']["image_name"]=filename
        #print(data)
        print(os.path.splitext(filename)[0])

        # 打印每个png图片的完整路径
        #print(os.path.join(folder_img, filename))
        img_path = os.path.join(folder_img, filename)
        d_result,image_size,line_point=detect(img_path)
        f_result=fit3(line_point)
        print(f_result)
        data['info']["image_size"] = image_size
        #print(data["perception"][0]['tracker_id'])
        if(data["perception"][0]['tracker_id']==-1):
            data["perception"][0]["lanetype"] = d_result[0]['-1']
            data["perception"][0]["fitlane"]['c0'] = f_result['-1'][0]
            data["perception"][0]["fitlane"]['c1'] = f_result['-1'][1]
            data["perception"][0]["fitlane"]['c2'] = f_result['-1'][2]
            data["perception"][0]["fitlane"]['c3'] = 0
        if (data["perception"][1]['tracker_id'] == -2):
            data["perception"][1]["lanetype"] = d_result[0]['-2']
            data["perception"][1]["fitlane"]['c0'] = f_result['-2'][0]
            data["perception"][1]["fitlane"]['c1'] = f_result['-2'][1]
            data["perception"][1]["fitlane"]['c2'] = f_result['-2'][2]
            data["perception"][1]["fitlane"]['c3'] = 0
        if (data["perception"][2]['tracker_id'] == 1):
            data["perception"][2]["lanetype"] = d_result[0]['+1']
            data["perception"][2]["fitlane"]['c0'] = f_result['+1'][0]
            data["perception"][2]["fitlane"]['c1'] = f_result['+1'][1]
            data["perception"][2]["fitlane"]['c2'] = f_result['+1'][2]
            data["perception"][2]["fitlane"]['c3'] = 0
        if (data["perception"][3]['tracker_id'] == 2):
            data["perception"][3]["lanetype"] = d_result[0]['+2']
            data["perception"][3]["fitlane"]['c0'] = f_result['+2'][0]
            data["perception"][3]["fitlane"]['c1'] = f_result['+2'][1]
            data["perception"][3]["fitlane"]['c2'] = f_result['+2'][2]
            data["perception"][3]["fitlane"]['c3'] = 0

        #print(d_result)
        with open(grandparent+'/result/'+os.path.splitext(filename)[0]+'.json', 'w+') as f:
            json_str = json.dumps(data, indent=4, separators=(',', ': '))
            f.write(json_str)
##转换灰度值


##监测分布

##保存json预测


##读取直线进行拟合



##保存拟合结果json
