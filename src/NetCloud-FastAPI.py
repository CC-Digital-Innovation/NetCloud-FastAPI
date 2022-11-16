from fastapi import FastAPI, Header, Response


# Module information.
__author__ = 'Anthony Farina'
__copyright__ = 'Copyright (C) 2022 Computacenter Digital Innovation'
__credits__ = ['Anthony Farina']
__maintainer__ = 'Anthony Farina'
__email__ = 'farinaanthony96@gmail.com'
__license__ = 'MIT'
__version__ = '1.0.1'
__status__ = 'Released'


# API instance variable.
NETCLOUD_API_INST = FastAPI()


# This API endpoint will return the status of the provided router in NetCloud.
@NETCLOUD_API_INST.get('/routers', status_code=200)
def routers(response: Response,
            name: str = None,
            x_cp_api_id: str = Header(...),
            x_cp_api_key: str = Header(...),
            x_ecm_api_id: str = Header(...),
            x_ecm_api_key: str = Header(...)):
    # Check the credentials.
    if not (x_cp_api_id == 'demo-cp-api-id' and
            x_cp_api_key == 'demo-cp-api-key' and
            x_ecm_api_id == 'demo-ecm-api-id' and
            x_ecm_api_key == 'demo-ecm-api-key'):
        response.status_code = 401
        return {
            "status_code": 401,
            "exception": "unauthorized",
            "message": " Invalid Credentials i.e. missing or invalid keys.",
            "success": False
        }

    # Check the name.
    if name is None:
        # Return both the online and offline objects.
        return \
            {
                "data": [
                    {
                        "account":
                            "https://www.cradlepointecm.com/api/v2/accounts"
                            "/00000/",
                        "actual_firmware":
                            "https://www.cradlepointecm.com/api/v2/firmwares"
                            "/0000/",
                        "asset_id": None,
                        "config_status": "pending",
                        "configuration_manager":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/configuration_manager/",
                        "created_at": "2020-01-20T21:45:26.821880+00:00",
                        "custom1": None,
                        "custom2": None,
                        "description": "A sad offline NetCloud router :(",
                        "device_type": "router",
                        "full_product_name": "AER2200-600M",
                        "group":
                            "https://www.cradlepointecm.com/api/v2/groups"
                            "/000000/",
                        "id": "0000000",
                        "ipv4_address": "0.0.0.0",
                        "lans":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/lans/",
                        "last_known_location": None,
                        "locality": "US/Eastern",
                        "mac": "00:00:00:00:00:00",
                        "name": "Offline_site",
                        "overlay_network_binding":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000"
                            "/overlay_network_binding/",
                        "product":
                            "https://www.cradlepointecm.com/api/v2/"
                            "products/41/",
                        "reboot_required": False,
                        "resource_url":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/",
                        "serial_number": "MM000000000000",
                        "state": "offline",
                        "state_updated_at": "2020-04-27T07:53:45.995018+00:00",
                        "target_firmware":
                            "https://www.cradlepointecm.com/api/v2/"
                            "firmwares/4543/",
                        "updated_at": "2022-03-12T04:36:15.440665+00:00",
                        "upgrade_pending": True
                    },
                    {
                        "account":
                            "https://www.cradlepointecm.com/api/v2/accounts"
                            "/00000/",
                        "actual_firmware":
                            "https://www.cradlepointecm.com/api/v2/firmwares"
                            "/0000/",
                        "asset_id": None,
                        "config_status": "synched",
                        "configuration_manager":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/configuration_manager/",
                        "created_at": "2020-01-20T21:45:26.821880+00:00",
                        "custom1": None,
                        "custom2": None,
                        "description": "A happy online NetCloud router!",
                        "device_type": "router",
                        "full_product_name": "AER2200-600M",
                        "group":
                            "https://www.cradlepointecm.com/api/v2/groups"
                            "/000000/",
                        "id": "0000000",
                        "ipv4_address": "0.0.0.0",
                        "lans":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/lans/",
                        "last_known_location": None,
                        "locality": "US/Eastern",
                        "mac": "00:00:00:00:00:00",
                        "name": "Online_site",
                        "overlay_network_binding":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000"
                            "/overlay_network_binding/",
                        "product":
                            "https://www.cradlepointecm.com/api/v2/"
                            "products/41/",
                        "reboot_required": False,
                        "resource_url":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/",
                        "serial_number": "MM000000000000",
                        "state": "online",
                        "state_updated_at": "2020-04-27T07:53:45.995018+00:00",
                        "target_firmware":
                            "https://www.cradlepointecm.com/api/v2/"
                            "firmwares/4543/",
                        "updated_at": "2022-03-12T04:36:15.440665+00:00",
                        "upgrade_pending": True
                    }
                ],
                "meta":
                    {
                        "limit": 20,
                        "next": None,
                        "offset": 0,
                        "previous": None
                    }
            }
    elif name == 'Online_site':
        # Return the online dummy object.
        return \
            {
                "data": [
                    {
                        "account":
                            "https://www.cradlepointecm.com/api/v2/accounts"
                            "/00000/",
                        "actual_firmware":
                            "https://www.cradlepointecm.com/api/v2/firmwares"
                            "/0000/",
                        "asset_id": None,
                        "config_status": "synched",
                        "configuration_manager":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/configuration_manager/",
                        "created_at": "2020-01-20T21:45:26.821880+00:00",
                        "custom1": None,
                        "custom2": None,
                        "description": "A happy online NetCloud router!",
                        "device_type": "router",
                        "full_product_name": "AER2200-600M",
                        "group":
                            "https://www.cradlepointecm.com/api/v2/groups"
                            "/000000/",
                        "id": "0000000",
                        "ipv4_address": "0.0.0.0",
                        "lans":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/lans/",
                        "last_known_location": None,
                        "locality": "US/Eastern",
                        "mac": "00:00:00:00:00:00",
                        "name": "Online_site",
                        "overlay_network_binding":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000"
                            "/overlay_network_binding/",
                        "product":
                            "https://www.cradlepointecm.com/api/v2/"
                            "products/41/",
                        "reboot_required": False,
                        "resource_url":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/",
                        "serial_number": "MM000000000000",
                        "state": "online",
                        "state_updated_at": "2020-04-27T07:53:45.995018+00:00",
                        "target_firmware":
                            "https://www.cradlepointecm.com/api/v2/"
                            "firmwares/4543/",
                        "updated_at": "2022-03-12T04:36:15.440665+00:00",
                        "upgrade_pending": True
                    }
                ],
                "meta":
                    {
                        "limit": 20,
                        "next": None,
                        "offset": 0,
                        "previous": None
                    }
            }
    elif name == 'Offline_site':
        # Return the offline dummy object.
        return \
            {
                "data": [
                    {
                        "account":
                            "https://www.cradlepointecm.com/api/v2/accounts"
                            "/00000/",
                        "actual_firmware":
                            "https://www.cradlepointecm.com/api/v2/firmwares"
                            "/0000/",
                        "asset_id": None,
                        "config_status": "pending",
                        "configuration_manager":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/configuration_manager/",
                        "created_at": "2020-01-20T21:45:26.821880+00:00",
                        "custom1": None,
                        "custom2": None,
                        "description": "A sad offline NetCloud router :(",
                        "device_type": "router",
                        "full_product_name": "AER2200-600M",
                        "group":
                            "https://www.cradlepointecm.com/api/v2/groups"
                            "/000000/",
                        "id": "0000000",
                        "ipv4_address": "0.0.0.0",
                        "lans":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/lans/",
                        "last_known_location": None,
                        "locality": "US/Eastern",
                        "mac": "00:00:00:00:00:00",
                        "name": "Offline_site",
                        "overlay_network_binding":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000"
                            "/overlay_network_binding/",
                        "product":
                            "https://www.cradlepointecm.com/api/v2/"
                            "products/41/",
                        "reboot_required": False,
                        "resource_url":
                            "https://www.cradlepointecm.com/api/v2/routers"
                            "/0000000/",
                        "serial_number": "MM000000000000",
                        "state": "offline",
                        "state_updated_at": "2020-04-27T07:53:45.995018+00:00",
                        "target_firmware":
                            "https://www.cradlepointecm.com/api/v2/"
                            "firmwares/4543/",
                        "updated_at": "2022-03-12T04:36:15.440665+00:00",
                        "upgrade_pending": True
                    }
                ],
                "meta":
                    {
                        "limit": 20,
                        "next": None,
                        "offset": 0,
                        "previous": None
                    }
            }
    else:
        # Return no routers.
        return {
            "data": [],
            "meta":
                {
                    "limit": 20,
                    "next": None,
                    "offset": 0,
                    "previous": None
                }
        }
