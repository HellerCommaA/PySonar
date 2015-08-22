This is a relatively simple API wrapper around SendSonar.com's messaging service.  

This API is designed for use with Django, so it is written to be as awesome as possible. I'm still testing it to see if it will work in INSTALLED_APPS, otherwise, just import it directly.  

All of the endpoints will be exposed via this API that are exposed via the offical SendSonar API.

# Things you need in settings.py  

1) SONAR_PUB = 'YOUR_SONAR_API_PUBLIC_KEY_HERE'  # or set these as enviornment vars  
2) SONAR_PRIV = 'YOUR_SONAR_API_PRIVATE_KEY_HERE' # or set these as enviornment vars  
3) SONAR_URL = 'https://www.sendsonar.com/api/v1/' # or using sandbox.sendsonar.com  

Suggested use:  
When ever you wish to send a messsage to a customer in a view: just import pysonar, then use pysonar.send(TO, MESSAGE) within a  
`try:`  
`except pysonar.SonarError, e:`  
`except pysonar.InvalidPhoneNumber, e`  
`else:`  
style block.  

Requires Kennith Reitz's Requests 

MIT Licensed.
