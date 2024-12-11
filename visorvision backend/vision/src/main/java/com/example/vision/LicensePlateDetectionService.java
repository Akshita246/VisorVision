package com.example.vision;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class LicensePlateDetectionService {

    @Autowired
    private LicensePlateDetectionRepository repository;

    // Save license plate detection
    public void saveDetection(String videoPath, String licensePlate) {
        LicensePlateDetection detection = new LicensePlateDetection();
        detection.setVideoPath(videoPath);
        detection.setLicensePlate(licensePlate);
        detection.setDetectionTime(LocalDateTime.now());
        repository.save(detection);
    }

    // Get all detections
    public List<LicensePlateDetection> getAllDetections() {
        return repository.findAll();
    }
}

