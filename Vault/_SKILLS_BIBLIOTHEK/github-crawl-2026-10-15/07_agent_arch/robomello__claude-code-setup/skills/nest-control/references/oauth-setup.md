# Nest OAuth Setup Reference

## Prerequisites

- Google Cloud Platform project (ID: `151952771234`, separate from main GCP project)
- Device Access Project ID: `YOUR_SDM_PROJECT_ID`
- Google Partner Connections Manager authorization

## Required Environment Variables

All must be set in `~/.env` (mounted as `/host/user/.env` in commander container):

| Variable | Description |
|----------|-------------|
| `NEST_CLIENT_ID` | GCP OAuth 2.0 client ID |
| `NEST_CLIENT_SECRET` | GCP OAuth 2.0 client secret |
| `NEST_SDM_PROJECT_ID` | Device Access project ID (`3f7bc708-...`) |
| `NEST_ACCESS_TOKEN` | OAuth access token (auto-refreshed on 401) |
| `NEST_REFRESH_TOKEN` | OAuth refresh token (long-lived) |

## Initial Authorization

1. Visit `cmd.example.com/nest/oauth/start` in browser
2. Authorize with Google account that owns the Nest devices
3. Grant permissions for thermostat access
4. Callback saves tokens automatically to `.env`
5. Verify: `cmd.example.com/nest/oauth/status`

## Token Lifecycle

- **Access token**: Expires in 1 hour. Auto-refreshed on 401 response by `NestClient`.
- **Refresh token**: Long-lived. Only invalidated if user revokes access in Google account settings.
- **Re-authorization**: Only needed if refresh token is revoked or GCP project config changes.

## OAuth Implementation

- **OAuth flow**: `~/commander/nest_oauth.py`
- **Client**: `~/tools/nest_client.py` - `NestClient` class
- **API base**: `https://sTABLE_ID_PLACEHOLDERent.googleapis.com/v1/enterprises/{project_id}/devices`

## Troubleshooting

- **"NEST_ACCESS_TOKEN not set"**: Run `cmd.example.com/nest/oauth/start` to authorize
- **Persistent 401 after refresh**: Refresh token may be revoked. Re-authorize.
- **"NEST_SDM_PROJECT_ID not set"**: Add to `.env`: `NEST_SDM_PROJECT_ID=YOUR_SDM_PROJECT_ID`
- **No devices found**: Verify thermostat is linked to the authorized Google account in Google Home app
