import TouchPortalAPI as TP
import os
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
# Setup callbacks and connection
TPClient = TP.Client("GitUtilsPlugin")

# This event handler will run once when the client connects to Touch Portal
@TPClient.on(TP.TYPES.onConnect) # Or replace TYPES.onConnect with 'info'
def onStart(data):
    print("Connected!", data)
    logging.debug("Connected!", data)

    #dontbeused for now.
    TPClient.stateUpdate("ExampleState", "Connected!")

# Action handlers, called when user activates one of this plugin's actions in Touch Portal.
@TPClient.on('action')
def onAction(data):
    print(data)
    # do something based on the action ID and the data value
    if data['actionId'] == "OpenGitBash":
      # get the value from the action data (a string the user specified)
      action_value = TPClient.getActionDataValue(data.get('data'), 'CONFIG_DIR')
      cmd = 'start C:\Program" "Files\Git\git-bash.exe --cd='+action_value+''
      logging.debug(f"Tentando executar {cmd}")
      os.system(cmd)

      print(action_value)
      # We can also update our ExampleStates with the Action Value
      TPClient.stateUpdate("ExampleStates", action_value)



# Shutdown handler, called when Touch Portal wants to stop your plugin.
@TPClient.on('closePlugin')# or 'closePlugin'
def onShutdown(data):
    print("Got Shutdown Message! Shutting Down the Plugin!")
    # Terminates the connection and returns from connect()
    TPClient.disconnect()

# After callback setup like we did then we can connect.
# Note that `connect()` blocks further execution until
# `disconnect()` is called in an event handler, or an
# internal error occurs.

logging.debug(f"Tentando conectar")

TPClient.connect()