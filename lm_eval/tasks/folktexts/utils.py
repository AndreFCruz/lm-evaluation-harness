import datasets
import numpy as np


def expected_calibration_error(y_true, y_scores, n_bins=10):
    """Computes the Expected Calibration Error (ECE).
    """
    y_true = np.asarray(y_true)
    y_scores = np.asarray(y_scores)

    # Define the bin boundaries
    bin_edges = np.linspace(0.0, 1.0, n_bins + 1)
    bin_indices = np.digitize(y_scores, bin_edges, right=True) - 1  # Bin indices start at 0

    ece = 0.0
    n_samples = len(y_true)

    for i in range(n_bins):
        # Get indices of samples in the current bin
        in_bin = bin_indices == i
        bin_count = np.sum(in_bin)

        if bin_count > 0:
            # Calculate average confidence and accuracy in the bin
            avg_confidence = np.mean(y_scores[in_bin])
            avg_accuracy = np.mean(y_true[in_bin])
            bin_weight = bin_count / n_samples

            # Accumulate the weighted absolute difference
            ece += bin_weight * np.abs(avg_confidence - avg_accuracy)

    return ece