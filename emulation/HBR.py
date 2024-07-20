import torch
import torch.nn as nn

# 定义你的神经网络结构
def HBR(dataframe):
    class SimpleNN(nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc1 = nn.Linear(3, 64)
            self.fc2 = nn.Linear(64, 32)
            self.fc3 = nn.Linear(32, 150)

        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = torch.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    # 创建模型实例
    model = SimpleNN()

    # 加载模型权重
    model.load_state_dict(torch.load('model.pth'))
    model.eval()  # 将模型设置为评估模式，这会关闭 Dropout 等层的影响
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    # 加载测试数据
    test_data = dataframe

    # 假设测试数据结构与训练时相同，提取特征
    X_test = test_data[['Ax', 'Ay', 'Az']].values

    # 使用训练时的标准化器进行数据预处理
    scaler = StandardScaler()
    X_test = scaler.fit_transform(X_test)
    

    # 转换为 PyTorch Tensor
    X_test_tensor = torch.FloatTensor(X_test)

    # 模型推理
    with torch.no_grad():
        outputs = model(X_test_tensor)
        _, predicted = torch.max(outputs, 1)

    # predicted 包含了模型的预测结果
    test_data['label'] = predicted.numpy()

    # 将包含预测结果的 DataFrame 写入新的 CSV 文件
    return test_data[['label']]
