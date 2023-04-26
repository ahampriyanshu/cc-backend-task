## User Access Management

- Cosmocloud backend task

- [https://cosmo-cloud.onrender.com/docs](https://cosmo-cloud.onrender.com/docs)
- [https://cosmo-cloud.onrender.com/redoc](https://cosmo-cloud.onrender.com/redoc)

## Setup

```bash
git clone https://github.com/ahampriyanshu/cc-backend-task.git cosmo
cd cosmo
pip3 install -r requirements.txt
```

- Setup and run mongo server
- Update the .env variables
- Run `uvicorn main:app --reload`

## Collections

![db](https://user-images.githubusercontent.com/54521023/234565503-1cdad4e0-d437-4084-bc98-8b17050d48c5.png)

## Endpoints

- [https://cosmo-cloud.onrender.com/api](https://cosmo-cloud.onrender.com/api)

### Users

#### ``POST`` Create new user - [Execute](https://cosmo-cloud.onrender.com/docs#/user/create_new_user_api_user__post)
- [https://cosmo-cloud.onrender.com/api/user/](https://cosmo-cloud.onrender.com/api/user/)
```
{
  "name": "Priyanshu Tiwari",
  "email": "ahampriyanshu@gmail.com"
}
```

#### ``GET`` Get user by ID - [Execute](https://cosmo-cloud.onrender.com/docs#/user/get_user_by_id_api_user__user_id__get)
- [https://cosmo-cloud.onrender.com/api/user/6449157fbc73adf705e6c418](https://cosmo-cloud.onrender.com/api/user/6449157fbc73adf705e6c418)

#### ``GET`` Get user by Email - [Execute](https://cosmo-cloud.onrender.com/docs#/user/get_users_by_filters_api_user__get)
- [https://cosmo-cloud.onrender.com/api/user/?email=ahampriyanshu](https://cosmo-cloud.onrender.com/api/user/?email=ahampriyanshu)


#### ``GET`` List of oraganisations for a user - [Execute](https://cosmo-cloud.onrender.com/docs#/user/get_organisation_users_api_user__user_id__organisations_get)
- [https://cosmo-cloud.onrender.com/api/user/6449157fbc73adf705e6c418/organisations?limit=10&offset=0](https://cosmo-cloud.onrender.com/api/user/6449157fbc73adf705e6c418/organisations?limit=10&offset=0)

#### ``GET`` List of users - [Execute](https://cosmo-cloud.onrender.com/api/user/?limit=10&offset=0)
- [https://cosmo-cloud.onrender.com/docs#/user/get_users_by_filters_api_user__get](https://cosmo-cloud.onrender.com/docs#/user/get_users_by_filters_api_user__get)

### Organisation

#### ``POST`` Create new organisation - [Execute](https://cosmo-cloud.onrender.com/docs#/organisation/create_new_organisation_api_organisation__post)
- [https://cosmo-cloud.onrender.com/api/organisation/](https://cosmo-cloud.onrender.com/api/organisation/)
```
{
  "name": "Cosmo Cloud"
}
```

#### ``GET`` Get organisation by ID - [Execute](https://cosmo-cloud.onrender.com/docs#/organisation/get_organisation_by_id_api_organisation__organisation_id__get)
- [https://cosmo-cloud.onrender.com/api/organisation/644917edbc73adf705e6c419](https://cosmo-cloud.onrender.com/api/organisation/644917edbc73adf705e6c419)

#### ``GET`` Get organisation by Name - [Execute](https://cosmo-cloud.onrender.com/docs#/organisation/get_organisations_by_filters_api_organisation__get)
- [https://cosmo-cloud.onrender.com/api/organisation/?name=Cosmo%20Cloud](https://cosmo-cloud.onrender.com/api/organisation/?name=Cosmo%20Cloud)


#### ``GET`` List of users from an organisation - [Execute](https://cosmo-cloud.onrender.com/docs#/organisation/get_organisation_users_api_organisation__organisation_id__users_get)
- [https://cosmo-cloud.onrender.com/api/organisation/644917edbc73adf705e6c419/users?limit=10&offset=0](https://cosmo-cloud.onrender.com/api/organisation/644917edbc73adf705e6c419/users?limit=10&offset=0)

#### ``GET`` List of organisations - [Execute](https://cosmo-cloud.onrender.com/docs#/organisation/get_organisations_by_filters_api_organisation__get)
- [https://cosmo-cloud.onrender.com/api/organisation/?limit=10&offset=0](https://cosmo-cloud.onrender.com/api/organisation/?limit=10&offset=0)

### Permissions

#### ``POST`` Add user(s) to an organisation - [Execute](https://cosmo-cloud.onrender.com/docs#/permissions/create_new_permission_api_permissions__organisation_id__post)
- [
https://cosmo-cloud.onrender.com/api/permissions/644917edbc73adf705e6c419](https://cosmo-cloud.onrender.com/api/permissions/644917edbc73adf705e6c419?access_level=WRITE)
```
[
  "6449157fbc73adf705e6c418", "6449123dbc73adf705e6c417"
]
```

#### ``PUT`` Update user(s) permissions - [Execute](https://cosmo-cloud.onrender.com/docs#/permissions/create_new_permission_api_permissions__organisation_id__post)
- [https://cosmo-cloud.onrender.com/api/permissions/644917edbc73adf705e6c419?access_level=READ](https://cosmo-cloud.onrender.com/api/permissions/644917edbc73adf705e6c419?access_level=READ)
```
[
  "6449157fbc73adf705e6c418", "6449123dbc73adf705e6c417"
]
```

#### ``DELETE`` Delete user(s) from an organisation - [Execute](https://cosmo-cloud.onrender.com/docs#/permissions/delete_existing_permission_api_permissions__organisation_id__delete)
- [https://cosmo-cloud.onrender.com/api/permissions/644917edbc73adf705e6c419](https://cosmo-cloud.onrender.com/api/permissions/644917edbc73adf705e6c419)
```
[
  "6449157fbc73adf705e6c418", "6449123dbc73adf705e6c417"
]
```

### Responses

#### 200, 201

```
{
"data": {

}
}
```

```
{
"data": [ ],
"metadata": {
"count": 0,
"limit": 0,
"offset": 0
}
}
```

#### 400, 404, 405, 409, 422, 500

```
{
    "error_message" : ""
}
