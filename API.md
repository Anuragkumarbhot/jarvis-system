API Documentation

Login

POST /login

Logout

GET /logout

Home

GET /

IoT Control

GET /iot/<device>/<state>

Example:

/iot/relay1/on

Camera

GET /camera

System Status

GET /system

Response Example:

{
"cpu": "ok",
"ram": "ok",
"battery": "48"
}
