---
name: nest-control
description: >
  This skill should be used when the user wants to "check thermostat",
  "set temperature", "change hvac mode", "toggle eco mode", "how hot is it",
  "how cold is it", "nest status", "set temp to 72", "turn on cooling",
  "turn on heating", "set range". Triggers on "thermostat", "temperature",
  "nest", "set temp", "hvac", "how hot", "how cold", "cooling", "heating",
  "eco mode", "set range".
  DO NOT trigger on: "install Nest", "buy a thermostat", "Nest camera",
  "Nest doorbell", "smart home setup" (hardware/setup, not thermostat control).
---

# Nest Thermostat Control

Control Google Nest thermostats via the SDM API through the commander container.

## Devices

| Index | Location |
|-------|----------|
| 0 | Upstairs |
| 1 | Downstairs |

Default is index 0 (Upstairs) when no location specified.

## Commands

All commands run inside the commander container:

### Check Status

```bash
# All thermostats
docker exec commander python -m tools.nest_client status

# Specific thermostat
docker exec commander python -m tools.nest_client status 0   # Upstairs
docker exec commander python -m tools.nest_client status 1   # Downstairs
```

### Set Temperature

```bash
# Set temp (auto-detects HEAT/COOL mode)
docker exec commander python -m tools.nest_client set-temp 72      # Upstairs (default)
docker exec commander python -m tools.nest_client set-temp 68 1    # Downstairs
```

### Set Temperature Range (HEATCOOL mode)

```bash
# Set heat and cool setpoints simultaneously
docker exec commander python -m tools.nest_client set-range 68 74      # Upstairs
docker exec commander python -m tools.nest_client set-range 66 72 1    # Downstairs
```

Note: `set-range` only works when mode is HEATCOOL. Switch mode first if needed.

### Change Mode

```bash
docker exec commander python -m tools.nest_client set-mode COOL     # Upstairs
docker exec commander python -m tools.nest_client set-mode HEAT 1   # Downstairs
# Modes: HEAT, COOL, HEATCOOL, OFF
```

### Eco Mode

```bash
docker exec commander python -m tools.nest_client set-eco on       # Upstairs
docker exec commander python -m tools.nest_client set-eco off 1    # Downstairs
```

### List Devices

```bash
docker exec commander python -m tools.nest_client devices
```

## Workflow

1. Always check current status first before making changes
2. Report temperatures in Fahrenheit (the CLI handles F/C conversion internally)
3. When user says "upstairs" use index 0, "downstairs" use index 1
4. If user just says "set to 72" without location, default to index 0 (Upstairs)
5. After setting temperature/mode, run status again to confirm the change took effect

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `NEST_ACCESS_TOKEN not set` | Token expired or missing | Visit `cmd.example.com/nest/oauth/start` to re-authorize |
| `NEST_SDM_PROJECT_ID not set` | Missing env var | Check `.env` has `NEST_SDM_PROJECT_ID=YOUR_SDM_PROJECT_ID` |
| `Thermostat index X out of range` | Wrong index | Run `devices` command to list available thermostats |
| `Cannot set temp in HEATCOOL mode` | Mode mismatch | Use `set-range` instead of `set-temp` for HEATCOOL |
| API 401 errors | Token expired | Token auto-refreshes on 401. If persistent, re-authorize via OAuth |

## Additional Resources

For OAuth setup details, GCP project IDs, and env var reference, see `references/oauth-setup.md`.
