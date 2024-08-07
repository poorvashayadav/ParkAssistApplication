# Stage 1: Build the application
FROM maven:3.8.5-openjdk-17 AS build
WORKDIR /app

# Copy only the necessary files for dependency resolution first
COPY pom.xml .
RUN mvn dependency:go-offline

# Now copy the rest of the source code
COPY src ./src

# Build the application
RUN mvn clean package

# Stage 2: Create the final image
FROM openjdk:17-jdk-slim
WORKDIR /app

# Copy the JAR file from the build stage
COPY --from=build /app/target/ParkAssist-0.0.1-SNAPSHOT.jar /app/ParkAssist-0.0.1-SNAPSHOT.jar

# Print the Java version to ensure Java is available
RUN java -version

# List files in the working directory to verify the JAR file is present
RUN ls -lh /app

# Expose port 80
EXPOSE 80

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=10s --retries=5 CMD curl -f http://localhost/ || exit 1

# Run the application
ENTRYPOINT ["java", "-jar", "/app/ParkAssist-0.0.1-SNAPSHOT.jar"]
