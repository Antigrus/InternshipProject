import numpy as np
import matplotlib.pyplot as plt

def generate_gradient(X, theta, y):
    sample_count = X.shape[0]
# 计算梯度，采用矩阵计算 1/m ∑(((h(x^i)-y^i)) x_j^i)
    return (1./sample_count)*X.T.dot(X.dot(theta)-y)

def get_training_data(file_path):
    orig_data = np.loadtxt(file_path, skiprows=1)  # 忽略第一行的标题
    cols = orig_data.shape[1]
    return (orig_data, orig_data[:, :cols - 1], orig_data[:, cols - 1:])

# 初始化θ数组
def init_theta(feature_count):
    return np.ones(feature_count).reshape(feature_count, 1)

def gradient_descending(X, y, theta, alpha):
    Jthetas= []  # 记录代价函数J(θ)的变化趋势，验证梯度下降是否运行正确
    # 计算损失函数，等于真实值与预测值差的平方。(y^i-h(x^i))^2
    Jtheta = (X.dot(theta)-y).T.dot(X.dot(theta)-y)
    index = 0
    gradient = generate_gradient(X, theta, y) #计算梯度
    while not np.all(np.absolute(gradient) <= 1e-5):  #梯度小于0.00001时计算结束
        theta = theta - alpha * gradient
        gradient = generate_gradient(X, theta, y) #计算新梯度
        # 计算损失函数，等于真实值与预测值差的平方(y^i-h(x^i))^2
        Jtheta = (X.dot(theta)-y).T.dot(X.dot(theta)-y)
        if (index+1) % 10 == 0:
            Jthetas.append((index, Jtheta[0]))  #每10次计算记录一次结果
        index += 1
    return theta,Jthetas

#展示损失函数变化曲线图
def showJTheta(diff_value):
    p_x = []
    p_y = []
    for (index, sum) in diff_value:
        p_x.append(index)
        p_y.append(sum)
    plt.plot(p_x, p_y, color='b')
    plt.xlabel('steps')
    plt.ylabel('loss funtion')
    plt.title('step - loss function curve')
    plt.show()

def showlinercurve(theta, sample_training_set):
    x, y = sample_training_set[:, 1], sample_training_set[:, 2]
    z = theta[0] + theta[1] * x
    plt.scatter(x, y, color='b', marker='x',label="sample data")
    plt.plot(x, z, 'r', color="r",label="regression curve")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('liner regression curve')
    plt.legend()
    plt.show()

# 读取数据集
training_data_include_y, training_x, y = get_training_data("data/02/lr2_data.txt")
# 获取数据集数量及特征数
sample_count, feature_count = training_x.shape
# 定义学习步长α
alpha = 0.01
# 初始化Ɵ
theta = init_theta(feature_count)
# 获取最终的参数Ɵ及代价
result_theta,Jthetas = gradient_descending(training_x, y, theta, alpha)
# 打印参数
print("w:{}".format(result_theta[0][0]),"b:{}".format(result_theta[1][0]))
showJTheta(Jthetas)
showlinercurve(result_theta, training_data_include_y)