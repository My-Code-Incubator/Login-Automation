from flask import request, Response, json
import requests
import os
from src.utils.reg_session import generate_signature
def register_session():
  """
  Registers a new session by sending a POST request to the API with device and user information.

  Parameters:
  None

  Returns:
  Response: A Flask response object containing a JSON message indicating success or failure.
  """
  try:  
    user_agent = request.headers.get('User-Agent')  
    data = request.json
    
    device_id = data['device_id']
    user_agent = user_agent.split()[0]
    signature = generate_signature()
    
    if not all([ device_id, user_agent ]):
      return Response(json.dumps({'error': 'All fields are required'}), status=400)
    session_data = {
      "device_id": device_id,
      "user_agent": user_agent,
      "signature": signature
    }
    
    response = requests.post(
            os.getenv('API_URI'),
            json=session_data
    )
    
    if response.status_code == 201:
      response = response.json()
      user_id = response['id']
      return Response(json.dumps({'message': 'Session registered successfully', "user_id": user_id}), status=201)

  except Exception as e:
    return Response(json.dumps({'error': str(e)}), status=500)
  
  