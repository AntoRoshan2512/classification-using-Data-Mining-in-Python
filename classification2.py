import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

pina = pd.read_excel("D:\python\power quality dataset2.xlsx")
print(pina.head())

feature_cols + ['Max','Min','Std','Mean']
X = pina[feature_vols]
y = pina.classification

X_train, X_test, y_train, y_test =  train_test_split(X,y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier(max_depth=5)

clf1=clf.fit(X_train,y_train)

y_pred = clf1.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


from matplotlib import pyplot as plt
from sklearn import tree

fig = plt.figure()

tree.plot_tree(clf1)
plt.show()
fig.savefig("decision_tree.png")