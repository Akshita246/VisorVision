package com.example.vision;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "license_plate_detection")
public class LicensePlateDetection {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "video_path")
    private String videoPath;

    @Column(name = "license_plate", nullable = false)
    private String licensePlate;

    @Column(name = "detection_time", nullable = false)
    private LocalDateTime detectionTime;

    // Getters and Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getVideoPath() {
        return videoPath;
    }

    public void setVideoPath(String videoPath) {
        this.videoPath = videoPath;
    }

    public String getLicensePlate() {
        return licensePlate;
    }

    public void setLicensePlate(String licensePlate) {
        this.licensePlate = licensePlate;
    }

    public LocalDateTime getDetectionTime() {
        return detectionTime;
    }

    public void setDetectionTime(LocalDateTime detectionTime) {
        this.detectionTime = detectionTime;
    }

}
