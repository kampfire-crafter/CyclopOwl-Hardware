from enum import Enum

class CommandAction(Enum):
    """Defines the actions that can be performed."""
    
    ENABLE_STREAMING = "ENABLE_STREAMING"  # Action to enable streaming from camera
    DISABLE_STREAMING = "DISABLE_STREAMING"  # Action to disable streaming from camera
    ROTATE = "ROTATE"  # Action to rotate the camera
