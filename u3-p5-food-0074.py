import matplotlib.pyplot as plt
import pandas as pd

# Johan Paulo Aros Reveles

# 1. Leer el archivo CSV comida pais India
df_food_india = pd.read_csv('indian_food.csv')
print('\n--- DATOS LEÍDOS DESDE CSV 0074 ---')
print(df_food_india)

print('\n--- Mostrando nombre, comida + ingredientes 0074 ---')
recetas = df_food_india[['name', 'ingredients']]
print(recetas)

print('\n--- Tiempo de cocinado mostrar 10 ingredientes con head 0074 ---')
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)

print('\n--- Grafica comida (x) Tiempo cocinado (Y) ---')
print('--- Grafica comida (x) texto a 30 grados ---')
nombre_y_hora.plot.bar(x='name', y='cook_time', rot=30)
plt.title('Comida Tipica india Jaquez 0074')
plt.xlabel('Nombre platillo')
plt.ylabel('Tiempo de cocinado')
plt.show()

# Gráfica de 2 columnas
nombre_y_hora_prep = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora_prep.plot.bar(x='name', rot=30)
plt.title('Grafica de 2 columnas Jaquez 0074')
plt.xlabel('Nombre de platillo')
plt.ylabel('Tiempo de cocinado prep y comida')
plt.show()

# Gráfica apilada
print('\n--- Grafica apiladas una tras otra verticalmente 0074 ---')
nombre_y_hora_prep.plot.bar(x='name', stacked=True, rot=30)
plt.title('Grafica apiladas Jaquez 0074')
plt.xlabel('Nombre de platillo')
plt.ylabel('Tiempo de cocinado prep y comida')
plt.show()
