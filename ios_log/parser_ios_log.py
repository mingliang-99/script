# -*-coding:utf-8-*-
import os, sys, time, subprocess

def execute_cmd(cmd):
    try:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        retcode = p.returncode
        if retcode != 0:
            return False, stderr, retcode
        else:
            return True, stdout, retcode
    except Exception, err:
        print("Oops, an error happened!:{}".format(err))
        return False, err

def get_contends_arr(contends):
    contends_arr_new = []
    contends_arr = str(contends).split('},{')
    for i in range(len(contends_arr)):
        print contends_arr[i]
        contends_arr_new.append(temp_str.replace('"', ''))
        #if (contends_arr[i].__contains__('[')):
        #    index = contends_arr[i].rfind('[')
        #    temp_str = contends_arr[i][index + 1:]
        #    if temp_str.__contains__('"'):
        #        contends_arr_new.append(temp_str.replace('"', ''))
            # print(index)
        # print(contends_arr[i])
    return contends_arr_new

def get_contends(path):
    with open(path) as file_object:
        contends = file_object.read()
    return contends

if __name__ == "__main__":
    
    srcfile = sys.argv[1]
    dstfile = sys.argv[2]

    file = open(dstfile, 'a')
    
    print srcfile
    print dstfile

    contends = get_contends(srcfile)
    contends_arr = str(contends).split('},{')
    for i in range(len(contends_arr)):
        file.write(contends_arr[i])
        file.write('\n')

    file.close()
    #get_contends_arr(contends)
  
    #cmd = "python tools/transform.py --srcfile=\"{}\" --despath=\"{}\" --title=\"{}\" --artist=\"{}\" --album=\"{}\" --comment=\"v1.0\" --channel=\"{}\"".format(srcfile, dstpath, title, artist, album, channel)

    #print(cmd)
    
    #ret = execute_cmd(cmd)

    #print(ret)


