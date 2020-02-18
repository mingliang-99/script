# -*-coding:utf-8-*-
import os, sys, time, subprocess
import json
import xlsxwriter,xlrd
#xlwt 列最大支持256 由于数据比较多 使用xlswirter

def file_json_to_dict(path):
    file = open(curve_file, 'r+')
    json_data = file.read()
    json_dict = json.loads(json_data)
    #print (json_str)
    file.close
    return json_dict

if __name__ == "__main__":
    
    parm_len = len(sys.argv)
    print ("parm_len=" + str(parm_len))
    if parm_len < 3:
       print ("python3 create_excel.py xxx.excel xxx.json")
       sys.exit(-1)

    curve_file = sys.argv[1]
    excel_file = sys.argv[2]
    print ("curve_file=" + (curve_file))
    print ("excel_file=" + (excel_file))
  
    workbook = xlsxwriter.Workbook(excel_file)     #创建工作簿
    worksheet = workbook.add_worksheet("curve")            #创建工作表

    json_size = 0
    json_dict = file_json_to_dict(curve_file)
    print ("json_size = ",(json_dict['size']))
    json_size = (json_dict['size'])
    data_array = json_dict['data']

    duration_ms = 0
    bandwidth_kbps = 0
    latency_ms = 0
    i = 1
    for i in range(json_size):
        duration_ms = data_array[i]['duration_ms']
        worksheet.write(i, 0, duration_ms)
        bandwidth_kbps = data_array[i]['bandwidth_kbps']
        worksheet.write(i, 1, bandwidth_kbps)
        latency_ms = str(data_array[i]['latency_ms'])
        print ("index=",i,"duration=",str(duration_ms),"bandwidth=",str(bandwidth_kbps),"latency_ms"+str(bandwidth_kbps))


    workbook.close()
    # for data_single in data_array:
    #     if data_single.has_key('duration_ms'):
    #         duration_ms = data_single['duration_ms'].decode().encode('utf8')
    #         print ("duration_ms",duration_ms)
    #     if data_single.has_key('bandwidth_kbps'):
    #         bandwidth_kbps = data_single['bandwidth_kbps'].decode().encode('utf8')
    #     if data_single.has_key('latency_ms'):
    #         latency_ms = data_single['latency_ms'].decode().encode('utf8')        

#    file = open(curve_file, 'r+')
 #   json_data = file.read()
 #   json_str = json.dumps(json_data)
 #   print (json_str)


    #contends_arr = str(contends).split('},{')
    #for i in range(len(contends_arr)):
    #    file.write(contends_arr[i])
    #    file.write('\n')

    #file.close()
    #get_contends_arr(contends)
  
    #cmd = "python tools/transform.py --srcfile=\"{}\" --despath=\"{}\" --title=\"{}\" --artist=\"{}\" --album=\"{}\" --comment=\"v1.0\" --channel=\"{}\"".format(srcfile, dstpath, title, artist, album, channel)

    #print(cmd)
    
    #ret = execute_cmd(cmd)

    #print(ret)