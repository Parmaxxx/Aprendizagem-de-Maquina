import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('../Csv/perfil_clientes.csv', sep=';')

print(df.head())

print(df.info())

print(df.tail())

print(df.describe())

round(df.describe().transpose(),2)

contagem_categorias = df['estado_civil'].value_counts()
print(contagem_categorias)

contagem_categorias.plot.barh()

# Tabela cruzada com outra variável categórica "Região"
pd.crosstab(df['estado_civil'], df['região'])

df.groupby('estado_civil')['idade'].max()

df_duplicated = df[df.duplicated()]
print(df_duplicated)
df.drop_duplicates(inplace=True)


print(df.shape)

df.isnull().sum()

var = df[df['classe_trabalho'].isna()]

df.query('qtde_filhos.isna()')

df.query('salario.isna()')


df.query('estado_civil =="Solteiro" and UF == "MG"')['idade'].mean()

moda = df['classe_trabalho'].mode()[0]
df['classe_trabalho'].fillna(moda, inplace=True)

df.query('index in (61,69)')
df.dropna(subset=['qtde_filhos'],
          inplace=True)

df.query('index in (12,20)')


media = round(df['salario'].mean(),2)

df['salario'].fillna(value=media,
                     inplace=True)

df.query('index in (242,962)')
df.isna().sum()
columns = df.columns
plt.figure(figsize=(20,7))
plt.title('Distribuição das Idades', size=20)
sns.histplot(data=df,
             x='idade',
             bins=25
)
plt.figure(figsize=(20,7))
plt.title('Distribuição dos Salários', size=20)
sns.histplot(data=df,
             x='salario',
             bins=25
)
plt.figure(figsize=(5,3))
plt.title('Gráfico Boxplot', size=20)
sns.boxplot(data=df.query('estado_civil == "Solteiro"'),
             x='idade',
             orient='h'
)
idades_solteiros = df.query('estado_civil == "Solteiro"')
idades_solteiros['idade'].describe()
plt.figure(figsize=(7,5))
plt.title('Gráfico Boxplot', size=10)
sns.boxplot(data=df,
             x='idade',
             y='classe_trabalho',
             orient='h',
             palette='flare'
)

media_estudo = pd.DataFrame(df.groupby(['anos_estudo'])['salario'].mean())

media_estudo.reset_index(inplace=True)
print(media_estudo)
media_estudo.plot.bar()

plt.figure(figsize=(7,5))
plt.title('Gráfico Dispersão', size=10)
sns.scatterplot(data=media_estudo,
                x='anos_estudo',
                y='salario'
)
plt.xlabel('Anos de Estudo')
plt.ylabel('Média dos Salários')

plt.show()

plt.figure(figsize=(10,7))
plt.title('Gráfico Barras', size=10)
sns.countplot(data=df,
             x='escolaridade',
)
plt.xticks(rotation=45, ha='right')

plt.show()

plt.figure(figsize=(10,7))
plt.title('Gráfico Barras', size=10)
sns.barplot(data=media_estudo,
           x='anos_estudo',
           y='salario'
           )

colunas = ['anos_estudo', 'salario', 'qtde_filhos', 'idade']
round(df[colunas].corr(),2)
dados_correlacao = round(df[colunas].corr(),2)
print(dados_correlacao)

plt.figure(figsize=(5,3))
plt.title('Gráfico Heatmap', size=10)
sns.heatmap(data=dados_correlacao,
            cmap='coolwarm',
            linewidths=0.1,
            linecolor='white',
            annot=True
           )
plt.show()

df.head()

df.groupby('escolaridade')['anos_estudo'].mean()
df.groupby(['região','sexo']).agg(
    total=('sexo', 'count'),
    media_idade = ('idade', 'mean')
)
df.groupby(['escolaridade'], as_index=False).agg(
    total=('sexo', 'count'),
    media_salario=('salario', 'mean'),
    mediana=('salario', 'median'),
).round(2)
df.groupby(['região'], as_index=False).agg(
    total=('região', 'count'),
    media_salario=('salario', 'mean'),
    maior_salario=('salario', 'max')
)
