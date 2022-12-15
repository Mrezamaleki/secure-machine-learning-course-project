import numpy as np
import pandas as pd
import sns as sns
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns
import matplotlib.pyplot as plt

cwd = os.getcwd()
path = os.path
pjoin = path.join

train_df = pd.read_csv(pjoin(cwd, 'data', 'X_train.csv'))

# print(var)

# enc = OneHotEncoder(handle_unknown='ignore')
# categorical_columns = ['urban']
# var[enc.get_feature_names_out()] = pd.DataFrame(enc.fit_transform(var[categorical_columns]).toarray(),
#                                                 columns=enc.get_feature_names_out())
# var.drop(categorical_columns, axis=1, inplace=True)
# print(var)

pca = PCA(n_components=1)
# pca = PCA(n_components=0.98, svd_solver='full')
result = pca.fit_transform(train_df)
print('explained variance covered by the PC=', pca.explained_variance_ratio_)
print('PC1=\n', result)


# ax = sns.heatmap(pcamodel.components_,
#                  cmap='YlGnBu',
#                  yticklabels=[ "PCA"+str(x) for x in range(1,pca.transform(var)+1)],
#                  xticklabels=list(x.columns),
#                  cbar_kws={"orientation": "horizontal"})
# ax.set_aspect("equal")

# corr = train_df.corr()
# print(sns.heatmap(corr))
# plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')