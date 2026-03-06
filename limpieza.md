Lo primero que realice con la base de datos es encontrar que 35 variables algunas refieren a datos sociodemograficos como la edad o educación, y otras a cuestiones relacionadas al ambito laboral desde nivel de satisfacción hasta datos de la trayectoria laboral previa. 

1° Cambio  Eliminar 3 columnas por tener el mismo valor en todos los casos
En princio realice una observación de que variables solo tenien un unico valor en cada casp mediante el comando de python df.nunique()
donde encontre que las columnas EmployeeCount, Over18 y StandardHours tienen 1, ? y 80 respectivamente. Por lo que tomo la decisión de eliminarlas de la base de datos mediante el comando df = df.drop(columns=['EmployeeCount','Over18','StandardHours']) 

Se observa mediante el comendo df.T.duplicated() que no hay columnas duplicadas. 

Se evalua que no hay valores faltantes mediante el comando df.isna().mean().sort_values(ascending=False)
ademas se observa que con el comando df.describe(include='all')
Todas las columnas muestran 1470, lo que implica: ✔ No hay valores faltantes (NaN) en estas variables.

Se elimina la columna EmployeeNumber por ser un numero de id. 

Se codifican las variables a binarias 
df['Attrition'] = df['Attrition'].map({'No':0, 'Yes':1})
df['Gender'] = df['Gender'].map({'Male':0, 'Female':1})
df['OverTime'] = df['OverTime'].map({'No':0, 'Yes':1})

Se cambia el tipo de datos de Education, JobInvolvement, PerformanceRating a ordinales 
df['Education'] = pd.Categorical(df['Education'], ordered=True)
df['JobInvolvement'] = pd.Categorical(df['JobInvolvement'], ordered=True)
df['PerformanceRating'] = pd.Categorical(df['PerformanceRating'], ordered=True)

Evaluo que variables deberian ser categoria 
df.select_dtypes('object').columns
y las transformo 
cols = ['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus']
df[cols] = df[cols].astype('category')

Creación de categorias nuevas 
#Construcción de una variable de lealtad. cercano a 1 → carrera concentrada en esta empresa cercano a 0 → mucha movilidad laboral
df["LoyaltyRate"] = df["YearsAtCompany"] / df["TotalWorkingYears"].replace(0, 1)

#Construcción de una variable de Indice de estancamiento. Mientras mas alto más tiempo sin promoción
df["StagnationIndex"] = df["YearsSinceLastPromotion"] / df["YearsAtCompany"].replace(0, 1)

#Creación de variable velocidad de promoción
df["PromotionVelocity"] = df["TotalWorkingYears"] / df["JobLevel"].replace(0, 1)

#Movilidad laboral alto → trabajador muy móvil bajo → carrera estable
df["CareerMobility"] = df["NumCompaniesWorked"] / df["TotalWorkingYears"].replace(0, 1)

#Se comprueba si se genero algún valor Nan 
df[["CareerMobility", "PromotionVelocity", "StagnationIndex", "LoyaltyRate"]].isna().sum()

#correlación punto-biserial
df[["Attrition", "CareerMobility", "PromotionVelocity", "StagnationIndex", "LoyaltyRate"]].corr()

#mapa de calor
import matplotlib.pyplot as plt
corr = df[["Attrition", "CareerMobility", "PromotionVelocity", "StagnationIndex", "LoyaltyRate"]].corr()
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()



