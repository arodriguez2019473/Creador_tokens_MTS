# 🩸 Math Token Scripture (MTS)

Sistema de **autenticación experimental** basado en matemáticas duras.
No usa JWT, no expone payloads legibles y no sigue estándares tradicionales.

> *"Aquí no hay usuarios, hay sellos.*
> *Aquí no hay tokens, hay matemáticas."*

---

## ⚙️ ¿Qué es MTS?

**MTS (Math Token Scripture)** es un sistema de seguridad para endpoints que genera **sellos criptográficos** basados en:

* 🔢 Aritmética modular
* 🧮 Exponenciación modular (logaritmo discreto)
* 🔐 Hash criptográfico (SHA-256)
* ⏳ Tiempo y entropía aleatoria

El resultado es un identificador **no reversible**, **no legible** y **difícil de atacar**.

---

## 🧠 Conceptos (lenguaje MTS)

| Concepto clásico | En MTS           |
| ---------------- | ---------------- |
| Token            | **Sello**        |
| Validar          | **Invocar**      |
| Endpoint         | **Umbral**       |
| Expiración       | **Putrefacción** |
| Clave secreta    | **Dogma**        |

---

## 📁 Estructura del proyecto

```
mts/
├── app.py              # Servidor Flask
├── core/
│   ├── cipher.py       # Núcleo matemático (creación del sello)
│   └── registry.py     # Registro y validación temporal
├── .env                # Variables secretas (NO compartir)
├── requirements.txt
└── README.md
```

---

## 🔐 Variables de entorno (.env)

⚠️ **Este archivo NO debe subirse a repositorios públicos**

Ejemplo de `.env`:

```env
P=170141183460469231731687303715884105727
G=5
SERVER_SECRET=928374982374982374
```

### 📌 ¿Qué es cada cosa?

* **P** → Número primo grande (módulo matemático)
* **G** → Generador (reservado para futuras versiones)
* **SERVER_SECRET** → Dogma del sistema (clave privada del servidor)

🔁 Cambia estos valores si:

* Reinicias el sistema
* Sospechas compromiso
* Quieres invalidar todos los sellos activos

---

## 🚀 Cómo ejecutar

### 1️⃣ Crear entorno

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar servidor

```bash
python app.py
```

Servidor disponible en:

```
http://127.0.0.1:5000
```

---

## 🔑 Uso del sistema

### 🩸 Crear sello

**POST** `/test`

```json
{
  "uid": 666
}
```

Respuesta:

```json
{
  "sello": "a91f3d0b4f2c8e9d..."
}
```

---

### 🚪 Acceder al umbral

**GET** `/view`

Header requerido:

```
X-MTS-SEAL: <sello>
```

Respuesta válida:

```json
{
  "estado": "acceso concedido"
}
```

---

## 🧪 Pruebas con Postman

* Usa `POST /test` para generar el sello
* Guarda el sello como variable de entorno
* Envíalo en `X-MTS-SEAL`

💡 Un solo carácter modificado invalida el acceso.

---

## ⚠️ Advertencias importantes

* ❌ No es estándar (no JWT, no OAuth)
* ❌ No recomendado para banca o pagos
* ✅ Ideal para APIs privadas
* ✅ Excelente para aprendizaje criptográfico

---

## 🧬 Filosofía MTS

> *El sello nace del caos.*
> *El umbral no perdona.*
> *La matemática no miente.*

---

## 🛣️ Roadmap

* [ ] MTS-β (stateless)
* [ ] Rotación automática del dogma
* [ ] Sellos encadenados
* [ ] Integración con Redis
* [ ] Documentación formal tipo RFC oscura

---

## 🖤 Licencia

Quiero dinero no tengo trabajo ;'c

