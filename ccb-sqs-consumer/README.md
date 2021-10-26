Toma las trazas de ejecución de los servicios de la cola SQS y los escribe a BD en tierra.

> Prueba pendiente:
- Configurar un Batch Window en SQS para disminuir la cantidad de llamadas a esta funcion Lambda y verificar que en BD 
SQL Server se graba la cantidad de registros correcta (la misma que la cantidad de invocaciones). 
Hacer la prueba con JMeter. 