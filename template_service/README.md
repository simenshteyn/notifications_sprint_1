## UGC Service

OpenAPI: [http://localhost/api/v1/docs](http://localhost/api/v1/docs)

**Setup**
1. Create .env file with sample:

`$ cp env.sample .env`

`$ vi .env`

**Run project without tests**

`$ docker-compose up --build -d`

**Testing**

`$ docker-compose --profile=testing up --build`

 - Clear docker containers with all data:
 
`$ docker-compose down -v`

**Using**

1. Create some template using `/template` endpoint. Use [string.Template](https://docs.python.org/3/library/string.html#template-strings) for templates content:

For example: `${user_name}, hello. Your ${email} is verified!`

2. Generate message with template:

- For user with UUID at `/message/user` endpoint. You can use standard fields: user_name, user_last_name, email, phone_number, telegram_user_name, location, birthdate.
Example POST requiest:

`{
    "template_id": "e68b06a2-c19c-49d5-ae8b-02e77f8d5276",
    "user_id": "2ece1a5b-c4c8-4626-a72e-363d82d0180e"
}`

- With custom payload at `/message/custom` endpoint.  For example, you can use template: `Hello, ${name} ${soname}` with POST requiest:

`{
    "template_id": "2be767ef-e626-4747-be20-2b48c84ec4d7",
    "payload": {
        "name": "Sergey",
        "soname": "Sergeevich"
    }
}`