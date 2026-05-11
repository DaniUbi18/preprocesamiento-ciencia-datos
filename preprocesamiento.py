
import pandas as pd

# Crear datos de ejemplo
datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "Ana", None],
    "Edad": [20, 21, None, 20, 22],
    "Ciudad": ["Quito", "Guayaquil", "Cuenca", "Quito", "Loja"]
}

# Crear DataFrame
df = pd.DataFrame(datos)

print("DataFrame original:")
print(df)

# Eliminar valores nulos
df = df.dropna()

print("\nDataFrame sin valores nulos:")
print(df)

# Eliminar duplicados
df = df.drop_duplicates()

print("\nDataFrame sin duplicados:")
print(df)
