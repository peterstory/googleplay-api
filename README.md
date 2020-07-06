# Google Play Python API

This code is a minimal fork of [NoMore201/googleplay-api](https://github.com/NoMore201/googleplay-api). The main functionality we maintain is the ability to download apps.

# Usage
Check `test.py` for a simple example.

An important note about login function:
```
def login(self, email=None, password=None, gsfId=None, authSubToken=None)
```
for first time logins, you should only provide email and password.
The module will take care of initalizing the api,upload device information
to the google account you supplied, and retrieving
a Google Service Framework ID (which, from now on, will be the android ID of a device).

For the next logins you **should** save the gsfId and the authSubToken, and provide them as parameters to the login function. If you login again with email and password only, this is the equivalent of re-initalizing your android device with a google account.

# Documentation

For some documentation about the google play API check out the relative folder.

# Development

If you haven't already, set up a virtual environment in the top-level of the project:

```
# Create the virtual environment
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install the project's dependencies
pip install -r requirements.txt
```

The dependencies installed for development include those described in `setup.py` as well as `pytest`, which is used to run the automated test suite.

To run `pytest`, first export your account `EMAIL` and `PASSWORD`, and also a hex-encoded `GSFID`, as environment variables. Next, run `pytest`.

```
export EMAIL='XXX'
export PASSWORD='XXX'
export GSFID='XXX'
python -m pytest -v
```

# Maintenance

As Google updates the Google Play Store API, it might be necessary to periodically update the protobuf definition. First, update `googleplay.proto` from the upstream repo, `NoMore201/googleplay-api`. Next, [download a recent version of the protobuf compiler, protoc](https://github.com/protocolbuffers/protobuf/releases/). Finally, use the compiler to update `gpapi/googleplay_pb2.py`:

```
protoc --proto_path . --python_out gpapi googleplay.proto
```
