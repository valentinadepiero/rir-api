"""Tests para el servicio apply_smoothing (Milestone 3)."""

import numpy as np
import pytest

from app.services.acoustic_parameters import apply_smoothing


class TestApplySmoothingValidation:
    """Tests de validacion para apply_smoothing."""

    def test_invalid_method(self):
        """Rechaza metodos de suavizado no admitidos."""
        signal = np.array([1.0, 2.0, 3.0])

        with pytest.raises(ValueError):
            apply_smoothing(signal, 1000, method="invalid")

    @pytest.mark.parametrize("fs", [0, -1, 1000.5, True])
    def test_invalid_sampling_rate(self, fs):
        """Rechaza frecuencias de muestreo invalidas."""
        signal = np.array([1.0, 2.0, 3.0])

        with pytest.raises(ValueError):
            apply_smoothing(signal, fs)

    @pytest.mark.parametrize(
        "window_ms", [0, -1, np.nan, np.inf, "10", True]
    )
    def test_invalid_window(self, window_ms):
        """Rechaza ventanas invalidas para moving_average."""
        signal = np.array([1.0, 2.0, 3.0])

        with pytest.raises(ValueError):
            apply_smoothing(
                signal, 1000, method="moving_average", window_ms=window_ms
            )

    def test_complex_signal(self):
        """Rechaza señales con valores complejos."""
        signal = np.array([1.0 + 1.0j, 2.0 + 0.0j])

        with pytest.raises(ValueError):
            apply_smoothing(signal, 1000)

    def test_window_larger_than_signal(self):
        """Mantiene la longitud de salida aunque la ventana sea mayor."""
        signal = np.array([1.0, 2.0, 3.0])

        envelope = apply_smoothing(
            signal, 1000, method="moving_average", window_ms=100
        )

        assert len(envelope) == len(signal)
        assert np.all(envelope >= 0)
        assert np.all(np.isfinite(envelope))


class TestApplySmoothingMethods:
    """Tests para los metodos de suavizado."""

    def test_hilbert_envelope(self):
        """La envolvente de Hilbert sigue la amplitud de una senal."""
        fs = 8000
        t = np.arange(fs) / fs
        amplitude = np.exp(-3 * t)
        signal = amplitude * np.sin(2 * np.pi * 500 * t)

        envelope = apply_smoothing(signal, fs, method="hilbert")

        assert len(envelope) == len(signal)
        assert np.all(envelope >= 0)

        center = slice(fs // 10, -fs // 10)
        np.testing.assert_allclose(
            envelope[center], amplitude[center], rtol=0.05
        )

    def test_moving_average_rms(self):
        """La media movil RMS conserva la amplitud de una senal constante."""
        signal = np.full(100, 2.0)

        envelope = apply_smoothing(
            signal, 1000, method="moving_average", window_ms=10
        )

        assert len(envelope) == len(signal)
        np.testing.assert_allclose(envelope, 2.0)

    def test_moving_average_uses_previous_samples(self):
        """La media movil utiliza la muestra actual y las anteriores."""
        signal = np.array([1.0, 2.0, 3.0, 4.0])
        fs = 1000
        window_ms = 2

        expected = np.array(
            [
                1.0,
                np.sqrt((1.0**2 + 2.0**2) / 2),
                np.sqrt((2.0**2 + 3.0**2) / 2),
                np.sqrt((3.0**2 + 4.0**2) / 2),
            ]
        )

        envelope = apply_smoothing(
            signal, fs, method="moving_average", window_ms=window_ms
        )

        np.testing.assert_allclose(envelope, expected)

    @pytest.mark.parametrize(
        "signal",
        [
            [1.0, 2.0, 3.0],
            np.array([[1.0, 2.0], [3.0, 4.0]]),
            np.array([]),
            np.array([1.0, np.nan]),
            np.array([1.0, np.inf]),
        ],
    )
    def test_invalid_signal(self, signal):
        """Rechaza señales con formato o valores inválidos."""
        with pytest.raises(ValueError):
            apply_smoothing(signal, 1000)
