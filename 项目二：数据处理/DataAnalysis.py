import pandas as pd

# 读取数据
df = pd.read_csv('data/titanic.csv')

# 1. 统计乘客人数
total_passengers = len(df)
print(f"乘客总人数: {total_passengers}")

# 2. 统计男女乘客人数及比例
sex_counts = df['Sex'].value_counts()
male_count = sex_counts.get('male', 0)
female_count = sex_counts.get('female', 0)
total = male_count + female_count
male_ratio = male_count / total * 100
female_ratio = female_count / total * 100

print(f"男性乘客人数: {male_count}")
print(f"女性乘客人数: {female_count}")
print(f"男性比例: {male_ratio:.2f}%")
print(f"女性比例: {female_ratio:.2f}%")

# 3. 计算大于35岁人员的姓名
over_35 = df[df['Age'] > 35]
names_over_35 = over_35['Name'].tolist()
print("大于35岁的人姓名:")
for name in names_over_35:
    print(name)

# 4. 计算平均票价
average_fare = df['Fare'].mean()
print(f"平均票价: {average_fare:.2f}")
