# Establecer la imagen base de Docker
FROM amazoncorretto:17

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo JAR generado por Maven a la imagen de Docker
COPY target/Microservicios-0.0.1-SNAPSHOT.jar app.jar

# Exponer el puerto en el que se ejecuta la aplicación Spring Boot
EXPOSE 8080

# Comando para ejecutar la aplicación Spring Boot
ENTRYPOINT ["java", "-jar", "app.jar"]
