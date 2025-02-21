import math
import subprocess

import subprocess




def signal_strength_percentage_to_dBm(signal_percentage):
    """
    Map signal strength percentage to dBm. Assuming -100 dBm at 0% and -30 dBm at 100%.
    """
    min_dBm = -100  # weakest signal
    max_dBm = -30  # strongest signal

    # Linearly map percentage to dBm range
    return min_dBm + (max_dBm - min_dBm) * (signal_percentage / 100)


def get_signal_strength_windows():
    try:
        # Run the netsh command to get Wi-Fi information
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        output = result.stdout

        # Find and extract the signal strength percentage
        for line in output.splitlines():
            if "Signal" in line:
                # Extract signal percentage from the line
                signal_percentage = int(line.split(":")[1].strip().replace('%', ''))
                return signal_percentage
    except Exception as e:
        print(f"Error: {e}")
        return None


# Get Wi-Fi signal strength percentage
signal_percentage = get_signal_strength_windows()
if signal_percentage:
    print(f"Signal Strength: {signal_percentage}%")

    # Convert signal strength percentage to dBm
    rssi_dBm = signal_strength_percentage_to_dBm(signal_percentage)
    print(f"Signal Strength (RSSI) in dBm: {rssi_dBm} dBm")

    # Example transmitted power in dBm (change as needed)
    transmitted_power_dBm = 20  # For example, 20 dBm (100mW)


    # Calculate channel gain (in dB)
    def dBm_to_watts(dBm):
        return 10 ** ((dBm - 30) / 10)


    def calculate_channel_gain(received_rssi_dBm, transmitted_power_dBm):
        # Convert RSSI and transmitted power to watts
        received_power_watts = dBm_to_watts(received_rssi_dBm)
        transmitted_power_watts = dBm_to_watts(transmitted_power_dBm)

        # Calculate channel gain
        channel_gain = received_power_watts / transmitted_power_watts
        channel_gain_dB = 10 * math.log10(channel_gain)

        return channel_gain, channel_gain_dB


    gain_linear, gain_dB = calculate_channel_gain(rssi_dBm, transmitted_power_dBm)

    print(f"Channel Gain (Linear): {gain_linear}")
    print(f"Channel Gain (dB): {gain_dB} dB")
else:
    print("Could not retrieve Wi-Fi signal strength.")