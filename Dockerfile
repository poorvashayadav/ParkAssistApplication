# Stage 1: Build the application
FROM maven:3.8.5-openjdk-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package

# Stage 2: Create the final image
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY --from=build /app/target/ParkAssist-0.0.1-SNAPSHOT.jar .
ENTRYPOINT ["java", "-jar", "ParkAssist-0.0.1-SNAPSHOT.jar"]
