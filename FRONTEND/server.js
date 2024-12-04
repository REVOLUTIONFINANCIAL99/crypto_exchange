// Importar dependencias necesarias
const express = require('express');
const path = require('path');
const dotenv = require('dotenv'); // Para manejar variables de entorno (si es necesario)
const cors = require('cors'); // Si necesitas permitir peticiones de otros orígenes (CORS)

// Cargar las variables de entorno desde un archivo .env
dotenv.config();

// Inicializar la aplicación Express
const app = express();

// Configuración de puerto: usa el puerto de la variable de entorno o el 3000 por defecto
const port = process.env.PORT || 3000;

// Middleware de CORS (si lo necesitas para permitir peticiones entre diferentes orígenes)
app.use(cors());

// Middleware para analizar datos de solicitudes POST
app.use(express.json()); // Para JSON
app.use(express.urlencoded({ extended: true })); // Para datos URL codificados

// Configuración para servir archivos estáticos desde la carpeta 'public'
app.use(express.static(path.join(__dirname, 'public')));

// Ruta principal para servir el index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Ruta para la página de login (puedes personalizarla según tus necesidades)
app.get('/login', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'login.html'));
});

// Ruta para la página de registro (puedes personalizarla según tus necesidades)
app.get('/register', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'register.html'));
});

// Otras rutas adicionales (puedes agregar más según tu lógica de la app)
app.get('/dashboard', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'dashboard.html'));
});

// API de ejemplo: manejar peticiones POST (puedes personalizar según tu backend)
app.post('/api/transfer', (req, res) => {
  const { from, to, amount } = req.body;
  // Aquí agregarías la lógica para manejar la transferencia de activos
  res.status(200).json({ message: `Transferencia de ${amount} desde ${from} hacia ${to} procesada correctamente` });
});

// Manejo de errores 404: ruta no encontrada
app.use((req, res, next) => {
  res.status(404).send('Página no encontrada');
});

// Manejo de errores generales
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Algo salió mal en el servidor');
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor en funcionamiento en http://localhost:${port}`);
});
