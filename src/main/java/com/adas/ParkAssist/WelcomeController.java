package com.adas.ParkAssist;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WelcomeController {

    @GetMapping("/")
    public String hello() {
        return "<html><body><h1 style=\"font-size: 24px; font-weight: bold;\">Hello, Welcome to Park Assist!</h1><br>We are working on enhacing park assist feature.</body></html>";
    }
}
