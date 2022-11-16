# NetCloud-FastAPI

## Summary
This is a wrapper API implemented using FastAPI for NetCloud's official API.

_Note: If you have any questions or comments you can always use GitHub
discussions, or email me at farinaanthony96@gmail.com._

#### Why
FastAPI offers a convenient way to interface with an API via an interactive
web GUI, which allows people with little to no programming experience to
utilize the convenience of an API without having to code.

## Requirements
- Python >= 3.10.7
- fastapi
- uvicorn

## Usage
- This wrapper API is meant to run perpetually. To kick it off
  simply run the script using uvicorn:
  `uvicorn src.NetCloud-FastAPI:NETCLOUD_API_INST --host 0.0.0.0 --port 80 --root-path /netcloud-fastapi`
    
## Compatibility
Should be able to run on any machine with a Python interpreter and the
uvicorn library. This script was only tested on a Windows machine running
Python 3.10.7.

## Disclaimer
The code provided in this project is an open source example and should 
not be treated as an officially supported product. Use at your own 
risk. If you encounter any problems, please log an
[issue](https://github.com/CC-Digital-Innovation/NetCloud-FastAPI/issues).

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request ツ

## History
-  version 1.0.1 - 2022/11/16
   - Added README.md
   - Added LICENSE
   - Added module information and corrected spacing in the main 
     Python file
  

-  version 1.0.0 - 2022/08/29
   - Initial release

## Credits
Anthony Farina <<farinaanthony96@gmail.com>>
