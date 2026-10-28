# Auditor de Contraseñas

Herramienta de línea de comandos escrita en Python que evalúa la fortaleza
de una contraseña y genera contraseñas seguras. Proyecto de aprendizaje
orientado a ciberseguridad.

## Funcionalidades

- **Auditoría de contraseñas**: analiza longitud y tipos de caracteres
  (minúsculas, mayúsculas, números, símbolos).
- **Puntaje de 0 a 100** con clasificación: Muy débil, Débil, Media,
  Fuerte o Muy fuerte.
- **Recomendaciones** personalizadas según las debilidades detectadas.
- **Generador de contraseñas** con el módulo `secrets` (aleatoriedad
  criptográfica).
- **Menú interactivo** para usar todas las funciones.
- La contraseña auditada **nunca se almacena ni se muestra en pantalla**
  (se lee con `getpass`).

## Requisitos

- Python 3.8 o superior. Sin librerías externas: solo módulos de la
  biblioteca estándar (`getpass`, `secrets`, `string`).

## Cómo ejecutarlo

```
py main.py
```

## Ejemplo de uso

```
===== AUDITOR DE CONTRASEÑAS =====
1. Auditar una contraseña
2. Generar una contraseña segura
3. Salir
Elige una opción (1-3): 1

Tu password tiene 14 caracteres
{'minusculas': True, 'mayusculas': True, 'numeros': True, 'simbolos': True}
Puntaje: 90/100
Nivel: Contrasena es muy fuerte
- ¡Excelente! No hay mejoras obvias.
```

## Qué aprendí con este proyecto

- Funciones, parámetros y valores por defecto.
- Condicionales, bucles `for` y `while`, y diccionarios.
- Diferencia entre `print` y `return`.
- Aleatoriedad criptográfica con `secrets` (y por qué no usar `random`
  para seguridad).
- Menús interactivos y refactorización.
- Flujo de trabajo con Git y GitHub: commit, pull, merge y push.

## Mejoras futuras

- Garantizar al menos un carácter de cada tipo en el generador.
- Manejo de errores con `try/except` para entradas inválidas.
- Detectar contraseñas comunes (listas de contraseñas filtradas).
- Calcular entropía real y comparar con librerías como `zxcvbn`.

## Aviso

Herramienta con fines educativos. El puntaje es una aproximación
simplificada y no sustituye un gestor de contraseñas ni buenas prácticas
de seguridad.

## Licencia

MIT
