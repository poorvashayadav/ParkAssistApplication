package com.adas.ParkAssist;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WelcomeController {

    @GetMapping("/")
    public String hello() {
        return "<html>" +
               "<head>" +
               "<style>" +
               "body { " +
               "    font-family: Arial, sans-serif; " +
               "    background-image: url('https://www.emergingrisks.co.uk/wp-content/uploads/2022/08/Autonomous-driving-850px.jpg');" + // Replace with your image URL
               "    background-size: cover;" +
               "    background-position: center;" +
               "    background-repeat: no-repeat;" +
               "    color: #000; " + // Main text color set to black
               "    margin: 0; " +
               "    padding: 0; " +
               "    text-align: center; " +
               "} " +
               ".container { " +
               "    max-width: 800px; " +
               "    margin: 50px auto; " +
               "    padding: 20px; " +
               "    background: rgba(255, 255, 255, 0.8);" + // Semi-transparent background
               "    border-radius: 8px; " +
               "    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); " +
               "} " +
               "h1 { " +
               "    font-size: 32px; " +
               "    color: #4CAF50; " +
               "    margin-bottom: 20px; " +
               "} " +
               "p { " +
               "    font-size: 18px; " +
               "    line-height: 1.6; " +
               "} " +
               ".highlight { " +
               "    font-weight: bold; " +
               "    color: #0000FF; " + // Highlighted text color set to blue
               "} " +
               ".change-request { " +
               "    margin-top: 30px; " +
               "    padding: 20px; " +
               "    background: #eaf0e5; " +
               "    border-radius: 8px; " +
               "    border: 1px solid #c4e1c1; " +
               "} " +
               ".bug-request { " +
               "    background: #fbe8e8; " +
               "    border: 1px solid #f5c6c6; " +
               "} " +
               "</style>" +
               "</head>" +
               "<body>" +
               "<div class=\"container\">" +
               "<h1>Hello, Welcome to Park Assist!</h1>" +
               "<p>We are currently working on enhancing the <span class=\"highlight\">Park Assist</span> features.</p>" +
               "<p>Our latest project includes developing an <span class=\"highlight\">automated lane keeping system</span>.</p>" +
               "<div class=\"change-request\">" +
               "<h2>Change Request 1</h2>" +
               "<p>New Feature: <span class=\"highlight\">Stop parking if a door opens to ensure safety</span>.</p>" +
               "<p>This enhancement will ensure that the parking maneuver automatically stops if a door is opened, preventing potential accidents and improving overall safety.</p>" +
               "</div>" +
               "<div class=\"change-request\">" +
               "<h2>Change Request 2</h2>" +
               "<p>New Feature: <span class=\"highlight\">Enhanced Parking Safety: Stop on Object Detection</span>.</p>" +
               "<p>This feature will halt the parking maneuver when an object is detected, ensuring the vehicle does not collide with any obstacles.</p>" +
               "</div>" +
               "<div class=\"change-request\">" +
               "<h2>Change Request 3</h2>" +
               "<p>New Feature: <span class=\"highlight\">Smart Perpendicular Parking Assist</span>.</p>" +
               "<p>This feature enhances the system's ability to park perpendicularly, making parking in tight spots easier and safer.</p>" +
               "</div>" +
               "<div class=\"bug-request\">" +
               "<h2>Bug Requests</h2>" +
               "<h3>[BUG-27389]</h3>" +
               "<p>Issue: <span class=\"highlight\">The system should immediately stop the parking maneuver if an object is detected in the vehicle's path</span>.</p>" +
               "<p>This bug involves the failure of the parking assist system to halt when an obstacle is detected, which can lead to potential accidents or damage.</p>" +
               "<h3>[BUG-27385]</h3>" +
               "<p>Issue: <span class=\"highlight\">The vehicle does not stop parking when a door opens, posing a safety risk</span>.</p>" +
               "<p>There is a critical bug where the parking process continues even if a door is opened, which could result in safety hazards. This issue requires immediate attention.</p>" +
               "<h3>[BUG-27393]</h3>" +
               "<p>Issue: <span class=\"highlight\">The system does not currently halt perpendicular parking when a door opens during adjustments</span>.</p>" +
               "<p>There is a bug where the vehicle continues to adjust itself during perpendicular parking even if a door opens. This poses a safety risk and needs to be addressed immediately to prevent potential accidents.</p>" +
               "</div>" +
               "</div>" +
               "</body>" +
               "</html>";
    }
}
