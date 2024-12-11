package com.example.vision;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/license-plates")
public class LicensePlateDetectionController {

    @Autowired
    private LicensePlateDetectionService service;

    // API to save a license plate detection
    @PostMapping("/detect")
    public String detectLicensePlate(@RequestParam String videoPath, @RequestParam String licensePlate) {
        service.saveDetection(videoPath, licensePlate);
        return "License plate detected and saved successfully!";
    }

    @CrossOrigin(origins = "http://localhost:3000")
    @GetMapping("/get-all")
    public List<LicensePlateDetection> getAllDetections() {
        return service.getAllDetections(); // This should fetch data from your database
    }


}
