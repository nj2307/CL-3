import numpy as np

class NegativeSelectionAlgorithm:
    def __init__(self, antigen_space_dim, detector_threshold, detector_radius):
        self.antigen_space_dim = antigen_space_dim
        self.detector_threshold = detector_threshold
        self.detector_radius = detector_radius

    def euclidean_distance(self, p1, p2):
        # Calculate Euclidean distance between two points
        return np.linalg.norm(p1 - p2)

    def train(self, normal_samples):
        # Train the model using normal samples
        self.detector_centers = []
        for i in range(len(normal_samples)):
            for j in range(i + 1, len(normal_samples)):
                # Calculate the distance between pairs of normal samples
                dist = self.euclidean_distance(normal_samples[i], normal_samples[j])
                # If the distance is greater than the detector radius, add the midpoint as a detector center
                if dist >= self.detector_radius:
                    self.detector_centers.append((normal_samples[i] + normal_samples[j]) / 2)

    def predict(self, unknown_samples):
        # Predict anomalies in unknown samples
        predictions = []
        for sample in unknown_samples:
            anomaly_detected = False
            for detector_center in self.detector_centers:
                # Calculate the distance between the unknown sample and each detector center
                dist = self.euclidean_distance(sample, detector_center)
                # If the distance is less than the detector threshold, mark as anomaly detected
                if dist < self.detector_threshold:
                    anomaly_detected = True
                    break
            predictions.append(anomaly_detected)
        return predictions

# Example usage:
antigen_space_dim = 10
detector_threshold = 0.5
detector_radius = 1.0

# Generate some random normal and unknown samples for demonstration
np.random.seed(0)
normal_samples = np.random.rand(100, antigen_space_dim)
unknown_samples = np.random.rand(20, antigen_space_dim)

# Initialize and train NSA model
nsa = NegativeSelectionAlgorithm(antigen_space_dim, detector_threshold, detector_radius)
nsa.train(normal_samples)

# Predict anomalies in unknown samples
predictions = nsa.predict(unknown_samples)

# Print predictions
print("Predictions:")
for i, pred in enumerate(predictions):
    print(f"Sample {i+1}: {'Anomaly Detected' if pred else 'Normal'}")
