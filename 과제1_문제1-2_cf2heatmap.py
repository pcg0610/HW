import matplotlib.pyplot as plt
import numpy as np

# define data and label
data = [[976, 0, 0, 0, 6, 18, 0],
        [0, 997, 0, 0, 3, 0, 0],
        [1, 0, 982, 0, 0, 6, 11],
        [1, 2, 2, 995, 0, 0, 0],
        [14, 0, 0, 0, 975, 11, 0],
        [17, 0, 0, 0, 5, 978, 0],
        [0, 0, 3, 0, 0, 0, 997]]

data.reverse()

label = ['angry', 'disgusted', 'fearful',
         'happy', 'neutral', 'sad', 'surprised']

# set plot
plt.figure(layout='tight')
plt.pcolor(data, cmap='summer')
plt.xticks(np.arange(0.5, len(label)), label)  # 개수, 데이터
plt.yticks(np.arange(0.5, len(label)), sorted(label, reverse=True))

# 비율 추가
for i in range(len(label)):
    for j in range(len(label)):
        plt.text(i+0.5, j+0.5, data[i][j]/sum(data[i]),
                 ha='center', va='center')

plt.xlabel('Estimated Label', fontsize=14)
plt.ylabel('True Label', fontsize=14)

plt.colorbar()
plt.show()
