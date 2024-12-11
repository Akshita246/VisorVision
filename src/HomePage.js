import React, { useState, useEffect } from 'react';
import './HomePage.css';


// HomePage component
function HomePage() {

  const [violations, setViolations] = useState([]);

  // Fetch violations data from the backend when the component mounts
  useEffect(() => {
    fetch('http://localhost:8080/api/license-plates/get-all')
      .then((response) => response.json())
      .then((data) => setViolations(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="home-page">
      <header className="navbar">
        <h1 className="logo-container">
          <div className="logo"></div>
          <h2 className="logo-text">
            <span>V</span>
            <span>i</span>
            <span>s</span>
            <span>o</span>
            <span>r</span>
            <span>V</span>
            <span>i</span>
            <span>s</span>
            <span>i</span>
            <span>o</span>
            <span>n</span>
          </h2>
        </h1>
        <nav>
          <ul className="nav-links">
            <li>
              <a href="#features">Features</a>
            </li>
            <li>
              <a href="#violators">Violators Data</a>
            </li>
            <li>
              <a href="#contact">Contact</a>
            </li>
          </ul>
        </nav>
      </header>

      <section className="hero-section" id="about">
        <img src="img4.jpg" alt="Traffic Surveillance" className="hero-image" />
        <div className="hero-content">
          <h2>Next-Gen Traffic Surveillance</h2>
          <p>
            VisorVision ensures road safety by detecting helmet usage and
            recording vehicle details. Stay protected, stay informed.
          </p>
        </div>
      </section>

      <section className="features-section" id="features">
        <h2>Features</h2>
        <div className="features-grid">
          <img src="img01.png" alt="Traffic Surveillance" className="image" />
          <div className="feature-card">
            <h3>Real-Time Detection</h3>
            <p>Monitor traffic and detect helmet violations in real-time.</p>
          </div>
          <img src="img02.jpg" alt="Traffic Surveillance" className="image" />
          <div className="feature-card">
            <h3>License Plate Recognition</h3>
            <p>Automatic detection of number plates for non-compliance.</p>
          </div>
          <img src="img3.jpg" alt="Traffic Surveillance" className="image" />
          <div className="feature-card">
            <h3>Data Logging</h3>
            <p>Maintain detailed logs for better tracking and analysis.</p>
          </div>
        </div>
      </section>

      <section className="violators-section" id="violators">
        <h2>Violators Dashboard</h2>
        <table className="violator-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Video Path</th>
              <th>License Plate</th>
              <th>Detection Time</th>
            </tr>
          </thead>
          <tbody>
            {violations.map((violation) => (
              <tr key={violation.id}>
                <td>{violation.id}</td>
                <td>
                <a
                 href={`${violation.videoPath}`}  // Using relative path from the public folder
                   target="_blank"
                  rel="noopener noreferrer"
                >
               {violation.videoPath}
              </a>
                </td>
                <td>{violation.licensePlate}</td>
                <td>{violation.detectionTime}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      <section className="contact-section" id="contact">
        <h2>Contact</h2>
        <p>Email: contact@visorvision.com</p>
        <p>Phone: +91 9876543210</p>
      </section>

      <footer className="footer">
        <p>&copy; 2024 VisorVision. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default HomePage;
