# Start with a base image that includes Maven and JDK
FROM maven:3.8.4-openjdk-17-slim AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the Maven configuration files (if any) and the POM file
COPY pom.xml .

# Download the Maven dependencies (only dependencies)
RUN mvn dependency:go-offline -B

# Copy the entire project source
COPY src ./src

# Build the application
RUN mvn package -DskipTests

# Second stage: Create a minimal Docker image with just the Java runtime and the built artifact
FROM openjdk:17-slim

# Set the working directory
WORKDIR /app

# Copy the JAR file built in the previous stage
COPY --from=build /app/target/ParkAssist-0.0.1-SNAPSHOT.jar .

# Command to run the Spring Boot application
CMD ["java", "-jar", "ParkAssist-0.0.1-SNAPSHOT.jar"]
