import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 加载数据
data = pd.read_csv('D:\科研\ICAN挑战杯\scripts\prian\processed-data\processed_S006.csv')  
# 特征和标签
X = data[['Ax', 'Ay', 'Az']].values
y = data['label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
import torch.nn as nn

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

model = SimpleNN()
import torch.optim as optim

criterion = nn.CrossEntropyLoss()  
optimizer = optim.Adam(model.parameters(), lr=0.001) 

X_train_tensor = torch.FloatTensor(X_train)
y_train_tensor = torch.LongTensor(y_train)
X_test_tensor = torch.FloatTensor(X_test)
y_test_tensor = torch.LongTensor(y_test)


num_epochs = 100
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad() 

   
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    
    
    loss.backward()
    optimizer.step()  

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')
model.eval() 
with torch.no_grad():
    test_outputs = model(X_test_tensor)
    _, predicted = torch.max(test_outputs, 1)
    accuracy = (predicted == y_test_tensor).float().mean()
    print(f'Accuracy: {accuracy:.4f}')
torch.save(model.state_dict(), 'model.pth')