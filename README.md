# Flask REST API con MySQL

Este es un proyecto de API REST utilizando Flask y MySQL como base de datos. Está estructurado siguiendo buenas prácticas para facilitar la escalabilidad y el mantenimiento.

## Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Realiza las migraciones de base de datos:

```bash
flask db init
```

```bash
flask db migrate -m "Initial migration"
```

```bash
flask db upgrade
```

## Ejecuta el servidor:

```bash
python run.py
```