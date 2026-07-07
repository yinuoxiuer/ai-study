#!/usr/bin/python
# author luke

import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
#unpack实现转置的效果
t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

#取出来英国的youtube评论数和喜欢数,第1列是like数，第3列是comment数

t_uk=t_uk[t_uk[:,1]<=250000] #筛选like数小于等于250000的视频
print(t_uk.shape)
t_uk_like=t_uk[:,1]

t_uk_comment = t_uk[:,-1]

plt.figure(figsize=(20,8),dpi=80)
#打印横轴纵轴标签
plt.xlabel("like")
plt.ylabel("comment")
plt.scatter(t_uk_like,t_uk_comment)  #画散点图,观察横轴和纵轴的关系

plt.show()