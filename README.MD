[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mirovix_uango_ros&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mirovix_uango_ros)


# Robot Control Commands

This document provides an overview of the commands used to set up and operate a robotic system through a serial port connection via `/dev/ttymxc7`.

## Setup

Before sending any commands, ensure the serial port is correctly configured.

### 1. Port Setup
Set the port communication speed to `115200` baud.

```bash
stty -F /dev/ttymxc7 115200
```

## Commands

Each command is sent to the serial port (`/dev/ttymxc7`) to control specific robotic actions.

### 2. Basic Commands

| Command       | Code | Description                          |
|---------------|------|--------------------------------------|
| turn_on       | 10   | Turns on the device.                |
| reset_fault   | 15   | Recovers from a fault.              |
| homing_up     | 20   | Initiates the homing sequence with a specified time delay. |
| next          | 90   | Moves to the next step.             |
| stop          | 70   | Stops all operations.               |
| turn_off      | 80   | Turns off the device.               |
| get_stream    | 200 | Gets the stream data.               |

### 3. Motion Control Commands

These commands control movement, including step size, height, direction, and timing.

#### Minimum Jerk Movement

| Command                    | Hip Length (mm) | Tibia Length (mm) | Step Length (mm) | Step Height (mm) | Order | Interval (ms) | Direction |
|----------------------------|-----------------|--------------------|------------------|------------------|-------|---------------|-----------|
| first_step_jerk_dx         | 310             | 350               | 465             | 460             | 100   | 3             | 0         |
| first_step_jerk_sx         | 311             | 350               | 465             | 460             | 100   | 3             | 0         |
| first_step_jerk_walk_dx    | 410             | 350               | 465             | 460             | 100   | 3             | 0         |
| first_step_jerk_walk_sx    | 411             | 350               | 465             | 460             | 100   | 5             | 0         |

#### Inverted Pendulum Movement

| Command                  | Hip Length (mm) | Tibia Length (mm) | Step Length (mm) | Step Height (mm) | Swing Time (ms) | Order | Interval (ms) | Direction |
|--------------------------|-----------------|--------------------|------------------|------------------|-----------------|-------|---------------|-----------|
| first_step_invp_dx       | 510         | 350               | 465             | 460             | 2000            | 3     | 1000          | 0         |
| first_step_invp_sx       | 511         | 350               | 465             | 460             | 2000            | 3     | 1000          | 0         |
| first_step_invp_walk_dx  | 610         | 350               | 465             | 460             | 2000            | 3     | 0             | 0         |
| first_step_invp_walk_sx  | 611         | 350               | 465             | 460             | 2000            | 3     | 0             | 0         |

## Install and Run Commands

To run a command, send the command code to the serial port.

#### 1. Prepare the environment
```bash
mkdir ~/uango_ros/
cd ~/uango_ros/
python3.12 -m venv venv
source venv/bin/activate

```
#### 2. Install the package
```bash
echo "--index-url https://pypi.fury.io/miroljubmihailovic98/" > requirements.txt
echo "--extra-index-url https://pypi.org/simple/" >> requirements.txt
echo "uango_ros_web_socket" >> requirements.txt
pip install -r requirements.txt
```

#### 3. Set environment variables
```bash
export IP_ADDRESS_UANGO=192.168.12.1
export PORT_UANGO=8080
```

#### 4. Run the command
```bash
python3 -m web_socket **command**
```

---