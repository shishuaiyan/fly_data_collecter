# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 09:38:38 2018

@author: Weilit
"""
import time

f_date = input('请输入日期: ')
while (len(f_date) != 4  or f_date[0] not in ['0','1']):
    f_date = input('请正确输入四位数日期: ')

user_input = ''
print_str = ['','','']
launch_times = [0,0,0]
t_flys = [0,0,0]
engine_start_hot_times = [0,0,0]
engine_hot_times = [0,0,0]
engine_start_times = [0,0,0]
engine_times = [0,0,0]
t_engines = [0,0,0]
str_hot = [0,0,0]
counters = [0,0,0]
gas_start = [0,0,0]
gas_end = [0,0,0]
gas_cost = [0,0,0]

# =============================================================================
# 重要输入：油；准备起飞；起飞；end；余油
# =============================================================================

def collect_data(user_input,f_date):
    global launch_times, print_str, str_hot, gas_start, gas_end, gas_cost
    current_time = time.strftime('%H %M %S',time.localtime(time.time()))
    split_cur = current_time.split(' ')

    if user_input[1:3] == '余油':
        try:
            gas_end[int(user_input[0])-1] = int(user_input[3:])
        except:
            print('油量输入错误。')
        if gas_start[int(user_input[0])-1] and gas_end[int(user_input[0])-1]:
            gas_cost[int(user_input[0])-1] = gas_start[int(user_input[0])-1] - gas_end[int(user_input[0])-1]
        t_engines[int(user_input[0])-1] = engine_hot_times[int(user_input[0])-1]+engine_times[int(user_input[0])-1]
        if str_hot[int(user_input[0])-1] and '热车' not in print_str[int(user_input[0])-1]:
            print_str[int(user_input[0])-1] += str_hot[int(user_input[0])-1]
        print_str[int(user_input[0])-1] += '余油{}L，滞空时间{}分{}秒，发动机运行时间{}分{}秒。'.format(user_input[3:],t_flys[int(user_input[0])-1]//60,t_flys[int(user_input[0])-1]%60,t_engines[int(user_input[0])-1]//60,t_engines[int(user_input[0])-1]%60)
        write_data(print_str[int(user_input[0])-1],user_input[0])
    elif user_input in ['time','时间','t']:
        for i in range(3):
            if launch_times[i]:
                fly_time = int(time.time())-launch_times[i]
                print('{}号无人机飞行时间： {}分钟{}秒'.format(i+1,fly_time//60,fly_time%60))
    elif user_input[1:2] == '油':
        try:
            gas_start[int(user_input[0])-1] = int(user_input[2:])
        except:
            print('油量输入错误。')
        print_str[int(user_input[0])-1] = '初始油量为{}L，'.format(user_input[2:])
    elif user_input[1:] in ['开始热车','热车','热']:
        engine_start_hot_times[int(user_input[0])-1] = int(time.time())
        str_hot[int(user_input[0])-1] = '{:0>2s}:{:0>2s}:{:0>2s}无人机开始热车，'.format(split_cur[0],split_cur[1],split_cur[2])
        #print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}无人机开始热车，'.format(split_cur[0],split_cur[1],split_cur[2])
    elif user_input[1:] in ['热车完毕','完毕','完','热车完成','完成']:
        if engine_start_hot_times[int(user_input[0])-1]:
            engine_hot_times[int(user_input[0])-1] = int(time.time())-engine_start_hot_times[int(user_input[0])-1]
            engine_start_hot_times[int(user_input[0])-1] = 0
        #print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}热车完毕，'.format(split_cur[0],split_cur[1],split_cur[2])
        str_hot[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}热车完毕，'.format(split_cur[0],split_cur[1],split_cur[2])
    elif user_input[1:] in ['准备起飞','准备','准','prepare']:
        if str_hot[int(user_input[0])-1]:
            print_str[int(user_input[0])-1] += str_hot[int(user_input[0])-1]
            str_hot[int(user_input[0])-1] = 0
        engine_start_times[int(user_input[0])-1] = int(time.time())
        print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}准备起飞，'.format(split_cur[0],split_cur[1],split_cur[2])
    elif user_input[1:] in ['离地','起飞','launch']:
        print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}无人机离地，'.format(split_cur[0],split_cur[1],split_cur[2])
        launch_times[int(user_input[0])-1] = int(time.time())
        print('{}号无人机起飞时间： {}'.format(user_input[0],time.strftime('%H %M %S',time.localtime(time.time()))))
    elif user_input[1:3] == '位置':
        if user_input[3] == '1':
            print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}到达位置1(经度：119.2984869，纬度：31.774822，高度：27m)，'.format(split_cur[0],split_cur[1],split_cur[2])
        elif user_input[3] == '2':
            print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}到达位置2(经度：119.2986543，纬度：31.773824，高度：35.5m)，'.format(split_cur[0],split_cur[1],split_cur[2])
        elif user_input[3] == '3':
            print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}到达位置3(经度：119.299151，纬度：31.773188，高度：35.5m)，'.format(split_cur[0],split_cur[1],split_cur[2])
        elif user_input[3] == '4':
            print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}到达位置4(经度：119.2990119，纬度：31.7739545，高度：60m)，'.format(split_cur[0],split_cur[1],split_cur[2])
        else:
            print('输入位置不在预设位置中。')
    elif user_input[1:] in ['返航','返','return']:
        print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}开始返航，'.format(split_cur[0],split_cur[1],split_cur[2])
    elif user_input[1:] in ['落地','降落','着陆','end']:
        fly_time = int(time.time())-launch_times[int(user_input[0])-1]
        fly_time_data = '{}号无人机滞空时间{}分{}秒'.format(int(user_input[0]),fly_time//60,fly_time%60)
        print(fly_time_data)
        print_str[int(user_input[0])-1] += '{:0>2s}:{:0>2s}:{:0>2s}无人机着陆，'.format(split_cur[0],split_cur[1],split_cur[2])
        if engine_start_times[int(user_input[0])-1]:
            engine_times[int(user_input[0])-1] = int(time.time())-engine_start_times[int(user_input[0])-1]
            engine_start_times[int(user_input[0])-1] = 0
        if launch_times[int(user_input[0])-1]:
            t_flys[int(user_input[0])-1] = int(time.time())-launch_times[int(user_input[0])-1]
            launch_times[int(user_input[0])-1] = 0
    else:
        print('未知输入，已记入log。')
    if user_input[0] in ['1','2','3']:
        write_log(current_time,user_input[1:],user_input[0])
    elif user_input[0] in ['t','时']:
        pass
    else:
        print('未指定无人机编号，输入无效。')


def write_log(current_time,log,uav_n):
    #f = open('/storage/emulated/0/1/'+f_date+'_'+uav_n+'_log.txt','a+')
    f = open('C:/Users/Weilit/Desktop/'+f_date+'_'+uav_n+'_log.txt','a+')
    f.write(current_time+' : '+log+'  ,  ')
    f.close()


def write_data(data, uav_n):
    global couners
    counters[int(uav_n)-1] += 1
    #f_p = open('/storage/emulated/0/1/'+f_date+'_'+uav_n+'_data.txt','a+')
    f_p = open('C:/Users/Weilit/Desktop/'+f_date+'_'+uav_n+'_data.txt','a+')
    f_p.write(data+'\n\n')
    f_p.close()
    if gas_cost[int(uav_n)-1]:
        print(' {} 号无人机第 {} 架次，油耗 {} 升，data已写入。'.format(uav_n,counters[int(uav_n)-1],str(gas_cost[int(uav_n)-1])))
    else:
        print(' {} 号无人机第 {} 架次，data已写入。'.format(uav_n,counters[int(uav_n)-1]))

    
while user_input != 'exit':
    user_input = input('请输入： ')
    if user_input:
        if user_input[0] in ['1','2','3','t','时']:
            collect_data(user_input,f_date)
        elif user_input == 'exit':
            pass
        else:
            print('无效输入\n')

        
